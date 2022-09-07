# This is a sample Python script.
from openpyxl import load_workbook

import functionMain
import setting
import getDataOneExcel
import logging


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def excel():
    wb = load_workbook('c:/Users/User/Desktop/траты на авто.xlsx')
    print(wb.get_sheet_names())

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    #logging.basicConfig(filename="sample.log", level=logging.INFO)
    #console_out = logging.StreamHandler()
    #logging.info('--------- start APP ---------')
    #logging.basicConfig(handlers=(file_log, console_out),
    #                    format='[%(asctime)s | %(levelname)s]: %(message)s',
    #                    datefmt='%m.%d.%Y %H:%M:%S',
    #                    level=logging.INFO)

    file_log = logging.FileHandler('sample.log')
    console_out = logging.StreamHandler()

    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)

    logging.info('Info message??))')


    print_hi('PyCharm')
    #excel()
    setting.setting()
    print(setting.languageUser())
    #print(len(setting.settingList))
    functionMain.main()
