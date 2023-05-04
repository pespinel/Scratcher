from flow import flow
from setup import setup
import utils.constants as constants

import csv
import logging
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

logger = logging.basicConfig(filename=constants.LOG_NAME, level=logging.INFO)


if __name__ == "__main__":
    driver_wrapper = setup()

    with open(constants.CSV_NAME, encoding=constants.ENCODING) as file:
        data = csv.reader(file, skipinitialspace=True)
        for row in data:
            completed = False
            username = row[0].split(constants.CSV_DELIMITER)[
                0].replace('\ufeff', '')
            password = row[0].split(constants.CSV_DELIMITER)[
                1].replace('\ufeff', '')
            while not completed:
                try:
                    flow(driver_wrapper.driver, username, password)
                except Exception:
                    driver_wrapper.close()
                    driver_wrapper = setup()
                else:
                    completed = True
                    logging.info("Account created: {}".format(username))
                finally:
                    driver_wrapper.driver.delete_all_cookies()
                    driver_wrapper.driver.refresh()
