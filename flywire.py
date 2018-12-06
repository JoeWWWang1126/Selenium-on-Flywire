from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import  mysql.connector
import json
import datetime
def openDisplay():
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display
def openChrome():
    # 鍔犲惎鍔ㄩ厤缃�
    #display = Display(visible=0, size=(800, 800))
    #display.start()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
def operationAuth():
    url="https://flywire.com/zh/pay/uc"
    driver.get(url)
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "sender_country"))

        )
    finally:
            pass
    country=driver.find_element_by_name("sender_country")
    country.send_keys('China')
   
    country.send_keys(Keys.ENTER)
    driver.get_screenshot_as_file("country.png")
    amount=driver.find_element_by_id("amount")
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    #amount.send_keys('4300')
    # driver.implicitly_wait(2)
    #amount.send_keys(Keys.ENTER)
    #driver.find_element_by_class_name('Navigation-slide--next').click()
    #driver.find_element_by_class_name('ErrorCounter').click()
    amount.send_keys(Keys.NUMPAD4)

    amount.send_keys(Keys.NUMPAD3)

    amount.send_keys(Keys.NUMPAD0)

    amount.send_keys(Keys.NUMPAD0)
    driver.get_screenshot_as_file("amount.png")
    # amount.send_keys(Keys.TAB)
    # print(amount.is_selected())
    #driver.find_element_by_xpath('//*[@id="app-root"]/div/main/div/section/div[3]/nav/button/div/span[1]').click()
    driver.find_element_by_class_name('Navigation-slide--next').click()
    time.sleep(15)
    driver.find_element_by_class_name('Navigation-slide--error').click()
    #driver.find_element_by_xpath('//*[@id="app-root"]/div/main/div/section/div[3]/nav/button/div/span[2]').click()
    time.sleep(15)
    driver.get_screenshot_as_file("screen.png")
    time.sleep(15)
    driver.find_element_by_xpath('//a[@data-qa="continueAsGuest"]').click()


    time.sleep(15)
    final=driver.find_element_by_xpath('//*[@id="app-root"]/div/main/div/section/div[2]/div/div[2]/ul/li[1]/div[1]/div[1]/div/h4')
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="autof460",database="pachong")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM jilu")
    first = mycursor.fetchone()

    mycursor.execute("update jilu set record = '"+final.text+"' where record= '"+first[0]+"'")
    mydb.commit()
    mycursor.execute("select * from jilu")
    last=mycursor.fetchone()
    print(last[0])
    mydb.close()
    
    #print(final.text)
    driver.quit()
    
    display.stop()
    return last[0]
if __name__ == '__main__':
    #display = openDisplay()
    #driver = openChrome()
    while True:
        display = openDisplay()
        driver = openChrome()

        try:
            operationAuth()
        except:
            driver.quit()
        finally:
            pass
        #time.sleep(10)

        #driver.quit()
    #driver.quit()

