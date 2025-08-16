from flask import Flask, request, jsonify
from db import detections_collection
from datetime import datetime

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    satellite_id = request.form.get("satellite_id", "UNKNOWN")

    # Here you’d run Dipak's model inference on image_file
    detections = [
        {"debris_type": "metal fragment", "confidence": 0.92, "coordinates": [123.45, 67.89]},
        {"debris_type": "paint chip", "confidence": 0.81, "coordinates": [125.12, 69.01]}
    ]
    risk_level = "medium"
    model_version = "v2.3"

    # Save to MongoDB
    doc = {
        "satellite_id": satellite_id,
        "timestamp": datetime.utcnow().isoformat(),
        "detections": detections,
        "risk_level": risk_level,
        "processed_by_model": model_version
    }
    detections_collection.insert_one(doc)

    return jsonify({"message": "Detection saved", "detections": detections})

@app.route("/results", methods=["GET"])
def get_results():
    satellite_id = request.args.get("satellite_id")
    query = {}
    if satellite_id:
        query["satellite_id"] = satellite_id

    results = list(detections_collection.find(query, {"_id": 0}))
    return jsonify(results)

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)), debug=True)
