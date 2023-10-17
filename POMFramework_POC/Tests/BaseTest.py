import pytest


"""BaseTest is designed to retrieve the webdriver through the fixture defined in conftest.py"""


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass