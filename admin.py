from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery, FSInputFile, BufferedInputFile
from aiogram.fsm.context import FSMContext
from statistics import generate_diagram
from aiogram.filters import Command
from aiogram import Router, F, Bot
from states import send_message
from config import ADMIN_CHAT
from datetime import datetime
import keyboards as kb
import aiosqlite

admin = Router()

@admin.message(Command('admin'))
async def admin_panel(message: Message):
    if message.chat.id == ADMIN_CHAT:
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)

@admin.callback_query(F.data == 'mailing')
async def start_mailing(call: CallbackQuery, state: FSMContext):
    await state.set_state(send_message.ru)
    await call.message.delete()
    await call.message.answer('Введите сообщение на <b>Русском</b> языке:',
                              parse_mode='HTML', reply_markup=kb.cancel['ru'])

@admin.message(send_message.ru)
async def get_ru_text(message: Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)

    else:
        await state.update_data(ru=message.text)
        await state.set_state(send_message.en)
        await message.answer('Введите сообщение на <b>Английском</b> языке:',
                             parse_mode='HTML', reply_markup=kb.cancel['ru'])

@admin.message(send_message.en)
async def get_en_text(message: Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)

    else:
        await state.update_data(en=message.text)
        await state.set_state(send_message.zh)
        await message.answer('Введите сообщение на <b>Китайском</b> языке:',
                             parse_mode='HTML', reply_markup=kb.cancel['ru'])


@admin.message(send_message.zh)
async def get_zh_text(message: Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)

    else:
        await state.update_data(zh=message.text)
        await state.set_state(send_message.photo)
        await message.answer('Отправьте фото (если нужно)',
                             parse_mode='HTML', reply_markup=kb.skip_or_no)

@admin.message(send_message.photo)
async def get_photo(message: Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)
        return

    elif message.text == 'Skip':
        await state.update_data(photo='Skip')

    else:
        await state.update_data(photo=message.photo[-1].file_id)

    await state.set_state(send_message.button)
    await message.answer('Отправьте кнопку в формате: <b>[Русский текст;Английский текст;Китайский текст;Ссылка]</b> (или нет)',
                         parse_mode='HTML', reply_markup=kb.skip_or_no)


@admin.message(send_message.button)
async def message_check(message: Message, state: FSMContext):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)
        return

    elif message.text == 'Skip':
        await state.update_data(button='Skip')

    else:
        await state.update_data(button=message.text)

    data = await state.get_data()
    await state.set_state(send_message.is_good)

    ru_text, en_text, zh_text, photo, button = data.values()

    if photo != 'Skip' and button != 'Skip':
        button_ru_text, button_en_text, button_zh_text, button_link = button.split(';')
        await message.answer_photo(caption=ru_text, photo=photo, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=button_ru_text, url=button_link)]]))

    elif button != 'Skip':
        button_ru_text, button_en_text, button_zh_text, button_link = button.split(';')
        await message.answer(text=ru_text, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=button_ru_text, url=button_link)]]))

    elif photo != 'Skip':
        await message.answer_photo(caption=ru_text, photo=photo)

    else:
        await message.answer(text=ru_text)

    await message.answer('Тестовое сообщение. Отправляем?', reply_markup=kb.is_good_message)

@admin.message(send_message.is_good)
async def end_mailing(message: Message, state: FSMContext, bot: Bot):
    if message.text == '❌ Отмена':
        await state.clear()
        await message.answer('❌ Отмена', reply_markup=ReplyKeyboardRemove())
        await message.answer('Панель администратора', reply_markup=kb.admin_keyboard)
        return

    else:
        data = await state.get_data()
        await state.clear()
        ru_text, en_text, zh_text, photo, button = data.values()
        text = {'ru_text': ru_text, 'en_text': en_text, 'zh_text': zh_text}

        if button != 'Skip':
            button_ru_text, button_en_text, button_zh_text, button_link = button.split(';')
            buttons = {'button_ru_text': button_ru_text, 'button_en_text': button_en_text, 'button_zh_text': button_zh_text}

        async with aiosqlite.connect('psu.db') as db:
            async with db.execute('SELECT user_id, user_language FROM users') as cur:
                take_data = await cur.fetchall()

        sended = 0
        not_sended = 0

        await message.answer('💬 Начинаю рассылку...', reply_markup=ReplyKeyboardRemove())

        for user in take_data:
            user_id, user_language = user

            try:
                if photo != 'Skip' and button != 'Skip':
                    await bot.send_photo(chat_id=user_id, caption=text[f'{user_language}_text'], photo=photo,
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=buttons[f'button_{user_language}_text'], url=button_link)]]))

                elif button != 'Skip':
                    await bot.send_message(chat_id=user_id, text=text[f'{user_language}_text'],
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=buttons[f'button_{user_language}_text'], url=button_link)]]))

                elif photo != 'Skip':
                    await bot.send_photo(chat_id=user_id, caption=text[f'{user_language}_text'], photo=photo)

                else:
                    await bot.send_message(chat_id=user_id, text=text[f'{user_language}_text'])

                sended += 1

            except Exception as e:
                not_sended += 1

        await message.answer(f'✅ Рассылка завершена\n\n'
                             f'Сообщение доставлено <code>{sended}</code> пользователям\n\n'
                             f'<code>{not_sended}</code> пользователей не получили рассылку.',
                             parse_mode='HTML')

@admin.callback_query(F.data == 'download_bd')
async def send_bd(call: CallbackQuery):
    await call.message.edit_text(text='📄 База данных:')
    await call.message.answer_document(document=FSInputFile('psu.db'))

@admin.callback_query(F.data == 'check_statistics')
async def stats(call: CallbackQuery):
    await call.message.edit_text('Выберите статистику', reply_markup=kb.select_statistics)

@admin.callback_query(F.data.startswith('stats:'))
async def send_stats(call: CallbackQuery):
    type_stats = call.data.split(':')[1]

    image = await generate_diagram(type_stats)
    image = BufferedInputFile(image.getvalue(), filename="stats.png")

    if type_stats == 'today':
        async with aiosqlite.connect('psu.db') as db:
            async with db.execute('SELECT date, use_bot, timetable, cut_link, make_qr, check_map, new_users FROM statistics WHERE date = ?', (str(datetime.now()).split()[0],)) as cur:
                indicators = await cur.fetchone()

        date, use_bot, timetable, cut_link, make_qr, check_map, new_users = indicators

        await call.message.delete()
        await call.message.answer_photo(photo=image, reply_markup=kb.statistics_1,parse_mode='HTML',
                                        caption=f'<b>Статистика за <code>{date}</code></b>\n\n'
                                                f'Воспользовались ботом: <code>{use_bot}</code> человек\n'
                                                f'Новых пользователей: <code>{new_users}</code> человек\n\n'
                                                f'Посмотрели расписание: <code>{timetable}</code> раз\n'
                                                f'Сократили ссылку: <code>{cut_link}</code> раз\n'
                                                f'Сделали QR-Код: <code>{make_qr}</code> раз\n'
                                                f'Посмотрели карту: <code>{check_map}</code> раз')

    elif type_stats == 'new_users':
        await call.message.delete()
        await call.message.answer_photo(photo=image, reply_markup=kb.statistics_2, parse_mode='HTML')

    else:
        await call.message.delete()
        await call.message.answer_photo(photo=image, reply_markup=kb.statistics_3, parse_mode='HTML')