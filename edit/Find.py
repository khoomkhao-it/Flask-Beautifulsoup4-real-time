from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import app #file Python

Url = ''
Name = []
Tag = []
Attri = []
Value = []
Chart = []
#selenium
options = Options()
options.headless = True
def Getdata():
    driver = webdriver.Firefox(options=options,executable_path=r'showweb\สหกิจ2\edit\D-selenium\geckodriver.exe')
    driver.get(Url)
    # Give the javascript time to render
    time.sleep(1)
    #beautifulsoup
    soup = BeautifulSoup(driver.page_source, "lxml")
    data = []
    for i in Tag:
        data.append(i)
    #-------------------------------------------------------------------------------
    count = 0
    for i in Tag:
        data[count] = soup.find(Tag[count] ,{Attri[count]:Value[count]})
        #If Else สำหรับเช็คค่าที่ได้รับมาเป็น None หรือไม่
        if data[count] is not None:
            data[count] = data[count].text
        else:
            data[count] = "null"
        #ตัดหน่วยเงินออกสำหรับแสดงค่า
        count = count+1
    driver.close()
    return(data)
#-------------------------------------------------------------------------------------------------------------------------------------------------
    '''
        data[count] = data[count].replace("$", "")
        data[count] = data[count].replace("¢", "")
        data[count] = data[count].replace("€", "")
        data[count] = data[count].replace("£", "")
        data[count] = data[count].replace("¥", "")
        data[count] = data[count].replace("₩", "")
        data[count] = data[count].replace("₿", "")
        data[count] = data[count].replace("₽", "")
        data[count] = data[count].replace("₹", "")
        data[count] = data[count].replace("¤", "")
        data[count] = data[count].replace("₱", "")
        data[count] = data[count].replace("₦", "")
        data[count] = data[count].replace("ƒ", "")
        data[count] = data[count].replace("₮", "")
        data[count] = data[count].replace("৲", "")
        data[count] = data[count].replace("₨", "")
        data[count] = data[count].replace("௹", "")
        data[count] = data[count].replace("฿", "")
        data[count] = data[count].replace("៛", "")
        data[count] = data[count].replace("₪", "")
        data[count] = data[count].replace("₫", "")
        data[count] = data[count].replace("₭", "")
        data[count] = data[count].replace("₲", "")
        data[count] = data[count].replace("₴", "")
        data[count] = data[count].replace("₵", "")
        data[count] = data[count].replace("≋", "")
        data[count] = data[count].replace("﷼", "")
    '''