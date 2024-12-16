# Регистрация аккаунта

'''from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
time.sleep(3)
register_email = driver.find_element_by_id("reg_email")
register_email.send_keys("Anna_Ozerova@gmail.com")
register_password = driver.find_element_by_id("reg_password")
register_password.send_keys("Anna_0zerova")
time.sleep(3)
register_btn = driver.find_element_by_css_selector('[name="register"]')
register_btn.click()
time.sleep(3)
driver.quit()'''

# Логин в систему

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
time.sleep(3)
login_email = driver.find_element_by_id("username")
login_email.send_keys("Anna_Ozerova@gmail.com")
login_password = driver.find_element_by_id("password")
login_password.send_keys("Anna_0zerova")
time.sleep(3)
login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()
logout = driver.find_element_by_link_text("Logout")
logout_get_text = logout.text
if logout_get_text == "Logout":
    print("Элемент есть")
else:
    print("Элемент отсутствует")
time.sleep(3)
driver.quit()