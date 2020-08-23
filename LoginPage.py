# coding=utf-8
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
class LoginPage:
    def __init__(self,driver,url,username,password):
        self.driver=driver
        self._url=url
        self._username=username
        self._password=password

    def loginPage(self):
        print("Instagramm logging in...")
        self.driver.get(self._url)
        sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article/div/div/h1')))
            girisYapButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')
            girisYapButton.click()

            kullaniciAdi = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))
            kullaniciAdi.clear()
            kullaniciAdi.send_keys(self._username)

            password =WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))
            password.clear()
            password.send_keys(self._password)

            girisButon = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))
            girisButon.click()

            simdiDegil = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/button')))
            simdiDegil.click()

            iptalButon = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
            iptalButon.click()
            try:
                simdiDegil2 = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
                simdiDegil2.click()
            except:
                pass
            print("Login to the Instagram main page...")
        except:
            print ('An error has occurred on the login page.\nThe application is closing...')
            self.driver.close()
            sys.exit(2)
