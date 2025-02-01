from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import random
from getmessage import getmes
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222" 

driver = webdriver.Chrome(options=options)
url = "https://www.twitch.tv/roger9527"
driver.get(url)


def send(sss: str):
    # 找到傳送訊息框
    messageBox = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"WYSIWGChatInputEditor_SkipChat\"]/div/div[2]"))
    )
    messageBox.send_keys(sss)
    time.sleep(1) # 沒有停一下會傳送不出去
    # 找到傳送訊息按鍵
    sendButton = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"live-page-chat\"]/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[2]/div[2]/div[3]/div/button"))
    )
    sendButton.click()

pre = ""
while 1:
    # driver.minimize_window()
    text = getmes()
    while text == pre: text = getmes()
    pre = text
    send(pre)
    wait = random.uniform(10, 35)
    print(wait)
    time.sleep(wait)








