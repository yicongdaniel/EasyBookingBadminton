from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Email = "danielzyc9631@gmail.com"
Password = "Minouandchoue2!"

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://portailcitoyen.gatineau.ca/identite/Account/Login?ReturnUrl=%2Fidentite%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dic3.web%26redirect_uri%3Dhttps%253A%252F%252Fcultureloisirs.gatineau.ca%252Fic3.production%252Fopenidauthcallback%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520email%2520lazer%26state%3D7836e490ce534e37bd1436451800cba7%26nonce%3D2165cc51d19e444f91747bd139c65e94")

driver.find_element_by_name("Email").send_keys(Email)
driver.find_element_by_name("Password").send_keys(Password)
driver.find_element_by_css_selector("input[type=submit]").click()
print("logged in successfully!\n")
time.sleep(3)

driver.get("https://cultureloisirs.gatineau.ca/ic3.production/#/U5200/view/73277")
print("To the court page successfully!\n")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='u5200_btnRegisterSecond']").click()
print("Clicked Inscrire button successfully!\n")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u3600_btnSelect0']").click()
print("Clicked person successfully!\n")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u3600_btnCheckout0']").click()
print("Clicked checkout button click successfully!\n")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u3600_btnCartShoppingCompleteStep']").click()
print("Completed button click successfully!\n")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u3600_chkElectronicPaymentCondition']").click()
print("Checkbox check successfully!\n")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u3600_btnCartPaymentCompleteStep']").click()
print("Confirm button click successfully!\n")
time.sleep(2)



# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Mardi 12:00 - 12:45"))
#     )
#     element.click()
# except:
#     driver.quit()
