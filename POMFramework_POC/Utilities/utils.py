import openpyxl
import inspect
import logging
from openpyxl import Workbook, load_workbook


class Utils:
    def log_to_file_output(logLevel=logging.DEBUG):
        # 1. Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # 1. create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # 2. create console handler or file handler and set the log level
        fh = logging.FileHandler("automation1.log")
        # 3. create formatter - how you want your logs to be formatted
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%Y %I:%M:%S %p')
        # 4. add formatter to console or file handler
        fh.setFormatter(formatter1)
        # 5. add console handler to logger
        logger.addHandler(fh)
        return logger


    def get_data(column_name):
        # Specify the Excel file path
        excel_file_path = "C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel.xlsx"
        sheet_name = "Sheet1"
        row_number = 4  # Use an integer, not a string

        try:
            workbook = openpyxl.load_workbook(excel_file_path)
            workSheet = workbook[sheet_name]
            headings = [workSheet.cell(1, col).value for col in range(1, workSheet.max_column + 1)]
            row_data = {}

            print("maximum col: " + str(workSheet.max_column))

            for col_num in range(1, workSheet.max_column + 1):
                heading = headings[col_num - 1]
                value = workSheet.cell(row_number, col_num).value
                row_data[heading] = value

            # Print the data
            for heading, value in row_data.items():
                print(f"{heading}: {value}")

            if column_name in row_data:
                value = row_data[column_name]
                print(f"{column_name}: {value}")  # Print the value of the specified column
                return value
            else:
                return None

        except Exception as e:
            print("E: ", e)
            return {}


    """
    def read_data_from_excel(file_name, sheet):
        datalist = []
        wb = load_workbook(filename=file_name)
        sh = wb[sheet]

        row_ct = sh.max_row
        col_ct = sh.max_column

        for i in range(1, row_ct + 1):
            row = []
            for j in range(1, col_ct + 1):
                row.append(sh.cell(row=1, column=j).value)
            datalist.append(row)
        return datalist
    """