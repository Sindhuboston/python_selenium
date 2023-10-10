import inspect
import logging
from openpyxl import Workbook, load_workbook
class Utils:
    def log_to_file_output(logLevel=logging.DEBUG):
        #1. Set class/method name from where its called
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


    def read_data_from_excel(file_name, sheet):
        datalist = []
        wb= load_workbook(filename=file_name )
        sh = wb[sheet]

        row_ct = sh.max_row
        col_ct = sh.max_column

        for i in range(1, row_ct+1):
            row = []
            for j in range(1, col_ct+1):
                row.append(sh.cell(row=1, column=j).value)
            datalist.append(row)
        return datalist

