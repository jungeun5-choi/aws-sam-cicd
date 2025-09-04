# tests/test_app.py

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apigateway.app import lambda_handler

def test_lambda_handler_with_valid_query_param():
    # given: 정상적인 foo 파라미터가 포함된 event
    event = {
        "queryStringParameters": {
            "foo": "banana"
        }
    }
    context = {}

    # when
    result = lambda_handler(event, context)

    # then
    assert result["statusCode"] == 200
    assert result["body"] == "banana"

def test_lambda_handler_with_missing_query_param():
    # given: queryStringParameters가 없는 event
    event = {}
    context = {}

    # when / then
    with pytest.raises(KeyError):
        lambda_handler(event, context)
