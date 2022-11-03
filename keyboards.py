from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

from constants import ANSWERS, START_BUTTONS


def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    for text, callback_data in START_BUTTONS.items():
        builder.add(types.InlineKeyboardButton(
            text=text,
            callback_data=callback_data)
        )
    return builder


def get_answers_keyboard():
    builder = InlineKeyboardBuilder()
    for index, answer in enumerate(ANSWERS):
        builder.add(types.InlineKeyboardButton(
            text=answer,
            callback_data=f'answer_{index+1}'
        ))
    builder.adjust(1)
    return builder


def get_end_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='В меню',
        callback_data='restart')
    )
    return builder
