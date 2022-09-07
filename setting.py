import os
import logging

settingList = {}
languageUser = ''

def setting():
    logging.info('def - setting.setting -- start')
    language()

def language():
    logging.info('def - setting.language -- start')
    global settingList
    global languageUser
    fileWithSetting = "Setting.conf"
    fileList = os.listdir(os.getcwd())
    if fileWithSetting not in fileList:
        logging.info('def - setting.language -- not file setting')
        languageUser = input('language?    (ru / cz / en) :   ')
        logging.info('def - setting.language -- get user language')
        #settingList.insert(0, languageUser)
        write2settingFile(languageUser, 'w')
        logging.info('def - setting.language -- write user language to setting file')
    else:
        logging.error('def - setting.language -- file setting is found')
        with open(fileWithSetting) as fileWithSetting:
            logging.info('def - setting.language -- setting file is reading')
            lines = fileWithSetting.readlines()
            logging.info('def - setting.language -- languageUser is setting')
            settingList = dict(languageUser=lines[0])

def write2settingFile(settingCommand, proppertis):
    settingFile = open("Setting.conf", proppertis)
    settingFile.write(settingCommand)
    settingFile.close()

def languageUser():
    for key in settingList.keys():
        if key == 'languageUser':
            return settingList.get(key)


