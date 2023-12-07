from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import html

# libs
from libs import MESSAGES

#keyboards 
from keyboards import main_kb, courses_kb

router = Router() 

@router.message(F.text == "📚 Kurslar")
async def cmd_start(message: Message):
    return await message.answer(f"{html.bold(MESSAGES['courses'])}", reply_markup=courses_kb)

