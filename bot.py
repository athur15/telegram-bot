import os
import requests
from datetime import datetime, timedelta, timezone

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

vn_time = datetime.now(timezone(timedelta(hours=7)))
current_time = vn_time.strftime("%H:%M")

allowed_times = ["23:00", "01:00", "03:00", "05:00", "07:00", "09:00"]

if current_time not in allowed_times:
    print(f"Not sending. Current VN time: {current_time}")
    exit()

message = """🔔 Đến giờ kiểm tra trạng thái kênh.

✔ Kiểm tra trạng thái kênh
✔ Nếu kênh ổn định thì phát thông báo"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.text)
