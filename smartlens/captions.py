import os
import re
import urllib
import base64
import json
from .util import makeRequest, checkIfValidURL, isBase64

def _runCaptions(image, apiKey):
    imageBytes = None

    if (os.path.exists(image)):
        # Open a local image
        imageBytes = open(image, 'rb').read()
        imageBytes = base64.b64encode(imageBytes).decode('utf-8')
    elif (isBase64(image)):
        if isinstance(image, str):
            imageBytes = image
        elif isinstance(image, bytes):
            imageBytes = str(image, encoding='utf-8')
    elif (checkIfValidURL(image)):
        try:
            req =  urllib.request.Request(image)
            req.add_header('User-Agent', 'Mozilla/5.0')
            response = urllib.request.urlopen(req)
            imageBytes = response.read()
        except urllib.error.HTTPError:
            return {"error": "The URL you passed in is invalid."}
        imageBytes = base64.b64encode(imageBytes).decode('utf-8')
    else:
        return {"error": "Your \"image\" parameter needs to be either a path to a local image, a string of base64 bytes, or a URL to a remote image."}

    # Compose a JSON Predict request
    data = json.dumps({'image': imageBytes})

    url = 'https://api.smartlens.ai/v1/models/caption/predict'
    r = makeRequest(url, data, apiKey)
    r = r.decode('utf-8')

    dictResponse = json.loads(r)

    return dictResponse
