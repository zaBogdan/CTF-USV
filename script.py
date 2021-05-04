#!/usr/bin/python3
from PIL import Image
import pytesseract
import requests
from io import BytesIO

url = "http://80.96.120.172/ctf-USV/captcha.php"
response = requests.get(url)

img = Image.open(BytesIO(response.content))

print(pytesseract.image_to_string(img, config='--psm 6'))
