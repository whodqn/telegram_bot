from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '7420711472:AAFiEtyLb6QNDYXGomrZpJGQIV8DMCmPuG4'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ ботинок(bot) от Никитосика!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
   await message.reply("Никита с Перми, прям щас, прям тут!")

@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)