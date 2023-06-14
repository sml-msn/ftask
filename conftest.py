import pytest

def pytest_addoption(parser):
    parser.addoption("--datapath", action="store")
    parser.addoption("--modelpath", action="store")

@pytest.fixture(scope='session')
def datapath(request):
    data = request.config.option.datapath
    if data is None:
        pytest.skip()
    return data
    
@pytest.fixture(scope='session')
def modelpath(request):
    model = request.config.option.modelpath
    if model is None:
        pytest.skip()
    return model