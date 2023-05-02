from selenium.webdriver.common.by import By


class GenderPage:
    select = None
    nextButton = None

    def __init__(self, driver):
        self.select = driver.find_element(By.ID, "GenderRadioOptionPreferNot")
        self.nextButton = driver.find_element(
            By.XPATH, "//main/div/form/div/div[2]/button")
