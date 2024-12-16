# Отображение страницы товара

'''from selenium import webdriver
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
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
book_html5_forms = driver.find_element_by_css_selector('[alt="Mastering HTML5 Forms"]')
book_html5_forms.click()
name_book = driver.find_element_by_css_selector(".entry-title")
name_book_text = name_book.text
assert name_book_text == "HTML5 Forms"
time.sleep(3)
driver.quit()

# Количество товаров в категории


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
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
category_html = driver.find_element_by_link_text("HTML")
category_html.click()
books_html = driver.find_elements_by_css_selector(".product")
if len(books_html) == 3:
    print("В разделе 3 товара")
else:
    print("Ошибка")
time.sleep(3)
driver.quit()

# Сортировка товаров

from selenium import webdriver
from selenium.webdriver.support.select import Select
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
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
sort_by_default = driver.find_element_by_css_selector('[value="menu_order"]')
sort_by_default_selected = sort_by_default.get_attribute("selected")
if sort_by_default_selected is not None:
    print("Статус выбран")
else:
    print("Статус не выбран")
sort_selector = driver.find_element_by_css_selector(".orderby")
select = Select(sort_selector)
select.select_by_value("price-desc")
time.sleep(3)
sort_by_price = driver.find_element_by_css_selector('[value="price-desc"]')
sort_by_price_selected = sort_by_price.get_attribute("selected")
if sort_by_price_selected is not None:
    print("Статус выбран")
else:
    print("Статус не выбран")
driver.quit()

# Отображение, скидка товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
android_quick_start_book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
android_quick_start_book.click()
old_price = driver.find_element_by_css_selector(".price>del>span")
old_price_text = old_price.text
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price>ins>span")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
book_cover = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".zoom")))
book_cover.click()
book_cover_close = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()
driver.quit()

# Проверка цены в корзине

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
html5_webapp_book_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_webapp_book_basket.click()
time.sleep(3)
#item_in_basket = driver.find_element_by_css_selector("a>.cartcontents")
#item_in_basket_text = item_in_basket.text
#price_book_in_basket = driver.find_element_by_css_selector("a>.amount")
#price_book_in_basket_text = price_book_in_basket.text
#assert item_in_basket_text == "1 item"
#assert price_book_in_basket_text == "₹180.00"
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket.click()
subtotal = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00"))
total = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong .amount"), "₹183.60"))
driver.quit()

# Работа в корзине

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_book_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_webapp_book_basket.click()
time.sleep(3)
js_data_book_basket = driver.find_element_by_css_selector('[data-product_id="180"]')
js_data_book_basket.click()
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket.click()
time.sleep(3)
book_remove = driver.find_element_by_css_selector("tbody>.cart_item:nth-child(1)  .remove")
book_remove.click()
time.sleep(3)
undo_book_remove = driver.find_element_by_css_selector(".woocommerce-message>a")
undo_book_remove.click()
quantity = driver.find_element_by_css_selector("tbody>.cart_item:nth-child(1) .input-text")
quantity.clear()
quantity.send_keys("3")
update_basket_btn = driver.find_element_by_name("update_cart")
update_basket_btn.click()
quantity = driver.find_element_by_css_selector("tbody>.cart_item:nth-child(1) .input-text")
quantity_check = quantity.get_attribute("value")
assert quantity_check == "3"
time.sleep(3)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()
error_message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
driver.quit()



# Покупка товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop_btn = driver.find_element_by_link_text("Shop")
shop_btn.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_book_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_webapp_book_basket.click()
time.sleep(3)
basket = driver.find_element_by_css_selector(".wpmenucart-contents")
basket.click()
proceed_to_checkout_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
proceed_to_checkout_btn.click()
first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Anna")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Ozerova")
email = driver.find_element_by_id("billing_email")
email.send_keys("Anna_Ozerova@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89009228154")
time.sleep(3)
country_selector = driver.find_element_by_id("s2id_billing_country")
country_selector.click()
search = driver.find_element_by_id("s2id_autogen1_search")
search.send_keys("Russia")
select_country = driver.find_element_by_id("select2-results-1")
select_country.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Ivanova street 15")
city = driver.find_element_by_id("billing_city")
city.send_keys("Saint Petersburg")
state = driver.find_element_by_id("billing_state")
state.send_keys("Saint Petersburg")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("195861")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))
driver.quit() '''

