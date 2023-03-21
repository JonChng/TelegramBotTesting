# import asyncio
# import telegram
#
#
#
# async def main():
#     bot = telegram.Bot("5670247797:AAEKkuO9l-UQ3DMr7GeCxmEzQFyBl0qPkU8")
#     async with bot:
#         await bot.send_message(text='Hi Keii!', chat_id=401735120)
#
#
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

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
    print(context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ['TOKEN']).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()