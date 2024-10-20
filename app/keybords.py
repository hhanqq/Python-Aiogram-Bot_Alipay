from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import emoji


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=emoji.emojize('Актуальный курс :chart_increasing_with_yen:'), callback_data='current_rate'), InlineKeyboardButton(text=emoji.emojize('Регистрация Alipay :school: '), callback_data='allowance')],
    [InlineKeyboardButton(text=emoji.emojize('Отзывы :closed_mailbox_with_raised_flag:'), callback_data='reviews', url='https://t.me/MONEY_ALIPAY_REVIEWS'),InlineKeyboardButton(text=emoji.emojize('Тех. поддержка :gear:'), callback_data='support', url='https://t.me/money_alipay')]])

rev = ReplyKeyboardMarkup(keyboard=
    [[KeyboardButton(text=emoji.emojize('Оставить заявку на пополнение :memo:'), callback_data='request')]], resize_keyboard=True)

req = InlineKeyboardMarkup(inline_keyboard=
    [[InlineKeyboardButton(text=emoji.emojize('Подтвердить :check_mark_button:'), callback_data='yes')],
    [InlineKeyboardButton(text=emoji.emojize('Отказаться :cross_mark:'), callback_data='no')]])

back = InlineKeyboardMarkup(inline_keyboard=
    [[InlineKeyboardButton(text=emoji.emojize('Вернуться на главное меню :right_arrow_curving_left:'), callback_data='back')]])