
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Please enter your Email and password in the variables: For example Email = "danielyicong@gmail.com"  Password = "123456789" 
Email = "danielzyc9631@gmail.com"
Password = "Minouandchoue2!"        
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# Go to web page
driver.get("https://portailcitoyen.gatineau.ca/identite/Account/Login?ReturnUrl=%2Fidentite%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dic3.web%26redirect_uri%3Dhttps%253A%252F%252Fcultureloisirs.gatineau.ca%252Fic3.production%252Fopenidauthcallback%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520email%2520lazer%26state%3D7836e490ce534e37bd1436451800cba7%26nonce%3D2165cc51d19e444f91747bd139c65e94")
driver.find_element_by_name("Email").send_keys(Email)
driver.find_element_by_name("Password").send_keys(Password)
driver.find_element_by_css_selector("input[type=submit]").click()
print("logged in successfully!\n")
time.sleep(3)

# Go to court 1
driver.implicitly_wait(10) # seconds
driver.get("https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73289")
print("To the court 1 page\n")
myDynamicElement = driver.find_element_by_xpath("//*[@id='u5200_btnRegisterSecond']")
myDynamicElement.click()
print("Clicked Inscrire button\n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnSelect0']")
myDynamicElement.click()
print("Clicked person\n")

# Go to court 2
driver.implicitly_wait(10) # seconds
Phase
driver.get("https://cultureloisirs.gatineau.ca/IC3.Production/#/U5200/view/73295")
print("To the court 1 page\n")
myDynamicElement = driver.find_element_by_xpath("//*[@id='u5200_btnRegisterSecond']")
myDynamicElement.click()
print("Clicked Inscrire button\n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnSelect0']")
myDynamicElement.click()
print("Clicked person\n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnCheckout0']")
myDynamicElement.click()
print("Clicked checkout button\n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnCartShoppingCompleteStep']")
myDynamicElement.click()
print("Clicked Basket section completed button\n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_chkElectronicPaymentCondition']")
myDynamicElement.click()
print("Checked terms and conditions \n")

driver.implicitly_wait(10) # seconds
myDynamicElement = driver.find_element_by_xpath("//*[@id='u3600_btnCartPaymentCancel']")
myDynamicElement.click()
print("Clicked Cancel button \n")

# # driver.find_element_by_xpath("//*[@id='u3600_btnCartPaymentCompleteStep']").click()
# # print("Clicked Confirm button\n")


