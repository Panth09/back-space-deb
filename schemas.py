# app/schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class BBox(BaseModel):
    x: float
    y: float
    w: float
    h: float
    label: str
    confidence: float

class DetectionResult(BaseModel):
    id: str = Field(..., description="DB id")
    satellite_id: str
    timestamp: datetime
    risk_score: float
    debris_count: int
    bboxes: List[BBox]
    image_ref: Optional[str] = None  # path/hash/url

class PredictResponse(BaseModel):
    result: DetectionResult

class ListResponse(BaseModel):
    items: List[DetectionResult]
    total: int

# For query filters
class DetectionQuery(BaseModel):
    satellite_id: Optional[str] = None
    from_ts: Optional[datetime] = None
    to_ts: Optional[datetime] = None
    limit: int = 20
    skip: int = 0
