import utils.constants as constants
from utils.driver_wrapper import DriverWrapper
from pageobjects.registration_page import RegistrationPage
from pageobjects.country_page import CountryPage
from pageobjects.birth_page import BirthPage
from pageobjects.gender_page import GenderPage
from pageobjects.email_page import EmailPage
from pageobjects.welcome_page import WelcomePage

import csv
import logging
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

logger = logging.basicConfig(filename=constants.LOG_NAME, level=logging.INFO)


if __name__ == "__main__":
    driver_wrapper = DriverWrapper()
    driver_wrapper.open(constants.SCRATCH_REGISTRATION_URL)

    with open(constants.CSV_NAME) as file:
        data = csv.reader(file)
        for row in data:
            completed = False
            username = row[0].split(";")[0]
            password = row[0].split(";")[1]
            while not completed:
                try:
                    registration_page = RegistrationPage(driver_wrapper.driver)
                    registration_page.fill_username(username)
                    registration_page.fill_password(password)
                    registration_page.nextButton.click()

                    country_page = CountryPage(driver_wrapper.driver)
                    country_page.pick_country(constants.COUNTRY)
                    country_page.nextButton.click()

                    birth_page = BirthPage(driver_wrapper.driver)
                    birth_page.fill_data()
                    birth_page.nextButton.click()

                    gender_page = GenderPage(driver_wrapper.driver)
                    gender_page.select.click()
                    gender_page.nextButton.click()

                    email_page = EmailPage(driver_wrapper.driver)
                    email_page.fill_email(constants.EMAIL_ACCOUNT)
                    sleep(0.5)
                    email_page.finishButton.click()

                    welcome_page = WelcomePage(driver_wrapper.driver)
                    logging.info("Account created: {}".format(username))
                except ElementNotVisibleException:
                    driver_wrapper.driver.close()
                    driver_wrapper = DriverWrapper()
                    driver_wrapper.open(constants.SCRATCH_REGISTRATION_URL)
                    logger.error("Error creating account: {}".format(username))
                else:
                    completed = True
                finally:
                    driver_wrapper.driver.delete_all_cookies()
                    driver_wrapper.driver.refresh()
