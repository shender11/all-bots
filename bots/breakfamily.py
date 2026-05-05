from aiogram import Bot, Dispatcher


TOKEN = "PASTE_BREAKFAMILY_TOKEN_HERE"
ADMIN_ID = 0
OWNER_ID = 0
SHEET_KEY = "PASTE_SHEET_KEY_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def start_bot():
    print("BreakFamily bot started")
    await dp.start_polling(bot)
