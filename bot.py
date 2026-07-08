import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """🔔 Đến giờ kiểm tra trạng thái kênh.

✔ Kiểm tra trạng thái kênh
✔ Nếu kênh ổn định thì phát thông báo
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=data)

print(response.text)
