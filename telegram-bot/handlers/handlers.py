import io

from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.context import FSMContext
from PIL import Image

from lexicon.lexicon import LEXICON_RU
from core.config import bot
from services import *
from keyboards import *

router: Router = Router()


@router.message(Command('help'))
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.photo)
async def calculate_topics(message: Message):
    tg_photo = await bot.get_file(message.photo[-1].file_id)
    print(type(await bot.download_file(tg_photo.file_path)), await bot.download_file(tg_photo.file_path))
    img = Image.open(await bot.download_file(tg_photo.file_path))
    print(type(img), img)
    print(type(Image), Image)
    try:
        latex = API().get_latex(img)
        print(type(latex), latex)
        try:
            answer = API.integrate_from_latex(latex, 1000)
            if answer['success']:
                text = str('<b>Метод прямоугольников</b>: <i>{}</i>\n'
                           '<b>Метод трапеций</b>: <i>{}</i>\n'
                           '<b>Метод парабол</b>: <i>{}</i>').format(
                    answer['squares_method'],
                    answer['trapezoids_method'],
                    answer['parabolic_method']
                )

            await message.answer(text)
            # await bot.send_photo(
            #     chat_id=message.from_user.id,
            #     photo='latex_integral_{message.from_user.id}.jpg',
            #     caption='Верно ли распознан интеграл?')
        except Exception as e:
            print(e)
            await message.answer(str(e))
    except Exception as e:
        print(e)
        await message.answer('😔 Не удалось обработать изображение')


@router.message(F.text)
async def calculate_function(message: Message, state: FSMContext):
    try:
        k, b, left, right = [float(el) for el in message.text.split()]
    except Exception as e:
        print(e)
        await message.answer('🤕 Неверный формат ввода.\nФормат ввода смотрите по команде /help')

    def func(x):
        return sqrt(k * x + b)

    text = f'Интеграл для функции <code>sqrt({k} * x + {b})</code>\nВ пределах от {left} до {right}:\n\n'
    text += ('<b>Метод прямоугольников</b>: <i>{}</i>\n'
             '<b>Метод трапеций</b>: <i>{}</i>\n'
             '<b>Метод парабол</b>: <i>{}</i>').format(
        str(rectangle_method(func, left, right, 1000)),
        str(trapezoid_method(func, left, right, 1000)),
        str(simpson_method(func, left, right, 1000))
    )

    await message.answer(text=text)


@router.message(Command('help'))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.callback_query(F.data == 'cancel_button')
async def cancel_button_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Действие отменено')
    await state.clear()
