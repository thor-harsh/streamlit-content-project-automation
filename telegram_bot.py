import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_to_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("Telegram bot token or chat ID not set!")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Telegram API Error: {response.status_code}, {response.text}")

def send_summaries_in_batches(df):
    summaries = df.dropna(subset=["Summary"]).to_dict("records")
    for i in range(0, len(summaries), 2):
        batch = summaries[i:i + 2]

        for article in batch:
            message = (
                f"**🗂️ Category:** {article['Category Name']}\n"
                f"**📄 Description:** {article['Description']}\n\n"
                f"**✨ Summary:**\n{article['Summary']}\n\n"
                f"🔗 **Read More:** [Click Here]({article['Link']})\n"
                "----------------------------------------"
            )
            send_to_telegram(message)

        time.sleep(30)

