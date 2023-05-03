from captcha import captcha_solver
from flow import flow
from setup import setup
import utils.constants as constants

import csv
import logging
from selenium.common.exceptions import ElementNotVisibleException

logger = logging.basicConfig(filename=constants.LOG_NAME, level=logging.INFO)


if __name__ == "__main__":
    driver_wrapper = setup()

    with open(constants.CSV_NAME) as file:
        data = csv.reader(file)
        for row in data:
            completed = False
            username, password = row[0].split(constants.CSV_DELIMITER)
            while not completed:
                try:
                    flow(driver_wrapper.driver, username, password)
                    logging.info("Account created: {}".format(username))
                except ElementNotVisibleException:
                    logger.error("Error creating account: {}".format(username))
                    captcha_solver(driver_wrapper.driver)
                    driver_wrapper.close()
                    driver_wrapper = setup()
                else:
                    completed = True
                finally:
                    driver_wrapper.driver.delete_all_cookies()
                    driver_wrapper.driver.refresh()
