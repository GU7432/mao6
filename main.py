import time, random
import tkinter as tk
import threading
from randommessage import getmes
from controlchrome import send, init

lo = 1
hi = 3
isrunning = False
def Sending():
    global isrunning
    pre = ""
    while isrunning:
        text = getmes()
        while text == pre: text = getmes()
        pre = text
        send(pre)
        wait = random.uniform(lo, hi)
        print(wait)
        time.sleep(wait)

def startSending():
    global isrunning
    if isrunning: return
    isrunning = True
    threading.Thread(target=Sending, daemon=True).start()

def stopSending():
    global isrunning
    isrunning = False

def openurl():
    url = urlEntry.get()
    print(url)
    if url: init(url)

def settiming():
    global lo, hi
    lo = int(loEntry.get())
    hi = int(hiEntry.get())

# 創建主窗口
root = tk.Tk()
root.geometry("800x600")
root.title("Twitch 刷貓機器人")

# 設置界面元素
start_btn = tk.Button(root, text="開始發送訊息", command=startSending, width=15, height=2)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="停止發送訊息", command=stopSending, width=15, height=2)
stop_btn.pack(pady=10)

# 輸入框（Entry）開啟網址按鈕
urlEntry = tk.Entry(root, width=40)
urlEntry.pack(pady=10)

openurl_btn = tk.Button(root, text="打開網址", command=openurl)
openurl_btn.pack(pady=10)

# 設定刷貓間隔
setlabel = tk.Label(root, text="設定刷貓間隔", font=("Arial", 16))
setlabel.pack(pady=10)

loEntry = tk.Entry(root, width=5)
loEntry.pack(pady=10)

hiEntry = tk.Entry(root, width=5)
hiEntry.pack(pady=10)

settime_btn = tk.Button(root, text="設定", command=settiming)
settime_btn.pack(pady=10)

# 倒數計時
# timer_label = tk.Label(root, text="等待開始...", font=("Arial", 16))
# timer_label.pack(pady=20)

root.mainloop()