from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url1 = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
driver1 = webdriver.Chrome()



def opensite(url,driver):
    driver.get(url)
    time.sleep(2)


def login(url,driver):
    opensite(url,driver)
    time.sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
    time.sleep(2)
    login.click()
    time.sleep(2)
    names = driver.find_element(By.CSS_SELECTOR, '#userSelect')
    names.click()
    # time.sleep(2)
    names.send_keys(Keys.ARROW_DOWN)
    names.send_keys(Keys.ENTER)
    # time.sleep(2)
    login_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')
    login_button.click()
    time.sleep(2)


def find_element(driver,selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def deposit1(amount,driver):
    money_before_deposit= (find_element(driver,'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')).text
    deposit= find_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    deposit.click()
    time.sleep(2)
    deposit_amount= find_element(driver,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    deposit_amount.send_keys(amount)
    deposit_button= find_element(driver,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
    deposit_button.click()
    time.sleep(2)
    money_after_deposit= (find_element(driver,'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)')).text
    print(money_after_deposit)
    return int(money_after_deposit)


def withraw(amount, driver):
    withraw = find_element(driver,'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)')
    withraw.click()
    time.sleep(3)
    amount_button = find_element(driver,'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    time.sleep(3)
    amount_button.click()

    amount_button.send_keys(amount)
    time.sleep(3)
    amount_button.send_keys(Keys.ENTER)
    amount_after_withraw = int(find_element(driver,'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)').text)
    print(amount_after_withraw)
    return amount_after_withraw


def deposit_plus_withraw(depositAmount, withrawAmount, driver):
    deposit1(depositAmount, driver)
    return withraw(withrawAmount ,driver)


def not_text(text, driver):
    DepositB = find_element(driver, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
    DepositB.click()
    time.sleep(2)
    DepositL = find_element(driver, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
    DepositL.click()
    DepositL.send_keys(text)
    return DepositL.text


def login_as_manger(url,driver):
    opensite(url,driver)
    mangerL = find_element(driver, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    mangerL.click()
    time.sleep(2)


def add_customer(driver, first_name, last_name, post_code):
    manger_area = find_element(driver, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    manger_area.click()
    time.sleep(2)
    new_customer = find_element(driver, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
    new_customer.click()
    time.sleep(2)
    First_Name = find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input')
    First_Name.send_keys(first_name)
    Last_Name = find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
    Last_Name.send_keys(last_name)
    time.sleep(2)
    postal_code = find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
    postal_code.send_keys(post_code)
    time.sleep(2)
    postal_code.send_keys(Keys.ENTER)
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    time.sleep(2)



def if_customer_exist(first_name, last_name, post_code, driver):
    time.sleep(1)
    customers_list = driver.find_element(By.CSS_SELECTOR,'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
    time.sleep(1)
    customers_list.click()
    time.sleep(1)
    search_customer = find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > form > div > div > input')
    search_customer.send_keys(first_name)
    time.sleep(1)
    first_name_found = find_element(driver,'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr > td:nth-child(1)').text
    last_name_found = find_element(driver,'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr > td:nth-child(2)').text
    post_code_found = int(find_element(driver, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr > td:nth-child(3)').text)
    if first_name_found == first_name and last_name_found == last_name and post_code_found == post_code:
        return True
    else:
        return False





















