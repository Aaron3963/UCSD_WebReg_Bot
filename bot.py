from ast import While
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions

import openpyxl
bk=openpyxl.load_workbook('config.xlsx')
sheet=bk.active

maxRow=sheet.max_row
maxCol=sheet.max_column

USERNAME = sheet.cell(1,2).value
PASSWORD = sheet.cell(2,2).value

dict={}
for i in range(3,maxRow+1):
    list = []
    for j in range(2,maxCol+1):
        cell = str(sheet.cell(i,j).value)
        if len(cell) < 6:
            for numZero in range (0,6-len(cell)):
                cell = '0'+cell
        list.append(cell)
    dict[sheet.cell(i,1).value] = list
print(dict)


wd = webdriver.Chrome(service= Service(r'./chromedriver.exe'))
wd.implicitly_wait(10)

wd.get('https://act.ucsd.edu/webreg2')

username = wd.find_element(By.ID,'ssousername')
username.send_keys(USERNAME)
password = wd.find_element(By.ID,'ssopassword')
password.send_keys(PASSWORD)

wd.find_element(By.XPATH,'//*[@id="login"]/button').click()

sleep(15)

#Go page
termSelect = Select(wd.find_element(By.ID,'startpage-select-term'))
termSelect.select_by_visible_text('Fall Quarter 2022')

wd.find_element(By.ID,'startpage-button-go').click()


def search(wd,course,id):
    searchBar = wd.find_element(By.ID, 's2id_autogen1')
    searchBar.clear()
    searchBar.send_keys(course)
    
    #Confirm Selection
    wd.find_element(By.ID, 'select2-drop-mask').click()

    #Search Class
    wd.find_element(By.ID, 'search-div-t-b1').click()

    #Expand Section List
    wd.find_element(By.XPATH, '//*[@id="search-div-b-tableghead_0_0"]/td/span').click()
    
    sectionEnrollID = 'search-enroll-id-'+str(id)
    sectionWaitID = 'search-wait-id-'+str(id)

    wd.implicitly_wait(0.05)
    try:
        #targetClass = wd.find_element(By.ID,sectionEnrollID)
        targetClass = wd.find_element(By.ID,sectionEnrollID)
    except Exception:
        targetClass = wd.find_element(By.ID,sectionWaitID)

    wd.implicitly_wait(10)

    if course not in targetClass.get_attribute('class'):
        print("Class Mismatch. Abort.")

    if 'Waitlist' == targetClass.get_attribute('value'):
        print(course+sectionID+": No Space, retrying...")
        return False

    if 'Enroll' == targetClass.get_attribute('value'):
        #wd.find_element(By.ID)
        return True


enrolled = False
while True:
    for course in dict.keys():
        for sectionID in dict[course]:
            enrolled = search(wd,course,sectionID)
            if enrolled:
                break
        if enrolled:
            break
    if enrolled:
        break

