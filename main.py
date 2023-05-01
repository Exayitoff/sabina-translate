import requests
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5421188853:AAHeIGnMcFbKwrRuVjmKPi0V6NqPMzM0HtA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum, ushbu bot 5ta tilga tarjima qila oladi")



@dp.message_handler()
async def echo(message: types.Message):
   xabar = message.text 

   r = requests.get(f'https://trans.noxi8.repl.co/en/text={xabar}')
   r2 = requests.get(f'https://trans.noxi8.repl.co/ru/text={xabar}')
   r3= requests.get(f'https://trans.noxi8.repl.co/fr/text={xabar}')
   r4 = requests.get(f'https://trans.noxi8.repl.co/nl/text={xabar}')
   r5 = requests.get(f'https://trans.noxi8.repl.co/tr/text={xabar}')
   
   response = r.json()["text"]
   response2 = r2.json()["text"]
   response3 = r3.json()["text"]
   response4 = r4.json()["text"]
   response5 = r5.json()["text"]
   await message.reply(f'In english🇺🇸:  {response}\nНа русском🇷🇺:  {response2}\nEn français🇫🇷:  {response3}\nauf Deutsch🇩🇪:  {response4}\nTürkçe olarak🇹🇷:  {response5}')
   
   
   
   
   
   
   
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)