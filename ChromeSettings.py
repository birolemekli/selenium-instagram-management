# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ChromeSettings:
    def __init__(self,chrome_path,mobile_emulator):
        self.chrome_path=chrome_path
        self._mobile_emulator=mobile_emulator

    def mobileDriver(self):
        mobile_emulation = {"deviceName": self._mobile_emulator}
        chrome_options = Options()
        chrome_options.add_argument('--window-size=500,900')
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        try:
            driver = webdriver.Chrome(executable_path=self.chrome_path,chrome_options=chrome_options)
            return driver
        except :
            print ('Error occurred while installing chrome driver...')
