
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

courses_kb = InlineKeyboardMarkup(inline_keyboard=[
    [ InlineKeyboardButton(text="🖥 Front-end", callback_data="front-end") ],
    [ InlineKeyboardButton(text="🖥 Back-end", callback_data="back-end") ],
])

