import os
import sys
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    raise RuntimeError("Không đọc được BOT_TOKEN")

if not CHAT_ID:
    raise RuntimeError("Không đọc được CHAT_ID")

message = """🔔 Đến giờ kiểm tra trạng thái kênh.

✔ Kiểm tra trạng thái kênh
✔ Nếu kênh ổn định thì phát thông báo"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=30
)

print("HTTP status:", response.status_code)
print("Telegram response:", response.text)

if not response.ok:
    sys.exit(1)
