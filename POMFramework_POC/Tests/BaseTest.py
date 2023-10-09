import pytest


"""BaseTest calls the fixture to get the webdriver"""


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
