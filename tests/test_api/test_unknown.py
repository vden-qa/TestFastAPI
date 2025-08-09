import requests
from tests.test_api.base_data import data_unknown


def test_unknown_get_all(base_url):
    response = requests.get(base_url + '/api/unknown/all')
    assert response.status_code == 200
    assert len(response.json()) == len(data_unknown())

def test_unknown_get_by_id_existing(base_url):
    response = requests.get(base_url +'/api/unknown/1')
    assert response.status_code == 200
    assert response.json() == next((item for item in data_unknown() if item["id"] == 1 ), None)

def test_unknown_get_by_id_nonexistent(base_url):
    response = requests.get(base_url + '/api/unknown/11')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Запись с id=11 не найдена'