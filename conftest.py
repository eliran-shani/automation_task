import pytest


def pytest_addoption(parser):
    parser.addoption('--sort', action="store", default="a",
                     help="Set sort option \n'a' - Ascending \n'd' - Descending")

    parser.addoption('--delimiter', action="store", default="c",
                     help="Set delimiter option \n'c' - Comma \n's' - Space  \n'n' - Line")


@pytest.fixture(scope="module")
def sort(request):
    return request.config.getoption('--sort')


@pytest.fixture(scope="module")
def delimiter(request):
    return request.config.getoption('--delimiter')
