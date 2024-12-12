import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch, Mock
from azure_api import fetch_sign_in_logs, get_access_token
from datetime import datetime
from tests.test_output.mock_data import mock_sign_in_response

@patch("azure_api.requests.post")
def test_get_access_token(mock_post):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "token_type": "Bearer",
        "expires_in": 3599,
        "ext_expires_in": 3599,
        "access_token": "mock_token",
    }
    mock_post
    mock_post.return_value = mock_response

    creds = {"tenant_id": "test_tenant", "client_id": "test_client", "client_secret": "test_secret"}
    token = get_access_token(creds)
    assert token == "mock_token"

@patch("azure_api.requests.get")
@patch("azure_api.requests.post")  
def test_fetch_sign_in_logs(mock_post, mock_get):
    mock_token_response = Mock()
    mock_token_response.status_code = 200
    mock_token_response.json.return_value = {
        "token_type": "Bearer",
        "expires_in": 3599,
        "ext_expires_in": 3599,
        "access_token": "mock_token",
    }
    mock_post.return_value = mock_token_response

    mock_api_response = Mock()
    mock_api_response.status_code = 200
    mock_api_response.json.return_value = mock_sign_in_response
    mock_get.return_value = mock_api_response

    creds = {"tenant_id": "test_tenant", "client_id": "test_client", "client_secret": "test_secret"}
    start_date = datetime(2024, 12, 7)
    end_date = datetime(2024, 12, 9)

    logs = fetch_sign_in_logs(creds, start_date, end_date)
    assert logs == mock_sign_in_response
