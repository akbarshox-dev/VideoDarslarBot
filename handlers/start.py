from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import html

# libs
from libs import MESSAGES

#keyboards 
from keyboards import main_kb

router = Router() 

@router.message(Command("start"))  
async def cmd_start(message: Message):
    return await message.answer(f"{html.bold(MESSAGES['welcome'])}", reply_markup=main_kb)

