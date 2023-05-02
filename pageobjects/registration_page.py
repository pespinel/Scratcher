from selenium.webdriver.common.by import By


class RegistrationPage:
    username = None
    password = None
    confirmPassword = None
    nextButton = None

    def __init__(self, driver):
        self.username = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.confirmPassword = driver.find_element(By.NAME, "passwordConfirm")
        self.nextButton = driver.find_element(
            By.XPATH, "//main/div/form/div/div[2]/button")

    def fill_username(self, username):
        self.username.send_keys(username)

    def fill_password(self, password):
        self.password.send_keys(password)
        self.confirmPassword.send_keys(password)
