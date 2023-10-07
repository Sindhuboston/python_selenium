import pytest
from selenium import webdriver

class TestClass:

    @pytest.mark.usefixtures("init_driver")
    def test_Test1(self):
        self.driver.get("https://www.google.com")
        assert 4 == 5

