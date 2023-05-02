from selenium.webdriver.common.by import By


class EmailPage:
    email = None
    finishButton = None

    def __init__(self, driver):
        self.email = driver.find_element(By.ID, "email")
        self.finishButton = driver.find_element(
            By.XPATH, "//main/div/form/div/div[3]/button")

    def fill_email(self, email):
        self.email.send_keys(email)
