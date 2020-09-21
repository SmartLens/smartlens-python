import os
import re
import urllib
import base64
import json
from .util import makeRequest, checkIfValidURL, isBase64

def _runDocuments(image, customExtractions, apiKey):
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
        return {"error": "Your \"document\" parameter needs to be either a path to a local document (pdf, jpeg, or png), a string of base64 bytes (pdf, jpeg, or png), or a URL to a remote image (pdf, jpeg, or png)."}

    # Compose a JSON Predict request
    if customExtractions is not None:
        data = json.dumps({'document': imageBytes, 'custom_extractions': customExtractions})
    else:
        data = json.dumps({'document': imageBytes})

    url = 'https://api.smartlens.ai/v1/models/document-ai/predict'
    r = makeRequest(url, data, apiKey)
    r = r.decode('utf-8')

    dictResponse = json.loads(r)

    return dictResponse

def _runTextAnalysis(text, customExtractions, apiKey):
    # Compose a JSON Predict request
    if customExtractions is not None:
        data = json.dumps({'text': text, 'custom_extractions': customExtractions})
    else:
        data = json.dumps({'text': text})

    url = 'https://api.smartlens.ai/v1/models/analyze-text/predict'
    r = makeRequest(url, data, apiKey)
    r = r.decode('utf-8')

    dictResponse = json.loads(r)

    return dictResponse
