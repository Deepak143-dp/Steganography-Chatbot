from flask import Flask, render_template, request, send_file, jsonify
import os
from steg import encode_image, decode_image

# If your CSS is under 'ststic' folder, tell Flask about it; better: rename folder to 'static'
import os

app = Flask(__name__, static_folder="ststic")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html", decoded_message=None)

@app.route("/send", methods=["POST"])
def send_msg():
    message = request.form["message"]
    image = request.files["image"]

    img_path = os.path.join(UPLOAD_FOLDER, "input.png")
    image.save(img_path)

    encoded_path = encode_image(img_path, message)
    return send_file(encoded_path, as_attachment=True)

@app.route("/receive", methods=["POST"])
def receive_msg():
    image = request.files["image"]
    img_path = os.path.join(UPLOAD_FOLDER, "received.png")
    image.save(img_path)

    message = decode_image(img_path)
    return render_template("index.html", decoded_message=message)

if __name__ == "__main__":
    app.run(debug=True)