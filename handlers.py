from aiogram import Router
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from constants import (
    START_TEXT,
    PT_OPINIONS,
    RT_OPINIONS,
    PT_SUM1_INDEXES,
    PT_SUM2_INDEXES,
    RT_SUM1_INDEXES,
    RT_SUM2_INDEXES,
    END_TEXT
)
from keyboards import (
    get_start_keyboard,
    get_answers_keyboard,
    get_end_keyboard
)

router = Router()


@router.message(commands=['start', 'restart'])
@router.callback_query(text='restart')
async def start(call: Message | CallbackQuery, state: FSMContext):
    await state.update_data(opinion_index=0, sum1=0, sum2=0)
    answer = call.answer
    is_callback = type(call) == CallbackQuery
    if is_callback:
        answer = call.message.answer
    await answer(
        START_TEXT,
        reply_markup=get_start_keyboard().as_markup(resize_keyboard=True)
    )
    if is_callback:
        await call.answer()


@router.callback_query(Text(text_startswith='start_'))
async def callbacks_choose_test(callback: CallbackQuery, state: FSMContext):
    test_name = callback.data.split('_')[1]
    opinions = []

    if test_name == 'rt':
        opinions = [RT_OPINIONS, RT_SUM1_INDEXES, RT_SUM2_INDEXES, 1]
    elif test_name == 'pt':
        opinions = [PT_OPINIONS, PT_SUM1_INDEXES, PT_SUM2_INDEXES, 21]

    await state.update_data(opinions=opinions)
    user_data = await state.get_data()

    await callback.message.answer(
        opinions[0][user_data['opinion_index']],
        reply_markup=get_answers_keyboard().as_markup(resize_keyboard=True)
    )
    await callback.answer()


@router.callback_query(Text(text_startswith='answer_'))
async def callback_answer(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sum1 = user_data['sum1']
    sum2 = user_data['sum2']
    opinions = user_data['opinions']
    opinion_index = user_data['opinion_index']
    answer_number = int(callback.data.split('_')[1])

    if opinion_index + opinions[3] in opinions[1]:
        await state.update_data(sum1=sum1 + answer_number)
    elif opinion_index + opinions[3] in opinions[2]:
        await state.update_data(sum2=sum2 + answer_number)

    if opinion_index < 19:
        await state.update_data(opinion_index=opinion_index+1)
        user_data = await state.get_data()
        await update_question_text(
            callback.message,
            opinions[0][user_data['opinion_index']]
        )
    else:
        user_data = await state.get_data()
        await callback.message.answer(
            END_TEXT + ': ' + str(
                calculation(user_data['sum1'], user_data['sum2'])
            ),
            reply_markup=get_end_keyboard().as_markup()
        )
        await state.clear()
    await callback.answer()


def calculation(sum1, sum2: int):
    return sum1 - sum2 + 35


async def update_question_text(message: Message, new_value: str):
    await message.edit_text(
        new_value,
        reply_markup=get_answers_keyboard().as_markup(resize_keyboard=True)
    )
