from slack_sdk import WebClient
from apscheduler.schedulers.blocking import BlockingScheduler
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = "C08KTSW7DR9"

client = WebClient(token=SLACK_TOKEN)

def send_standup_reminder():
    client.chat_postMessage(
        channel=CHANNEL_ID,
        text=(
            "\U0001F44B Time for *daily standup* <!channel>! Please join the standup and update with:\n"
            "• What you did yesterday\n"
            "• What you're doing today\n"
            "• Any blockers"
        )
    )

scheduler = BlockingScheduler()
scheduler.add_job(send_standup_reminder, 'cron', day_of_week='mon-fri', hour=11, minute=30)
scheduler.start()
