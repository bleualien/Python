from flask import Flask, request, jsonify
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import random 


#CONFIGURATION
app = Flask(__name__)
UPLOAD_DIR = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensuring class folders exist
for folder in ["pothole", "garbage", "unknown"]:
    os.makedirs(os.path.join(UPLOAD_DIR, folder), exist_ok=True)

#HELPER FUNCTIONS
def allowed_file(filename):
    """Check if uploaded file is an allowed image type"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def dummy_predict(image_path):
    """
    Mock YOLOv8 prediction.
    Replace this with real YOLOv8 inference for production.
    """
    classes = ['pothole', 'garbage']
    predicted_class = random.choice(classes)
    confidence = round(random.uniform(0.7, 0.95), 2)
    bbox = [50, 50, 200, 200]  # Dummy bounding box
    return {"class": predicted_class, "confidence": confidence, "bbox": bbox}

def save_image_to_folder(temp_path, predicted_class):
    """Save uploaded image into the correct class folder with a unique name"""
    save_folder = os.path.join(UPLOAD_DIR, predicted_class)
    os.makedirs(save_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{predicted_class}_{timestamp}.jpg"
    final_path = os.path.join(save_folder, new_filename)
    os.rename(temp_path, final_path)
    return final_path

#ROUTES
@app.route("/upload", methods=["POST"])
def upload_image():
    # Validate file presence
    if "image" not in request.files:
        return jsonify({"error": "No image part in request"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Save temporarily
        filename = secure_filename(file.filename)
        temp_path = os.path.join(UPLOAD_DIR, filename)
        file.save(temp_path)

        # Run prediction
        result = dummy_predict(temp_path)  
        predicted_class = result["class"]
        confidence = result["confidence"]

        # Save to correct folder
        final_path = save_image_to_folder(temp_path, predicted_class)

        # Return JSON response
        return jsonify({
            "status": "success",
            "predicted_class": predicted_class,
            "confidence": confidence,
            "saved_path": final_path
        })

    return jsonify({"error": "Invalid file type"}), 400

# MAIN
if __name__ == "__main__":
    app.run(debug=True)
