import imp
from select import select
import pytest,requests,pdb,allure
import config
from page_obj import makemytrip_obj

@pytest.fixture()
def test_setup():
    global driver1
    driver1 = config.webdriver_obj().driver_obj()

    driver1.maximize_window()
    driver1.get(makemytrip_obj().url)
    print("Page Title is : %s" % driver1.title)
    yield 
    driver1.quit()

@allure.description("Valid page title test")
@allure.severity(severity_level="CRITICLE")
def test_page_title(test_setup):
    try:
        #pdb.set_trace()
        assert driver1.title.strip() == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
    finally:
        if(AssertionError):
            allure.attach(driver1.get_screenshot_as_png(), name="Invalid title name", attachment_type=allure.attachment_type.PNG)


@allure.description("Invalid page title test")
@allure.severity(severity_level="BLOCKER")
def test_page_invalid_title(test_setup):
    try:
        assert driver1.title.strip() == "MakeM - #1 Travel Website 50% OFF on Hotels, Flights & Holiday"
    finally:
        if(AssertionError):
            allure.attach(driver1.get_screenshot_as_png(), name="Invalid title name", attachment_type=allure.attachment_type.PNG)
