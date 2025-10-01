from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог',callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты',callback_data='contacts')]
])