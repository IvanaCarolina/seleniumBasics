from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

button = chrome_browser.find_element_by_class_name('btn-default')
print(button)

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Hello Student')

#webdriver.ActionChains(chrome_browser).move_to_element(button).click(button).perform()
chrome_browser.execute_script("arguments[0].click();",button)

output_message = chrome_browser.find_element_by_id('display')
assert 'Hello Student' in output_message.text

#chrome_browser.close()