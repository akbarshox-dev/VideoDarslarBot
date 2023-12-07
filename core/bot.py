import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import start, courses

from config import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.include_routers(start.router, courses.router)
