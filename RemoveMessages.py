
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RemoveMessages:
    def __init__(self,driver,messagesCount):
        self.driver=driver
        self._messagesCount=messagesCount

    def goMessagePage(self):
        mesajbutton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav[1]/div/div/header/div/div[2]')))
        mesajbutton.click()
        sleep(0.5)
        try:
            simdidegil1 = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
            simdidegil1.click()
        except:
            pass
        simdidegil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[5]/button')))
        simdidegil.click()
        sleep(0.5)
        print("Login to message page...")

    def startDeletedMessages(self):
        print("Messages are starting to be deleted...")
        a=1
        for i in range(self._messagesCount):
            try:
                sleep(1)
                mesajatikla = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div['"%s"']' % a)
                mesajatikla.click()
                isim = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/div[1]/header/div/h1/div/div[2]/button/div/div[1]/div')))
                deger=isim.text
                detay = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')))
                detay.click()
                sohbetsil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/div[2]/div/div[3]/div[1]/button')))
                sohbetsil.click()
                sil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/button[1]')))
                sil.click()
                print("{0} your message with the person named has been deleted".format(deger))
                sleep(1)
            except:
                a += 1
                i-=1
                pass
        print("\n\n *** The message as many as the number you entered has been successfully deleted... ***")