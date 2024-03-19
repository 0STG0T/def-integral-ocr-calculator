from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


def create_inline_kb(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup(resize_keyboard=True)


def create_reply_kb(width: int, *args: str, ) -> ReplyKeyboardMarkup:
    kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    buttons: list[KeyboardButton] = []

    if args:
        for button in args:
            buttons.append(KeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button
            )
            )
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup(resize_keyboard=True)


def create_grades_kb():
    grades_kb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button in ['7', '8', '9', '10', '11']:
        buttons.append(InlineKeyboardButton(
            text=button,
            callback_data=f'{button}_grade'
        )
        )

    # buttons.append(InlineKeyboardButton(text=LEXICON_RU['back_button'], callback_data='back_button_pressed'))
    grades_kb.row(*buttons, width=5)

    return grades_kb.as_markup(resize_keyboard=True)


def create_back_to_modules_kb(grade) -> InlineKeyboardMarkup:
    kb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_RU['back_button'], callback_data=f'back_to_modules_{grade}'
    )
    kb.row(button, width=1)

    return kb.as_markup(resize_keyboard=True)


def create_confirm_kb() -> InlineKeyboardMarkup:
    kb: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button in ['✅ Да', '❌ Нет, попробовать снова']:
        buttons.append(InlineKeyboardButton(
            text=button,
            callback_data=f'{button}_grade'
        )
        )

    # buttons.append(InlineKeyboardButton(text=LEXICON_RU['back_button'], callback_data='back_button_pressed'))
    kb.row(*buttons, width=2)

    return kb.as_markup(resize_keyboard=True)
