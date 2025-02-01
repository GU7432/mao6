import time, random
import tkinter as tk
import threading
from randommessage import getmes
from controlchrome import send

isrunning = False
def Sending():
    global isrunning
    pre = ""
    while isrunning:
        text = getmes()
        while text == pre: text = getmes()
        pre = text
        send(pre)
        wait = random.uniform(1, 3)
        time.sleep(wait)

def startSending():
    global isrunning
    if isrunning: return
    isrunning = True
    threading.Thread(target=Sending, daemon=True).start()

def stopSending():
    global isrunning
    isrunning = False


# 創建主窗口
root = tk.Tk()
root.geometry("800x600")
root.title("Twitch 刷貓機器人")

# 設置界面元素
start_btn = tk.Button(root, text="開始發送訊息", command=startSending, width=15, height=2)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="停止發送訊息", command=stopSending, width=15, height=2)
stop_btn.pack(pady=10)

# # 倒數計時
# timer_label = tk.Label(root, text="等待開始...", font=("Arial", 16))
# timer_label.pack(pady=20)

root.mainloop()