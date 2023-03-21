from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestInternetSpeed:
    def tis(self):
        try:
            driver = webdriver.Chrome()
            driver.get("https://www.speedtest.net/")
            btn_go = driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            btn_go.click()
            time.sleep(60)
            txt_transactionNumber = driver.find_element(by=By.XPATH,
                                                        value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')
            txt_DS = driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            txt_US = driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            print(txt_transactionNumber.text)
            print(txt_US.text)
            print(txt_DS.text)
            return txt_US.text, txt_DS.text, txt_transactionNumber.text
        except Exception as e:
            print(e)
        finally:
            driver.close()

