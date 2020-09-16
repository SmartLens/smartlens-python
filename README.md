# SmartLens Python Library

The SmartLens Python library provides convenient access to the SmartLens API from
applications written in the Python language. Integrate state-of-the-art AI into your application
in just five lines of code.

## Documentation

See the [API docs](https://smartlens.ai/docs).

## Installation

To install the package, simply run:

```sh
pip install smartlens
```

### Requirements

-   Python 3.6+

## Usage

The library needs to be configured with your account's API key which is
available in the [SmartLens Dashboard][api-keys]. Set `smartlens.api_key` to its
value:

```python
import smartlens
smartlens.api_key = "YOUR-API-KEY"

# tag image
tags = smartlens.runTags(
    image = "path/to/my/image"
)

# caption image
captions = smartlens.runCaptions(
    image = "path/to/my/image"
)

# process document
extractedItems = smartlens.runDocumentAI(
    document = "path/to/my/document",
    customExtractions = [{'natural_language_query': 'What is the salary?', 'answer_key': 'employee_salary'}] # Custom extractions are optional
)

# process text document
extractedItems = smartlens.runTextAnalysis(
    text = "path/to/my/text",
    customExtractions = [{'natural_language_query': 'What is the salary?', 'answer_key': 'employee_salary'}] # Custom extractions are optional
)
```

[api-keys]: https://dashboard.smartlens.ai

<!--
# vim: set tw=79:
-->
