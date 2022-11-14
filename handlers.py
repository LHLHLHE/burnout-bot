from aiogram import Router
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from constants import (
    START_TEXT,
    LT_OPINIONS,
    RT_OPINIONS,
    ST_OPINIONS,
    LT_SUM1_INDEXES,
    LT_SUM2_INDEXES,
    RT_SUM1_INDEXES,
    RT_SUM2_INDEXES,
    ST_SUM1_INDEXES,
    ST_SUM2_INDEXES,
    END_TEXT,
    ANXIETY_LEVEL
)
from keyboards import (
    get_start_keyboard,
    get_answers_keyboard,
    get_end_keyboard
)

router = Router()


async def start(answer):
    await answer(
        START_TEXT,
        reply_markup=get_start_keyboard().as_markup(resize_keyboard=True)
    )


@router.message(commands=['start'])
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await start(message.answer)


@router.callback_query(text='restart')
async def callbacks_start(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await start(callback.message.answer)
    await callback.answer()


@router.callback_query(Text(text_startswith='start_'))
async def callbacks_choose_test(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.update_data(opinion_index=0, sum1=0, sum2=0)
    test_name = callback.data.split('_')[1]
    test_data = []

    if test_name == 'rt':
        test_data = [
            RT_OPINIONS,
            RT_SUM1_INDEXES,
            RT_SUM2_INDEXES,
            1,
            lt_rt_calculation
        ]
    elif test_name == 'lt':
        test_data = [
            LT_OPINIONS,
            LT_SUM1_INDEXES,
            LT_SUM2_INDEXES,
            21,
            lt_rt_calculation
        ]
    elif test_name == 'st':
        test_data = [
            ST_OPINIONS,
            ST_SUM1_INDEXES,
            ST_SUM2_INDEXES,
            1,
            st_calculation
        ]

    await state.update_data(test_data=test_data)
    user_data = await state.get_data()

    await callback.message.answer(
        test_data[0][user_data['opinion_index']],
        reply_markup=get_answers_keyboard().as_markup(resize_keyboard=True)
    )
    await callback.answer()


@router.callback_query(Text(text_startswith='answer_'))
async def callback_answer(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    sum1 = user_data['sum1']
    sum2 = user_data['sum2']
    test_data = user_data['test_data']
    opinion_index = user_data['opinion_index']
    answer_number = int(callback.data.split('_')[1])
    opinions_list = test_data[0]
    test_sum1_indexes = test_data[1]
    test_sum2_indexes = test_data[2]
    index_shift = test_data[3]

    if opinion_index + index_shift in test_sum1_indexes:
        await state.update_data(sum1=sum1 + answer_number)
    elif opinion_index + index_shift in test_sum2_indexes:
        await state.update_data(sum2=sum2 + answer_number)

    if opinion_index < len(opinions_list) - 1:
        await state.update_data(opinion_index=opinion_index+1)
        user_data = await state.get_data()
        await update_question_text(
            callback.message,
            opinions_list[user_data['opinion_index']]
        )
    else:
        user_data = await state.get_data()
        result = test_data[4](user_data['sum1'], user_data['sum2'])
        if result < 30:
            anxiety_level = ANXIETY_LEVEL.get('low')
        elif result >= 45:
            anxiety_level = ANXIETY_LEVEL.get('high')
        else:
            anxiety_level = ANXIETY_LEVEL.get('middle')
        await callback.message.answer(
            END_TEXT.format(
                str(result),
                anxiety_level
            ),
            reply_markup=get_end_keyboard().as_markup()
        )
        await callback.message.delete()
        await state.clear()
    await callback.answer()


def lt_rt_calculation(sum1, sum2: int):
    return sum1 - sum2 + 35


def st_calculation(sum1, sum2: int):
    return (sum1 - sum2 + 15) * 4


async def update_question_text(message: Message, new_value: str):
    await message.edit_text(
        new_value,
        reply_markup=get_answers_keyboard().as_markup(resize_keyboard=True)
    )
