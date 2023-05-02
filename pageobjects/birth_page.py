from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BirthPage:
    month = None
    year = None
    nextButton = None

    def __init__(self, driver):
        self.month = Select(driver.find_element(By.NAME, "birth_month"))
        self.year = Select(driver.find_element(By.NAME, "birth_year"))
        self.nextButton = driver.find_element(
            By.XPATH, "//main/div/form/div/div[3]/button")

    def fill_month(self, month):
        self.month.select_by_visible_text(month)

    def fill_year(self, year):
        self.year.select_by_visible_text(year)

    def fill_data(self):
        self.fill_month("Enero")
        self.fill_year("2015")
