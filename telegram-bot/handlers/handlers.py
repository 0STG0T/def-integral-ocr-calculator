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


@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/start'])


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
            API.plot_latex(latex, '../temp', str(message.from_user.id))
            # await bot.send_photo(
            #     f'../temp/latex_integral_{message.from_user.id}.jpg',
            #     caption='Верно ли распознан интеграл?')
        except Exception as e:
            print(e)
            await message.answer(str(e))
    except Exception as e:
        print(e)
        await message.answer('😔 Не удалось обработать изображение')


@router.message(F.text)
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


@router.message(Command('help'))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.callback_query(F.data == 'cancel_button')
async def cancel_button_process(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text='Действие отменено')
    await state.clear()
