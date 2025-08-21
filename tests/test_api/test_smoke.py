from http import HTTPStatus

import requests

def test_status(app_url):
    response = requests.get(f"{app_url}/api/status")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["users"] == True