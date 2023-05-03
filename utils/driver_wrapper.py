from selenium import webdriver


class DriverWrapper:
    driver = None

    def __init__(self):
        super(DriverWrapper, self).__init__()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def open(self, url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()
