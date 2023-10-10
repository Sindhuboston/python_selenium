import logging

import Utilities


class Logs:
    def log_to_file_output(self):
        # 1. create logger
        logger = logging.getLogger(Utilities.__name__)
        logger.setLevel(logging.DEBUG)
        # 2. create console handler or file handler and set the log level
        "below code is to display output in the file"
        fh = logging.FileHandler("demologfile.log")
        # 3. create formatter - how you want your logs to be formatted
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%Y %I:%M:%S %p')
        # 4. add formatter to console or file handler
        fh.setFormatter(formatter1)
        # 5. add console handler to logger
        logger.addHandler(fh)
        # 6. application code - log messages

        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")

        """
           ld1=Logs()
           ld1.log_to_file_output()
        """

    def log_to_console_output(self):
        # 1. create logger
        logger = logging.getLogger("demolog")
        logger.setLevel(logging.DEBUG)
        # 2. create console handler or file handler and set the log level
        "below code is to display output in the console"
        ch = logging.StreamHandler()
        # 3. create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # 4. add formatter to console or file handler
        ch.setFormatter(formatter)
        # 5. add console handler to logger
        logger.addHandler(ch)
        # 6. application code - log messages

        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")


ld = Logs()
ld.log_to_console_output()
