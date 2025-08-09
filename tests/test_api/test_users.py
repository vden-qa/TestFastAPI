import requests
from tests.test_api.base_data import data_users


def test_unknown_get_all(base_url):
    response = requests.get(base_url + '/api/users/all')
    assert response.status_code == 200
    assert len(response.json()) == len(data_users())

def test_unknown_get_by_id_existing(base_url):
    response = requests.get(base_url +'/api/users/7')
    assert response.status_code == 200
    assert response.json() == next((item for item in data_users() if item["id"] == 7 ), None)

def test_unknown_get_by_id_nonexistent(base_url):
    response = requests.get(base_url + '/api/users/1')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Запись с id=1 не найдена'