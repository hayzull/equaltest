from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v4.html')

oneElem = browser.find_element_by_name('one')
oneElem.click()

addElem =  browser.find_element_by_name('plus')
addElem.click()

oneElem = browser.find_element_by_name('one')
oneElem.click()

equalElem = browser.find_element_by_name('DoIt')
equalElem.click()

inputElem = browser.find_element_by_name('Input') 

valueInputElem = inputElem.get_attribute('value')

print ('What is this  ' + valueInputElem)