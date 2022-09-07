import setting
import logging


languageUser = ''

def main():
    logging.info('def - functionMain.main -- start')
    getLanguageUser()
    menu(languageUser)

def getLanguageUser():
    logging.info('def - getLanguageUser -- start')
    global languageUser
    languageUser = setting.languageUser()

def menu(languageUser):
    if languageUser == "ru":
        print('работа с одним Excel файлом')

    elif languageUser == "cz":
        print('prace z jednim Excel souborem')

    elif languageUser == "en":
        print('work with one Excel file')

