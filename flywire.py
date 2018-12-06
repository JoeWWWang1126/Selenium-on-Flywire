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

def openDisplay(): #This is base on an linux server, so I need to get an virtual display.
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display

def openChrome(): #Open chromedriver and simply set up.
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless') #In my version, headless sometimes are not available.
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
def operationAuth():
    url="https://flywire.com/zh/pay/uc"
    driver.get(url)
    #----------------------------------------------
    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "sender_country"))

        )
    finally:
            pass
    
    country=driver.find_element_by_name("sender_country")
    
    """------This part is used to check the factor in the page.--------------------------------
    Use the try-finally will meet some errors that will end my program, so later I used if to replace
    it. It might seems stupid.
    """
    country.send_keys('China')
    country.send_keys(Keys.ENTER)
    driver.get_screenshot_as_file("country.png")#Get screenshot is used for test.
    amount=driver.find_element_by_id("amount")
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)
    amount.send_keys(Keys.BACK_SPACE)# This is used to clear the box. This method should be changed.
    amount.send_keys(Keys.NUMPAD4)
    amount.send_keys(Keys.NUMPAD3)
    amount.send_keys(Keys.NUMPAD0)
    amount.send_keys(Keys.NUMPAD0)#Use the text can have a same result. This method should bechanged.
    driver.get_screenshot_as_file("amount.png")#Get screenshot is used for test.
    driver.find_element_by_class_name('Navigation-slide--next').click()
    time.sleep(15)
    driver.find_element_by_class_name('Navigation-slide--error').click()#click error button is used when the next button is useless
    time.sleep(15)
    driver.get_screenshot_as_file("screen.png")
    time.sleep(15)
    driver.find_element_by_xpath('//a[@data-qa="continueAsGuest"]').click()
    time.sleep(15)
    final=driver.find_element_by_xpath('//*[@id="app-root"]/div/main/div/section/div[2]/div/div[2]/ul/li[1]/div[1]/div[1]/div/h4')
    #-------Below part is to wirte the data to MY OWN SQL
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="xxx",database="xxx")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM xxx")
    first = mycursor.fetchone()

    mycursor.execute("update xxx set record = '"+final.text+"' where record= '"+first[0]+"'")
    mydb.commit()
    mycursor.execute("select * from xxx")
    last=mycursor.fetchone()
    print(last[0])
    mydb.close()
    driver.quit()
    display.stop()
    return last[0]
if __name__ == '__main__':
    # This while loop is for the condition: Programe will never remind you that sth was wrong.
    #However, I still met this condition..I thought that is because of Lack of Space In Ram.
    while True:
        display = openDisplay()
        driver = openChrome()
        try:
            operationAuth()
        except:
            driver.quit()
        finally:
            pass


