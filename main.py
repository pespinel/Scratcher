from flow import flow
import utils.constants as constants
from utils.driver_wrapper import DriverWrapper

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
            username = row[0].split(constants.CSV_SEPARATOR)[0]
            password = row[0].split(constants.CSV_SEPARATOR)[1]
            while not completed:
                try:
                    flow(driver_wrapper.driver, username, password)
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
