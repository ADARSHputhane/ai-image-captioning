import os
import certifi

# Force the environment to use the correct SSL certificates
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

print("Loading BLIP Model... (This might take a minute on the first run)")
# We use the 'base' model for a good balance of speed and accuracy
# Point to the local directory you just cloned
processor = BlipProcessor.from_pretrained("./blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("./blip-image-captioning-base")
print("Model loaded successfully!")


@app.route("/", methods=["GET"])
def index():
    """Renders the frontend interface."""
    return render_template("index.html")


@app.route("/caption", methods=["POST"])
def generate_caption():
    """Handles image upload and generates the caption."""
    # Check if the post request has the file part
    if "image" not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Save the file temporarily
        file.save(filepath)

        try:
            # Open and convert the image to RGB (required by BLIP)
            raw_image = Image.open(filepath).convert("RGB")

            # Process the image and generate the caption
            inputs = processor(raw_image, return_tensors="pt")

            # Generate output; max_new_tokens prevents the model from cutting off early
            out = model.generate(**inputs, max_new_tokens=50)
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Return the caption and the path to display the image on the frontend
            return jsonify(
                {"caption": caption.capitalize(), "image_url": f"/{filepath}"}
            )

        except Exception as e:
            return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the app on port 5000
    app.run(debug=False, host="0.0.0.0", port=5000)
