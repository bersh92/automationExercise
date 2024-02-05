from fixture.application import Application
import json
import os
import pytest

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# def pytest_addoption(parser):
#     # using for set the name of config as --reality and use it for next operations
#     parser.addoption("--reality", action="store", default="config_realitka.json")