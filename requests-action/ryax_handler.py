# Copyright 2022 Ryax Technologies
# Use of this trigger code is governed by a BSD-style
# license that can be found in the LICENSE file.
import os

# Test imports
import requests

def handle(inputs: dict) -> dict:
    """Simple example test echo handler"""
    #outputs = copy.deepcopy(inputs)
    outputs = dict()
    url_str = inputs["url"]
    body = requests.get(url_str)
    outputs["body"] = body.text

    return outputs
