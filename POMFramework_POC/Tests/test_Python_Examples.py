import openpyxl


def test_testdatacalls():
    print("\nstart\n")
    workbook = openpyxl.load_workbook("C:\\Users\\sindh\\PycharmProjects\\POMFramework_POC\\TestData\\TDexcel.xlsx")
    workSheet = workbook["Sheet1"]

    dictHashMap = {}

    try:
        print("maximum row in the sheet: " + str(workSheet.max_row))
        # get tc_IDs:
        for tcNo in range(1,workSheet.max_row+1):
            current_tc_no = workSheet.cell(tcNo, 2).value
            print(current_tc_no)
            #dictHashMap[current_tc_no] =

    except Exception as e:
        print("E: ", e)
