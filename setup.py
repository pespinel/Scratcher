import utils.constants as constants
from utils.driver_wrapper import DriverWrapper


def setup():
    driver_wrapper = DriverWrapper()
    driver_wrapper.open(constants.SCRATCH_REGISTRATION_URL)
    return driver_wrapper
