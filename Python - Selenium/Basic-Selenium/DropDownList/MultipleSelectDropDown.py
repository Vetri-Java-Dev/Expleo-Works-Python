#GlobalSQA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def viewSelectedOptions():
    for selected in select.all_selected_options:
        print(selected.text)

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/select-menu")

wait=WebDriverWait(driver,15)

dropDown=wait.until(EC.visibility_of_element_located((By.ID,"cars")))

select=Select(dropDown)

if(select.is_multiple):
    print("Multiple select possible")
else:
    print("Multiple not select possible")
    
options=select.options

for option in options:
    print(option.text)


select.select_by_visible_text("Opel")
select.select_by_visible_text("Saab")

print("Selected options : ")
viewSelectedOptions()

print("After deselection, options : ")
select.deselect_by_index(1)
viewSelectedOptions()



