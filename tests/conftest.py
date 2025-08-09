import pytest


@pytest.fixture()
def base_url(request):
    base_url = request.config.getoption("--baseUrl")
    return base_url

def pytest_addoption(parser):
    parser.addoption("--baseUrl", action="store", default="http://127.0.0.1:8000")
