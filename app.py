from flask import Flask, request
from json import dumps
from PIL.Image import open
from pytesseract import pytesseract, image_to_string

app = Flask(__name__)
pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract'


@app.route("/ocr")
def ocr():
    try:
        image = open(request.files['image'])
        return dumps({'status': True, 'message': 'Success', 'data': image_to_string(image=image)})
    except Exception as e:
        return dumps({'status': False, 'message': 'Failure', 'data': str(e)})

