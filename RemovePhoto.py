
# coding=utf-8
from time import sleep
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RemovePhoto:
    def __init__(self,driver,sayi):
        self.driver=driver
        self._resimCount=sayi

    def goToProfile(self):
        profil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[5]/a/span')))
        profil.click()
        print("Profile page visited...")

    def deletedPhoto(self):
        print("The image is starting to be deleted, please wait...")
        a=0
        for i in range(self._resimCount):
            try:
                try:
                    if a==0:
                        fotoSec = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]')))
                        fotoSec.click()
                    else:
                        fotoSec = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]')))
                        fotoSec.click()
                except:
                    a=1
                    fotoSec = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]')))
                    fotoSec.click()
                detayButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div[1]/button')))
                detayButton.click()
                resimSil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/button[1]')))
                resimSil.click()
                silOnay = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/button[1]')))
                silOnay.click()
                sleep(5)
                if i%10==0 and i>0:
                    print("%s as many photos have been deleted..." %i)
                    sleep(5)
                if i%50==0 and i>0:
                    print("3 minutes break")
                    sleep(180)
            except:
                print("Error occurred while deleting photo ... Application is closing...")
                self.driver.close()
                sys.exit(1)
        print("\n\n *** The number of pictures you entered has been successfully deleted... ***")



