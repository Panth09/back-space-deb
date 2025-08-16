# app/routers/detections.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from fastapi import BackgroundTasks
from typing import Optional
from datetime import datetime
from bson import ObjectId

from app.db import get_db
from app.schemas import ListResponse, PredictResponse, DetectionQuery, BBox
from app.inference import run_inference
from app.models import serialize_detection
from app.routers.ws import manager, WSEvent

router = APIRouter(prefix="/api", tags=["detections"])

@router.post("/predict", response_model=PredictResponse)
async def predict(
    satellite_id: str = Form(...),
    image: UploadFile = File(...),
    background: BackgroundTasks = None,
    db=Depends(get_db)
):
    if image.content_type not in {"image/png", "image/jpeg", "image/jpg"}:
        raise HTTPException(status_code=400, detail="Only PNG/JPEG supported")

    img_bytes = await image.read()
    risk_score, debris = run_inference(img_bytes)

    doc = {
        "satellite_id": satellite_id,
        "timestamp": datetime.utcnow(),
        "risk_score": float(risk_score),
        "debris_count": len(debris),
        "bboxes": debris,
        "image_ref": None,  # store to S3/MinIO and save URL if needed
    }
    res = await db.detections.insert_one(doc)
    doc["_id"] = res.inserted_id

    # push to websocket listeners (non-blocking)
    if background:
        background.add_task(
            manager.broadcast_json,
            WSEvent(
                type="detection.created",
                payload=serialize_detection(doc)
            ).model_dump()
        )

    return {"result": serialize_detection(doc)}

@router.get("/detections", response_model=ListResponse)
async def list_detections(
    satellite_id: Optional[str] = None,
    from_ts: Optional[str] = None,
    to_ts: Optional[str] = None,
    limit: int = 20,
    skip: int = 0,
    db=Depends(get_db)
):
    query = {}
    if satellite_id:
        query["satellite_id"] = satellite_id
    if from_ts or to_ts:
        rng = {}
        if from_ts:
            rng["$gte"] = datetime.fromisoformat(from_ts)
        if to_ts:
            rng["$lte"] = datetime.fromisoformat(to_ts)
        query["timestamp"] = rng

    cursor = db.detections.find(query).sort("timestamp", -1).skip(skip).limit(min(limit, 100))
    docs = await cursor.to_list(length=min(limit, 100))
    total = await db.detections.count_documents(query)

    return {"items": [serialize_detection(d) for d in docs], "total": total}

@router.get("/detections/{det_id}", response_model=dict)
async def get_detection(det_id: str, db=Depends(get_db)):
    from bson.errors import InvalidId
    try:
        _id = ObjectId(det_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid id")
    doc = await db.detections.find_one({"_id": _id})
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    return serialize_detection(doc)
