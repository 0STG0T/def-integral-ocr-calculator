from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON_RU
from services import *
from keyboards import *

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/start'])


@router.message()
async def calculate_function(message: Message, state: FSMContext):
    k, b, left, right = [float(el) for el in message.text.split()]

    def func(x):
        return sqrt(k * x + b)

    text = ('<b>Метод прямоугольников</b>: <i>{}</i>\n'
            '<b>Метод трапеций</b>: <i>{}</i>\n'
            '<b>Метод парабол</b>: <i>{}</i>').format(
        str(rectangle_method(func, left, right, 100)),
        str(trapezoid_method(func, left, right, 100)),
        str(simpson_method(func, left, right, 100))
    )

    await message.answer(text=text)


@router.message(F.photo)
async def calculate_topics(message: Message):
    pass


@router.message(Command('help'))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.callback_query(F.data == 'cancel_button')
async def cancel_button_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Действие отменено')
    await state.clear()


# @router_user.message(F.text == LEXICON_RU['user_show_content'])
# async def content_button_pressed(message: Message):
#     await message.answer(text=LEXICON_RU['choose_your_grade'], reply_markup=create_grades_kb())
#
#
# @router_user.callback_query(UserGradeFilter())
# async def show_modules_grade(callback: CallbackQuery):
#     grade = callback.data.split('_')[0]
#     await callback.message.edit_text(
#         text='🗂 Выберите тему:',
#         reply_markup=show_topics_kb(grade)
#     )
#
#
# @router_user.callback_query(UserBackButtonFilter())
# async def show_modules_grade(callback: CallbackQuery):
#     grade = callback.data.split('_')[-1]
#     await callback.message.edit_text(
#         text='🗂 Выберите тему:',
#         reply_markup=show_topics_kb(grade)
#     )
#
#
# @router_user.callback_query(TopicsCallbacksFilter())
# async def show_content(callback: CallbackQuery):
#     grade = callback.data.split('_')[1]
#     title = callback.data.split('_')[0]
#     try:
#         data = crud.get_content_by_title(grade, title)
#         text = f'📖 <b>{title}</b>' + '\n\n' + data[1]
#         await callback.message.edit_text(
#             text=text,
#             reply_markup=create_back_to_modules_kb(grade)
#         )
#     except Exception as e:
#         await callback.message.edit_text(
#             text='Something went wrong' + f'\n\n👾 Error: {e}',
#             reply_mahrkup=create_back_to_modules_kb(grade)
#         )
