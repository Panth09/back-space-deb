# app/models.py
from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from app.schemas import BBox

def serialize_detection(doc) -> dict:
    return {
        "id": str(doc["_id"]),
        "satellite_id": doc["satellite_id"],
        "timestamp": doc["timestamp"],
        "risk_score": doc["risk_score"],
        "debris_count": doc["debris_count"],
        "bboxes": [BBox(**b).model_dump() for b in doc["bboxes"]],
        "image_ref": doc.get("image_ref")
    }
