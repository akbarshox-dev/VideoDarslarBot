
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📚 Kurslar")  ],  
    [KeyboardButton(text="🗃 Saqlanganlar"), KeyboardButton(text="☎️ Aloqa")] 
], resize_keyboard=True)

