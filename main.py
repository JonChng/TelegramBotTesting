#CURRENT GOAL: Integrate OpenAI API to allow for ChatGPT use of the bot in Telegram.


import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import dotenv
dotenv.load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="This bot is still in progress. Please try again later.")


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ['TOKEN']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

