import os
import cv2
import numpy as np
import base64
from flask import Flask, jsonify, request

from nopaddleocr import OCR

app = Flask(__name__)
ocr = OCR(os.path.join(os.path.dirname(__file__), '../models'))

@app.route('/ocr', methods=['GET'])
def process_image():
    base64_image = request.args.get('image')

    if not base64_image:
        return jsonify({"error": "No image data provided"}), 400

    try:
        image_data = base64.b64decode(base64_image)
        np_image = np.frombuffer(image_data, dtype=np.uint8)
        cv_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        if cv_image is None:
            return jsonify({"error": "Failed to decode image"}), 400

        result = ''.join(ocr(cv_image))

        return jsonify({
            "text": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


