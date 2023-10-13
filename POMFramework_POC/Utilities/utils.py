import openpyxl
import inspect
import logging
from openpyxl import Workbook, load_workbook
from Config.config import TestData

# The 'Utils' class serves as a utility class within a test automation framework and provides various helper methods.
# It is designed to offer convenient functions for logging, reading data from Excel files, and other utility functions.
# The key methods and features within this class include:
# - 'log_to_file_output': A method to create and configure logging for test activities, which can be used for debugging and reporting.
# - 'get_data': A method for reading data from an Excel file, specified by the 'TestData' class, based on the provided column name.
# Overall, the 'Utils' class simplifies common tasks and enhances test automation by providing reusable utility methods.

class Utils:
    @staticmethod
    def log_to_file_output(logLevel=logging.DEBUG):
        # 1. Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # 1. create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # 2. create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        # 3. create formatter - how you want your logs to be formatted
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%Y %I:%M:%S %p')
        # 4. add formatter to console or file handler
        fh.setFormatter(formatter1)
        # 5. add console handler to logger
        logger.addHandler(fh)
        return logger

    # - 'get_data': A method for reading data from an Excel file, specified by the 'TestData' class, based on the provided column name.
    # The 'get_data' method retrieves data from an Excel file, allowing easy access to test data during test case execution.
    def get_data(column_name):
        # Specify the Excel file path
        excel_file_path = TestData.EXCEL_FILE_PATH
        sheet_name = TestData.SHEET_NAME
        row_number = 4  # Use an integer, not a string

        try:
            workbook = openpyxl.load_workbook(excel_file_path)
            workSheet = workbook[sheet_name]
            headings = [workSheet.cell(1, col).value for col in range(1, workSheet.max_column + 1)]
            row_data = {}

            """print("maximum col: " + str(workSheet.max_column))"""

            for col_num in range(1, workSheet.max_column + 1):
                heading = headings[col_num - 1]
                value = workSheet.cell(row_number, col_num).value
                row_data[heading] = value

            # Print the data
            """
            for heading, value in row_data.items():
                print(f"{heading}: {value}")
            """

            if column_name in row_data:
                value = row_data[column_name]
                print(f"{column_name}: {value}")  # Print the value of the specified column
                return value
            else:
                return None

        except Exception as e:
            print("E: ", e)
            return {}

