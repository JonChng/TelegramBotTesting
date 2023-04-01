# CURRENT GOAL: Integrate OpenAI API to allow for ChatGPT use of the bot in Telegram.


import logging
import os
import dotenv
import telebot
import openai
import dotenv
import os
import requests

dotenv.load_dotenv()

token = os.environ['TOKEN']
apikey = os.environ['OPENAI_API']
org_key = os.environ['OPENAI_ORG_KEY']

endpoint1 = "https://api.openai.com/v1/completions"
endpoint2 = "https://api.openai.com/v1/models"
headers = {
    "Authorization": f"Bearer {apikey}",
    "Open-AI Organization":f"{org_key}",
    "Content-Type":"application/json"
}


def get_response(prompt):
    params = {
        "model": "text-davinci-003",
        "prompt": f"{prompt}",
        "max_tokens": 1000,
    }

    data = requests.post(endpoint1, json=params, headers=headers)
    data.raise_for_status()

    reply = data.json()['choices'][0]['text']
    return reply

bot = telebot.TeleBot(token)

is_active = False

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global is_active
    msg = bot.send_message(message.chat.id, "Hello there!"
                                            " To use this bot, type '/ask <prompt>'")
    is_active = True


@bot.message_handler(commands=['ask'], func=lambda message:True)
def ask(message):
    global is_active

    if is_active:
        reply = message.text.split(" ", 1)[1]
        answer = get_response(reply)
        msg = bot.reply_to(message, answer)
    else:
        msg = bot.reply_to(message, "Please start the bot with /start!")


bot.infinity_polling()




