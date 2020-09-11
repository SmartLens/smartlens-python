from __future__ import absolute_import, division, print_function

import os
import re
import base64
import json
import urllib
from .tags import _runTags
from .captions import _runCaptions
from .documents import _runDocuments, _runTextAnalysis

# SmartLens Python bindings
# API docs at https://smartlens.ai/docs
# Authors:
# Michael Royzen <michael@smartlens.ai>

# Configuration variables

api_key = None

def runTags(image):
    response = _runTags(image, api_key)
    return response

def runCaptions(image):
    response = _runCaptions(image, api_key)
    return response

def runDocumentAI(document, customExtractions=None):
    response = _runDocuments(document, customExtractions, api_key)
    return response

def runTextAnalysis(text, customExtractions=None):
    response = _runTextAnalysis(text, customExtractions, api_key)
    return response