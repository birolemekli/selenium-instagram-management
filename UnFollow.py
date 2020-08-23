# coding=utf-8
from time import sleep
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UnFollow:
    def __init__(self,driver,count):
        self.driver=driver
        self._count=count

    def goToProfile(self):
        profil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[5]/a/span')))
        profil.click()
        print("Profile page visited...")

    def goToFollowerList(self):
        takipList = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[3]')))
        takipList.click()
        print("The following page was visited...")

    def unfollow(self):
        b = 1
        for a in range(1,self._count):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/ul/div/li[1]/div/div[2]/button')))
                takiptencikButton=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/div/li['"%s"']/div/div[2]/button' % a)
                takiptencikButton.click()
                takipCikOnay = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]')))
                takipCikOnay.click()
                sleep(5)
                print(a)
                if a>0 and a%9==0:
                    kaydir=480*b
                    self.driver.execute_script("window.scrollTo(0, %s)"%kaydir)
                    print("1 minute break")
                    sleep(60)
                    b+=1
            except:
                print("A problem occurred while unfollowing... Application is closing...")
                self.driver.close()
                sys.exit(2)
