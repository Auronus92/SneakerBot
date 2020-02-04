from selenium import webdriver
from selenium.webdriver.support.ui import Select
from userInfo import myInfo
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
driver.get(myInfo['productURL'])
timeout = 7



def buyNikeSNKRS():

    driver.find_element_by_xpath('//button[contains(text(), "US 6")]').click()

    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button').click()

    time.sleep(3)

    driver.get('https://www.nike.com/ca/en/cart')

    time.sleep(5)

    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[2]/div[2]/aside/div[6]/div/button[1]').click()

    firstName = EC.presence_of_element_located((By.NAME, 'firstname'))
    WebDriverWait(driver, timeout).until(firstName)

    firstName = driver.find_element_by_name('firstname')
    firstName.send_keys(myInfo['firstName'])

    lastName = driver.find_element_by_name('lastname')
    lastName.send_keys(myInfo['lastName'])

    postCode = driver.find_element_by_name('pcode')
    postCode.send_keys(myInfo['postCode'])

    address1 = driver.find_element_by_name('shippingAddress1')
    address1.send_keys(myInfo['address1'])

    address2 = driver.find_element_by_name('shippingAddress2')
    address2.send_keys(myInfo['address2'])

    city = driver.find_element_by_name('shippingAddress3')
    city.send_keys(myInfo['city'])

    phone = driver.find_element_by_name('shippingPhoneNumber')
    phone.send_keys(myInfo['phone'])

    email = driver.find_element_by_name('shippingEmail')
    email.send_keys(myInfo['email'])

    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/div[2]/div[3]/div/div[1]/label[1]/span').click()

    driver.find_element_by_name('shipSubmit').click()

    time.sleep(5)

    driver.find_element_by_name('billingSubmit').click()

    time.sleep(10)

    # creditName = driver.find_element_by_name('CreditCardHolder')
    # creditName.send_keys(myInfo['firstName'] + myInfo['lastName'])

    credit = driver.find_element_by_xpath('//*[@id="CreditCardHolder"]')
    credit.send_keys(myInfo['cardNumber'])

    # cvv = driver.find_element_by_name('CCCVC')
    # cvv.send_keys(myInfo['cvv'])
    #
    # select = Select(driver.find_element_by_name('KKMonth'))
    # select.select_by_value(myInfo['cardMonth'])
    #
    # select = Select(driver.find_element_by_name('KKYear'))
    # select.select_by_value(myInfo['cardYear'])




#
#
# def buyNike():
#
#
# def buyAdidas():

buyNikeSNKRS()

