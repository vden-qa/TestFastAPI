import os
import pytest
import dotenv

dotenv.load_dotenv()

pytest.fixture(autouse=True)
def envs():
    dotenv.load_dotenv()

@pytest.fixture()
def app_url():
    return os.getenv("APP_URL")

# @pytest.fixture()
# def base_url(request):
#     base_url = request.config.getoption("--baseUrl")
#     return base_url
#
# def pytest_addoption(parser):
#     parser.addoption("--baseUrl", action="store", default="http://127.0.0.1:8000")
