import getDataOneExcel
import setting
import logging


languageUser = ''

def main():
    logging.info('def - functionMain.main -- start')
    getLanguageUser()
    menu(languageUser)

def getLanguageUser():
    logging.info('def - functionMain.getLanguageUser -- start')
    global languageUser
    languageUser = setting.languageUser()

# main menu for user
def menu(languageUser):
    if languageUser == "ru":
        print('работа с одним Excel файлом')
        getDataOneExcel.main()

    elif languageUser == "cz":
        print('prace z jednim Excel souborem')

    elif languageUser == "en":
        print('work with one Excel file')

