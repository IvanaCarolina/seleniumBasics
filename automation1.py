from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.google.com.br/')

button = chrome_browser.find_element_by_class_name('gNO89b')
print(button)

user_message = chrome_browser.find_element_by_name('q')
user_message.clear()
user_message.send_keys('naruto shippuden online')

#webdriver.ActionChains(chrome_browser).move_to_element(button).click(button).perform()
chrome_browser.execute_script("arguments[0].click();",button)