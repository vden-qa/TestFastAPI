from http import HTTPStatus

import pytest
import requests
from app.api.users.schemas import User

@pytest.fixture()
def users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK
    return response.json()


def test_users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK
    users = response.json()
    for user in users:
        User.model_validate(user)
    assert len(response.json()) == 11

def test_users_no_duplicates(users):
    users_ids = [user["id"] for user in users]
    assert len(users_ids) == len(set(users_ids))

@pytest.mark.parametrize("user_id", [1, 6, 11])
def test_user(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.OK
    user = response.json()
    User.model_validate(user)

@pytest.mark.parametrize("user_id", [-1,0,13])
def test_user_nonexistend_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND

@pytest.mark.parametrize("user_id", ["id", "id1"])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

@pytest.mark.parametrize("page,size,total,pages,quantity,initial_number",
                         [
                             (1,5,11,3,5,1),
                             (2,5,11,3,5,6),
                             (3,5,11,3,1,11),
                             (1,10,11,2,10,1),
                             (2,10,11,2,1,11),
                             (1,100,11,1,11,1)
                         ])
def test_paginate_users(app_url, page, size, total, pages, quantity, initial_number):
    params = {"page": page, "size": size}
    response = requests.get(f"{app_url}/api/users/paginate", params=params)

    assert response.status_code == HTTPStatus.OK
    users = response.json()
    assert users["items"][0]["id"] == initial_number
    assert users["total"] == total
    assert users["page"] == page
    assert users["size"] == size
    assert users["pages"] == pages
    users_ids = [user["id"] for user in users["items"]]
    assert len(users_ids) == quantity

@pytest.mark.parametrize("page,size", [("d",100),(1,"d"),(0,100),(1,0)])
def test_paginate_user_invalid_values(app_url,page,size):
    params = {"page": page, "size": size}
    response = requests.get(f"{app_url}/api/users/paginate", params=params)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

@pytest.mark.parametrize("page,size", [(3,100),(11,100)])
def test_paginate_user_nonexistend_values(app_url,page,size):
    params = {"page": page, "size": size}
    response = requests.get(f"{app_url}/api/users/paginate", params=params)
    assert response.status_code == HTTPStatus.NOT_FOUND

