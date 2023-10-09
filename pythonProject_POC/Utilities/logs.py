import logging


class Logs:
    """
    ----------- issues with the Logs() -------------
    -- Utilities/logs.py --
    1. constructor created for the Logs()
    2. constructor has  the filename & location, format & datefmt
    3. constructor uses self to connect the logger to this class
    import added in test_LoginPage.py file = from Utilities.logs import Logs

    -- Tests/test_LoginPage.py --
    1. from Utilities.logs import Logs brings the logs.py
    2. creates an object of teh Logs() class
    3. uses the object to call one of the methods that prints a message.
    4. This should create a log file in the location defined in the constructor
    5. This should print the message from the log method that is called here

    6. Issue =  #4 & #5 does not happens.
    """


    def __init__(self):
        self.logger = None
        logging.basicConfig(filename="C://Users//sindh//PycharmProjects//?pythonProject_POC//Utilities//test.log",
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger("demo_logger")
        self.logger = logger
        self.logger.setLevel(logging.DEBUG)

    def log_debug_message(self):
        self.logger.debug("This is debug message")

    def log_info_message(self):
        self.logger.info("This is info message")

    def log_warning_message(self):
        self.logger.warning("This is warning message")

    def log_error_message(self):
        self.logger.error("This is error message")

    def log_critical_message(self):
        self.logger.critical("This is critical message")
