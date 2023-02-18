import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = Bot(token='5576766843:AAFoBPgLz26ZT0-DvDy3SalNNUsUFeofaGo')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text="закон архимеда")], [types.KeyboardButton(text="закон паскаля")], [types.KeyboardButton(text="закон херни всякой")], [types.KeyboardButton(text="/help")]

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите формулу")
    await message.reply("Здравствуй, ты можешь меня спросить по формулам из физики.", reply_markup=keyboard)


@dp.message_handler()
async def cats(message: types.Message):
    if message.text == "закон архимеда":
        await message.reply("Сам закон звучит так:\n"
                            "Выталкивающая сила, действующая на погружённое в жидкость тело, равна весу жидкости, вытесненной этим телом \n"
                            "А формула вот: \n"
                            "F = ρ * g * V \n"
                            "Где \n"
                            "F - сила архимеда\n"
                            "ρ - плотность жидкости\n"
                            "V - объем погруженной части тела\n"
                            "g — ускорение свободного падения")


    if message.text == "закон паскаля":
        await message.reply("тут короче текст для закона, а чтобы перенести на новую строку, используй\n"
                            "а так же можешь для удобства делать так")

                            
    if message.text == "закон херни всякой":
        await message.reply("тут ты тоже допиши")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)