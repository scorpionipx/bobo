from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

driver = webdriver.Chrome(r"C:\Users\ScorpionIPX\AppData\Local\Temp\Rar$EXa23412.47142\chromedriver.exe")
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")

sleep(10)

ac = ActionChains(driver)
ac.move_by_offset(500, 500).click().perform()

input()
driver.close()

