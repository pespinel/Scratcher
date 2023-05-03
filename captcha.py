from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By


def captcha_solver(driver):
    solver = RecaptchaSolver(driver=driver)
    recaptcha_iframe = driver.find_element(
        By.XPATH, '//iframe[@title="reCAPTCHA"]'
    )
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
