from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, Video
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keybords as kb

router = Router()

class Request(StatesGroup):
        quantity = State()
        number = State()

rate1 = 14.00 # 100
rate2 = 13.90 # 300
rate3 = 13.80 # 500
rate4 = 13.70 # 1000
rate5 = 13.50 # 3000

@router.message(CommandStart())
async def get_photo_and_message(message: Message):
        await message.answer_photo(photo=FSInputFile('logo final.png', filename='logo'), reply_markup=kb.rev)
        await message.answer(f'<a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a><a>, Вас приветствует бот для пополнения вашего кошелька Alipay !</a>', reply_markup=kb.main) # вариант с обращением по имени

@router.callback_query(F.data == 'current_rate')
async def current_rate(callback: CallbackQuery):
        await callback.answer('', show_alert = False)
        await callback.message.answer(f'Актуальный курс на xx.xx.2024:\n\nПри пополнении от 100¥ - {rate1}₽\n\nПри пополнении от 300¥ - {rate2}₽\n\nПри пополнении от 500¥ - {rate3}₽\n\nПри пополнении от 1000¥ - {rate4}₽\n\nПри пополнении от 3000¥ - {rate5}₽\n')


@router.callback_query(F.data == 'allowance')
async def allowance(callback: CallbackQuery):
        await callback.answer('', show_alert = False)
        await callback.bot.send_video(
                chat_id=callback.from_user.id,
                video=FSInputFile(path='guidetest.mp4')
        )
        await callback.message.answer('Представляем вам подробный гайд по регистрации кошелька Alipay !\nЕсли останутся вопросы, обратитесь в тех.поддержку.')

@router.message(F.text == 'Оставить заявку на пополнение 📝')
async def request(message: Message, state: FSMContext):
        await state.set_state(Request.quantity)
        await message.answer(text='Введите сумму в юанях (¥) которую вы желаете пополнить')

@router.message(Request.quantity)
async def request_quantity(message: Message, state: FSMContext):
        await state.update_data(quantity=message.text)
        await state.set_state(Request.number)
        await message.answer(text='Введите номер телефона, который привязан к кошельку Alipay, в формате:\n+7-XXX-XXX-XX-XX')

@router.message(Request.number)
async def request_number(message: Message, state: FSMContext):
        await state.update_data(number=message.text)
        await state.set_state(Request.number)
        data = await state.get_data()
        if float(data["quantity"]) >= 100 and float(data["quantity"]) < 300:
                await message.answer(f'Ваш номер: {data["number"]}.\nК оплате будет: {float(data["quantity"])*rate1} рублей.',reply_markup=kb.req)
        elif float(data["quantity"]) >= 300 and float(data["quantity"]) < 500:
                await message.answer(f'Ваш номер: {data["number"]}.\nК оплате будет: {float(data["quantity"])*rate2} рублей.',reply_markup=kb.req)
        elif float(data["quantity"]) >= 500 and float(data["quantity"]) < 1000:
                await message.answer(f'Ваш номер: {data["number"]}.\nК оплате будет: {float(data["quantity"])*rate3} рублей.',reply_markup=kb.req)
        elif float(data["quantity"]) >= 1000 and float(data["quantity"]) < 3000:
                await message.answer(f'Ваш номер: {data["number"]}.\nК оплате будет: {float(data["quantity"])*rate4} рублей.',reply_markup=kb.req)
        else:
                await message.answer(f'Ваш номер: {data["number"]}.\nК оплате будет: {float(data["quantity"])*rate5} рублей.',reply_markup=kb.req)

@router.callback_query(F.data == 'yes')
async def yes(callback: CallbackQuery, state: FSMContext):
        await callback.answer('', show_alert='False')
        await callback.message.answer('Ваша заявка одобрена!\nВ течении 20 минут с вами свяжется наш оператор, если этого не произошло, обратитесь в тех.поддержку.', reply_markup=kb.back)
        data_yes = await state.get_data()
        if float(data_yes["quantity"]) >= 100 and float(data_yes["quantity"]) < 300:
                await callback.bot.send_message(chat_id=-1002376952587, text=f'Пользователь: <a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a>\nНомер телефона привязанный к Alipay: {data_yes["number"]}\nКол-во юаней к пополнению: {float(data_yes["quantity"])}\nСумма к оплате: {float(data_yes["quantity"])*rate1} рублей')
        elif float(data_yes["quantity"]) >= 300 and float(data_yes["quantity"]) < 500:
                await callback.bot.send_message(chat_id=-1002376952587, text=f'Пользователь: <a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a>\nНомер телефона привязанный к Alipay: {data_yes["number"]}\nКол-во юаней к пополнению: {float(data_yes["quantity"])}\nСумма к оплате: {float(data_yes["quantity"])*rate2} рублей')
        elif float(data_yes["quantity"]) >= 500 and float(data_yes["quantity"]) < 1000:
                await callback.bot.send_message(chat_id=-1002376952587, text=f'Пользователь: <a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a>\nНомер телефона привязанный к Alipay: {data_yes["number"]}\nКол-во юаней к пополнению: {float(data_yes["quantity"])}\nСумма к оплате: {float(data_yes["quantity"])*rate3} рублей')
        elif float(data_yes["quantity"]) >= 1000 and float(data_yes["quantity"]) < 3000:
                await callback.bot.send_message(chat_id=-1002376952587, text=f'Пользователь: <a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a>\nНомер телефона привязанный к Alipay: {data_yes["number"]}\nКол-во юаней к пополнению: {float(data_yes["quantity"])}\nСумма к оплате: {float(data_yes["quantity"])*rate4} рублей')
        else:
                await callback.bot.send_message(chat_id=-1002376952587, text=f'Пользователь: <a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a>\nНомер телефона привязанный к Alipay: {data_yes["number"]}\nКол-во юаней к пополнению: {float(data_yes["quantity"])}\nСумма к оплате: {float(data_yes["quantity"])*rate5} рублей')

        await state.clear()

@router.callback_query(F.data == 'no')
async def no(callback: CallbackQuery):
        await callback.answer('', show_alert='False')
        await callback.message.answer('Ваша заявка отменена.', reply_markup=kb.back)


@router.callback_query(F.data == 'back')
async def test(callback: CallbackQuery):
        await callback.message.answer_photo(photo=FSInputFile('logo final.png', filename='logo'), reply_markup=kb.rev)
        await callback.message.answer(f'<a href="tg://user?id={callback.from_user.id}">{callback.from_user.full_name}</a><a>, Вас приветствует бот для пополнения вашего кошелька Alipay !</a>',reply_markup=kb.main)  # вариант с обращением по имени
        await callback.answer()

#@router.message(F.photo)
#async def cmd_start(message: Message) -> None:
#    photo_data = message.photo[-1]
#    await message.answer(f'{photo_data}')
# Вас приветствует бот для пополнения вашего кошелька Alipay !