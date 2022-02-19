import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5095894833:AAFdTRlp8ykBxmZdcwjsEtHneulr2lzzt_0'
wikipedia.set_lang('uz')

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
    await message.reply("Wikipedia Botiga Xush Kelibsiz!, menga hohlagan so'zingizni yuboring, men sizga bu so'zning izohini jo'nataman")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)