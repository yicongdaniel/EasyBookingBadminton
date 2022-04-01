"""
----------------------------------------------------------------------------------------------------
Project: Booking Automation
Version: 1.0
Authors: Daniel Zhang, Sam Liu
Description: This script books badminton courts automaticlly on cultureloisirs.gatineau website.
----------------------------------------------------------------------------------------------------
"""
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
'''
TODO: Important!!! Please read the following instruction
Please enter your Email and password in the variables: 
For example 
Email = "danielyicong@gmail.com"  
Password = "123456789" 
Booking courts part
Phase the court's URL below. For example:
If you want to book only one court, do it like this:
courts_list = ["https://cultureloisirs.gatineau.ca/ic3.production/#/U5200/view/73376"]
If you want two courts do it like this
courts_list = ["https://cultureloisirs.gatineau.ca/ic3.production/#/U5200/view/73376", 
            "https://cultureloisirs.gatineau.ca/ic3.production/#/U5200/view/73292"]

CSG:
Tuesday 730
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73526
Tuesday 845
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73527
Thursay 730
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73541
Thursday 845
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73542
Sunday 19:30
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73507

Versant
Wednesday 730
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73566
Wednesday 855
https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73567

Hint: only need to change the last 5 digits
'''

courts_list = [
    "https://cultureloisirs.gatineau.ca/ic3.Production/#/U5200/view/73384",
    "https://cultureloisirs.gatineau.ca/ic3.Production/#/U5200/view/73581"
]

EMAIL = "XYZ@example.com"
PASSWORD = "1234"        
PATH = "D:\chromedriver.exe"
URL = "https://portailcitoyen.gatineau.ca/"
driver = webdriver.Chrome(PATH)
# driver.maximize_window()

# Log in part
driver.get(URL)
username = driver.find_element_by_name("Email")
username.send_keys(EMAIL)
password = driver.find_element_by_name("Password")
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

while True:
    now = datetime.datetime.now().time()
    if now.hour == 12 and now.minute == 57 and now.second == 10:
        driver.find_element_by_css_selector('[alt="Activités Culture et loisirs"]').click()
        driver.find_element_by_xpath('//*[@id="ProgrammeCultureLoisirs"]/div[2]/div[1]/input[2]').click()
        p = driver.current_window_handle

        for w in driver.window_handles:
            if(w!=p):
                driver.switch_to.window(w)
                print("switch tabs successful!")
                time.sleep(1)
        while True:
            driver.refresh() 
            time.sleep(1)
            searchbar = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, 'u2010_edSearch')))
            if searchbar:
                break
        court_num = 1
        for court in courts_list:
            driver.get(court)
            driver.implicitly_wait(10) # seconds
            myDynamicElement = driver.find_element_by_xpath("//*[@id='u5200_btnRegisterSecond']")
            myDynamicElement.click()
            print("Clicked Inscrire button\n")
            
            myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnSelect0']")
            myDynamicElement.click()
            print("Clicked person\n")
            print ("Court", court_num, "selected")
            court_num += 1

        # Checkout part
        # driver.implicitly_wait(10) # seconds
        myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnCheckout0']")
        myDynamicElement.click()
        print("Clicked checkout button\n")

        time.sleep(2)
        button = driver.find_element_by_xpath("//*[@id='u3600_btnCartShoppingCompleteStep']")
        driver.execute_script("arguments[0].click();", button) 
        print("Clicked Basket section completed button\n")

        myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_chkElectronicPaymentCondition']")
        myDynamicElement.click()
        print("Checked terms and conditions \n")

        myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnCartPaymentCompleteStep']")
        myDynamicElement.click()
        print("Clicked Confirm button \n")
        driver.quit()


