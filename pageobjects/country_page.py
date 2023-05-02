from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CountryPage:
    select = None
    nextButton = None

    def __init__(self, driver):
        self.select = Select(driver.find_element(By.NAME, "country"))
        self.nextButton = driver.find_element(
            By.XPATH, "//main/div/form/div/div[3]/button")

    def pick_country(self, country):
        self.select.select_by_visible_text(country)
