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
from selenium.common.exceptions import NoSuchElementException
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
    "https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73515",
    "https://cultureloisirs.gatineau.ca/ic3.Production/#/U5200/view/73597",
    "https://cultureloisirs.gatineau.ca/ic3.production/#/U5200/view/73543"
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
    if now.hour == 17 and now.minute == 30 and now.second == 00:
        driver.find_element_by_css_selector('[alt="Activités Culture et loisirs"]').click()
        driver.find_element_by_xpath('//*[@id="ProgrammeCultureLoisirs"]/div[2]/div[1]/input[2]').click()
        p = driver.current_window_handle

        for w in driver.window_handles:
            if(w!=p):
                driver.switch_to.window(w)
                print("switch tabs successful!")
        while True:
            driver.refresh() 
            time.sleep(1)
            searchbar = driver.find_elements_by_xpath('//*[@id="u2010_btnSearch"]')
            if len(searchbar) > 0:
                break
        court_num = 0
        # TODO: court not available exception handling 
        for court in courts_list:
            court_num += 1
            driver.get(court)
            driver.implicitly_wait(1.5) # seconds
            if len(driver.find_elements_by_xpath("//*[@id='u5200_btnRegisterSecond']")) > 0:
                driver.find_element_by_xpath("//*[@id='u5200_btnRegisterSecond']").click()
                print("Clicked Inscrire button\n")
                driver.find_element_by_xpath("//*[@id='u3600_btnSelect0']").click()
                print("Clicked person\n")
                # Checkout
                driver.find_element_by_xpath("//*[@id='u3600_btnCheckout0']").click()
                print("Clicked checkout button\n")
            else:
                print("Court not available")
                if court_num == len(courts_list):
                    driver.get("https://cultureloisirs.gatineau.ca/IC3.Production/#/U3600/cartshopping")
                    break
                else:
                    continue

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


