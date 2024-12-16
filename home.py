# Добавление комментария

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
book_selenium_ruby = driver.find_element_by_css_selector('[alt="Selenium Ruby"]')
book_selenium_ruby.click()
reviews = driver.find_element_by_css_selector(".reviews_tab>a")
reviews.click()
rating_5_star = driver.find_element_by_css_selector(".star-5")
rating_5_star.click()
your_review = driver.find_element_by_id("comment")
your_review.send_keys("Nice book!")
first_name = driver.find_element_by_id("author")
first_name.send_keys("Anna")
email = driver.find_element_by_id("email")
email.send_keys("Anna_Ozerova@gmail.com")
time.sleep(3)
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
time.sleep(3)
driver.quit()

