from selenium.webdriver.common.by import By


class WelcomePage:
    span = None

    def __init__(self, driver):
        self.span = driver.find_element(
            By.XPATH, "//main/div/form/div/div[2]/div/div[2]/span")
