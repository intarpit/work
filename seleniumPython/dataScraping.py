"""
The below program gets data from excel sheet and the look up for the data on a website and then scraps that data
and then insert it on a excel sheet.
! ? Currently work in progress.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl as op
import time

drive = "" #! Please enter drive path.
fileName = "" #! Please enter file name.
path = drive + fileName

r = 3 #! Please change the row number to the row number from which you would like to start reading the file.
nameList = list()
def institutionsNames():
    """
    This function load all the data from a excel sheet for a particular column and stores it in a list named "nameList".
    """
    itn = op.load_workbook(path)
    itnSh = itn.get_sheet_by_name("Sheet1")
    maxRow = itnSh.max_row
    for s in range(r, (maxRow + 10)):
        name = itnSh.cell(row = s, column = 3).value #! Please change the column number based on the column number in your file.
        if name != None:
            name = name.strip()
            nameList.append(name)
    itn.close()
    return nameList

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("disable-popup-blocking")
chromeOptions.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("https://www.edufever.com/")

for i in nameList:
    seachSign = driver.find_element_by_xpath("//*[@id='menu-mymenu-1']/li[9]/a")
    seachSign.click()

    searchBar = driver.find_element_by_id("q")
    searchBar.send_keys(i)


time.sleep(500)
