from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_eight_components():

    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.maximize_window()
    driver.get("https://www.google.com.br/")
    
    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="q")
    text_box.send_keys("Vita IT")

    submit_button = driver.find_element(by=By.CLASS_NAME, value="gNO89b")
    submit_button.click()

    return driver

test_eight_components()
