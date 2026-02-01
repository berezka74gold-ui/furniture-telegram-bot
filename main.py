from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🪑 Каталог мебели", "🎯 Подбор мебели")
    kb.add("🚚 Доставка", "📞 Менеджер")
    await message.answer("Здравствуйте! 👋 Я помогу подобрать мебель и оформить заказ.", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp)
