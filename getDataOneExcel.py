import setting
import logging
from openpyxl import load_workbook


languageUser = ''
def languageUser2222():
    print('')

def main():
    logging.info('def getDataOneExcel.main -- start')
    readExcel()

def readExcel():
    wb = load_workbook('c:/Users/User/Desktop/testdata.xlsx')
    print(wb.get_sheet_names())