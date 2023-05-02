import utils.constants as constants
from pageobjects.registration_page import RegistrationPage
from pageobjects.country_page import CountryPage
from pageobjects.birth_page import BirthPage
from pageobjects.gender_page import GenderPage
from pageobjects.email_page import EmailPage
from pageobjects.welcome_page import WelcomePage

from time import sleep


def flow(driver, username, password):
    registration_page = RegistrationPage(driver)
    registration_page.fill_username(username)
    registration_page.fill_password(password)
    registration_page.nextButton.click()

    country_page = CountryPage(driver)
    country_page.pick_country(constants.COUNTRY)
    country_page.nextButton.click()

    birth_page = BirthPage(driver)
    birth_page.fill_month(constants.BIRTH_MONTH)
    birth_page.fill_year(constants.BIRTH_YEAR)
    birth_page.nextButton.click()

    gender_page = GenderPage(driver)
    gender_page.select.click()
    gender_page.nextButton.click()

    email_page = EmailPage(driver)
    email_page.fill_email(constants.EMAIL_ACCOUNT)
    sleep(0.5)
    email_page.finishButton.click()

    welcome_page = WelcomePage(driver)
