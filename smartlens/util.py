import base64
import json
import os
import re
import urllib.request

def makeRequest(url, data, apiKey):
    req =  urllib.request.Request(url, data=bytes(data, encoding='utf-8'))
    req.add_header('User-Agent', 'Mozilla/5.0')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', apiKey)
    try:
        res = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        return e.read()

    return res.read()

def checkIfValidURL(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return (re.match(regex, url) is not None)

def isBase64(sb):
    try:
        if isinstance(sb, str):
            # If there's any unicode here, an exception will be thrown and the function will return false
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False