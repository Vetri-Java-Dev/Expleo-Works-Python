#GlobalSQA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

wait=WebDriverWait(driver,15)

dropDown=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select")))

select=Select(dropDown)

options=select.options

for option in options:
    print(option.text)

select.select_by_visible_text("India")

selected=select.all_selected_options

for s in selected:
    print(s.text)




