import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode # 7253960792:AAGrpqPXvY9ZIXgqAC_Zqi3MT8_DvSvkVAg
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')