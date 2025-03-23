from telegram import Bot
from config import TOKEN, CHAT_ID

bot = Bot(token=TOKEN)

def send_notification(job):
    message = f"New Job Alert:\n\n{job['title']}\n{job['company']} - {job['location']}\n{job['link']}"
    bot.send_message(chat_id=CHAT_ID, text=message)