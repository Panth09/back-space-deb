# app/inference.py
from typing import Tuple, List
import io
from PIL import Image
import numpy as np
import time
import os

try:
    import torch
except ImportError:
    torch = None

class DipakModel:
    def __init__(self, weights_path: str):
        self.weights_path = weights_path
        # Load your real model here
        # Example:
        # self.model = torch.jit.load(weights_path, map_location="cpu").eval()
        self.ready = os.path.exists(weights_path)

    def infer(self, image_bytes: bytes) -> Tuple[float, List[dict]]:
        """Return (risk_score, list of bbox dicts). Stubbed for now."""
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        w, h = img.size
        # TODO: replace with real inference from Dipak's model
        # demo: make a fake bbox
        time.sleep(0.05)
        bbox = {
            "x": 0.2 * w, "y": 0.3 * h, "w": 0.15 * w, "h": 0.18 * h,
            "label": "debris", "confidence": 0.82
        }
        debris = [bbox]
        risk_score = 0.65
        return risk_score, debris

model: DipakModel | None = None

def init_model(weights_path: str):
    global model
    model = DipakModel(weights_path)

def run_inference(image_bytes: bytes):
    if model is None:
        raise RuntimeError("Model not initialized")
    return model.infer(image_bytes)
