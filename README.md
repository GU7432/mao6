# mao6

自動發送訊息到 Twitch 聊天室。

## 目錄
- [介紹](#介紹)
- [安裝與使用說明](#安裝與使用說明)
- [建議改進](#建議改進)

## 介紹
這個專案使用 **Python** 和 **Selenium** 來實現自動登入 Twitch 並發送訊息的功能。

## 🛠️ 安裝與使用說明
### 1. 安裝環境
請確保你已安裝：
- Python 3.x
- Google Chrome 瀏覽器
- `pip` 套件管理器

### 2. 安裝必要的 Python 套件
```bash
pip3 install selenium
```
### 3. 在run.sh中設定路徑位置
創建新的瀏覽器資料夾
--user-data-dir="C:\MYDATA\Script\Python\twitch-bot\userdata" 改成自己想要的路徑
