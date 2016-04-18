# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from datetime import datetime

#--Generic Variables for use through Appium connection
K_APP_FILE_NAME = '/my_app.zip'
K_APPIUM_VER = '1.5.1'
K_APP_PLATFORM_NAME = 'iOS'
K_APP_PLATFORM_VER = '9.2'
K_DEVICE_NAME = 'iPhone Simulator'
K_APP_BROWSER_NAME = ''
k_APP_OS = 'iOS'

#--Webdriver property
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

K_WD_EXPLICITY_WAIT = 20
#K_WD_REMOTE_URL = 'http://ondemand.saucelabs.com:80/wd/hub'
K_WD_REMOTE_URL = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (SAUCE_USERNAME, SAUCE_ACCESS_KEY)

#--Result Files
K_RST_FILE = '/Result/test.txt'
K_RST_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + K_RST_FILE
K_RST_HTML_FILE = '/result.html'
K_RST_HTML_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + K_RST_HTML_FILE
K_RST_PDF_FILE = 'Report'

#--Execption/Fails 
K_FILE_NOT_FOUND = 'File not found for given path %s'

#Login
K_URL_1 = 'serverName1'
K_USER_1 = 'userName1'
K_PASSWORD_1 = 'passName1'
K_PASSWORD_WRONG_1 = 'pass_wrong'
K_SELF_SIGNED_1 = True

K_URL_2 = 'serverName2'
K_USER_2 = 'userName2'
K_PASSWORD_2 = 'passName2'
K_SELF_SIGNED_2 = True

#Create Folder
K_FOLDER_NAME = 'Test Folder ß'

class utility_functions():

    #--Common utils for Apending string in test.txt file.
    def write_comment_in_file(self,text):
        f = open(K_RST_FILE_PATH, "a")
        f.write('Time: %s ' % datetime.now())
        f.write(text)
        f.close()
        return True
