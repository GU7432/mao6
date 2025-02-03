import time, random
import tkinter as tk
import threading
from randommessage import getmes
from controlchrome import send, init

lo = 1 # 最小间隔时间
hi = 3 # 最大间隔时间
isrunning = False # 是否正在发送讯息
send_count = 0  # 已发送讯息次数
stop_program = False  # 是否退出程序
countdown_running = False  # 倒计时是否运行中
total_seconds = 0  # 全局变量，存储总秒数

def seconds_to_hms(seconds):
    # 将秒数转换为'小时:分钟:秒'的格式
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def Sending():
    global isrunning, send_count
    pre = ""
    while isrunning and not stop_program:
        text = getmes()
        while text == pre:
            text = getmes()
        pre = text
        send(pre)
        send_count += 1
        wait = random.uniform(lo, hi)
        start_time = time.time()
        while isrunning and (time.time() - start_time) < wait:
            remaining = wait - (time.time() - start_time)
            next_send_remaining.config(text=f"下次发送剩余时间: {remaining:.1f}秒")
            time.sleep(0.1)
        next_send_remaining.config(text="下次发送剩余时间: 0.0秒")

def startSending():
    global isrunning
    isrunning = True
    threading.Thread(target=Sending, daemon=True).start()

def stopSending():
    global isrunning
    isrunning = False

def openurl():
    url = urlEntry.get()
    print(url)
    if url:
        init(url)

def settiming():
    global lo, hi
    try:
        lo = int(loEntry.get())
        hi = int(hiEntry.get())
    except ValueError:
        print("请输入有效的数字！")

def startCountdown():
    global stop_program, countdown_running, total_seconds
    try:
        hours = int(countdownHoursEntry.get())
        minutes = int(countdownMinutesEntry.get())
        seconds = int(countdownSecondsEntry.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds
    except ValueError:
        print("请输入有效的数字！")
        return
    if total_seconds <= 0:
        print("请输入有效的时间！")
        return
    countdown_remaining.config(text=f"倒计时: {seconds_to_hms(total_seconds)}")
    countdown_running = True

    def countdown_thread():
        global stop_program, countdown_running, total_seconds
        while total_seconds > 0 and countdown_running:
            countdown_remaining.config(text=f"倒计时: {seconds_to_hms(total_seconds)}")
            time.sleep(1)
            total_seconds -= 1
        countdown_remaining.config(text="倒计时: 结束")
        stop_program = True
        isrunning = False
        countdown_running = False
        root.after(1000, root.quit)

    threading.Thread(target=countdown_thread, daemon=True).start()

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
urlFrame = tk.Frame(root)
urlFrame.pack(pady=10)
tk.Label(urlFrame, text="Twitch 頻道網址:").pack(side=tk.LEFT)
urlEntry = tk.Entry(urlFrame, width=40)
urlEntry.pack(side=tk.LEFT, padx=5)

openurl_btn = tk.Button(urlFrame, text="打開網址", command=openurl)
openurl_btn.pack(side=tk.LEFT)

# 設定刷貓間隔
setFrame = tk.Frame(root)
setFrame.pack(pady=10)
tk.Label(setFrame, text="設定刷貓間隔 (秒):").pack(side=tk.LEFT)
loEntry = tk.Entry(setFrame, width=5)
loEntry.pack(side=tk.LEFT, padx=5)
hiEntry = tk.Entry(setFrame, width=5)
hiEntry.pack(side=tk.LEFT, padx=5)
settime_btn = tk.Button(setFrame, text="設定", command=settiming)
settime_btn.pack(side=tk.LEFT, padx=5)


# 設定倒計時
countdownSetFrame = tk.Frame(root)
countdownSetFrame.pack(pady=10)
tk.Label(countdownSetFrame, text="設定倒計時 (小时:分钟:秒):").pack(side=tk.LEFT)
countdownHoursEntry = tk.Entry(countdownSetFrame, width=5)
countdownHoursEntry.pack(side=tk.LEFT, padx=5)
countdownMinutesEntry = tk.Entry(countdownSetFrame, width=5)
countdownMinutesEntry.pack(side=tk.LEFT, padx=5)
countdownSecondsEntry = tk.Entry(countdownSetFrame, width=5)
countdownSecondsEntry.pack(side=tk.LEFT, padx=5)

# 开始倒计时按钮
start_countdown_btn = tk.Button(countdownSetFrame, text="開始倒計時", command=startCountdown)
start_countdown_btn.pack(side=tk.LEFT, padx=5)

# 剩余时间显示（下次发送剩余时间）
next_send_remaining = tk.Label(root, text="下次发送剩余时间: 0.0秒", font=("Arial", 12))
next_send_remaining.pack(pady=10)

# 倒计时显示
countdown_remaining = tk.Label(root, text="倒计时: 0:00:00", font=("Arial", 12))
countdown_remaining.pack(pady=10)

# 已发送次数显示
send_count_display = tk.Label(root, text="已发送次数: 0次", font=("Arial", 12))
send_count_display.pack(pady=10)

# 定时更新已发送次数显示
def update_send_count_display():
    send_count_display.config(text=f"已发送次数: {send_count}次")
    root.after(1000, update_send_count_display)

update_send_count_display()

root.mainloop()