from aiogram.types import Message, CallbackQuery, BufferedInputFile
from states import take_url, cut_link, qr_link
from aiogram.fsm.context import FSMContext
from langid import classify, set_languages
from aiogram.filters import CommandStart
from urls import fetch_ical, short_link
from datetime import datetime, date
from statistics import new_request
from config import language as lg
from icalendar import Calendar
from aiogram import Router, F
from config import months
from io import BytesIO
import keyboards as kb
import aiosqlite
import qrcode

set_languages(['ru','en','zh'])
user = Router()

@user.message(CommandStart())
async def start_bot(message: Message):
    await message.answer('🇷🇺 Добро пожаловать в бота! Пожалуйста, выберите язык:\n\n'
                         '🇬🇧 Welcome to the bot! Please select a language:\n\n'
                         '🇨🇳 歡迎使用機器人！請選擇語言:',
                         reply_markup=kb.choose_language)


@user.callback_query(F.data.startswith('select_'))
async def select_language(call: CallbackQuery):
    language = call.data.split('_')[1]

    async with aiosqlite.connect('psu.db') as db:
        async with db.execute('SELECT user_id FROM users WHERE user_id = ?', (call.message.chat.id,)) as cur:
            check_user = await cur.fetchone()

        if check_user is None:
            await db.execute('INSERT INTO users (user_id, user_language) VALUES (?, ?)', (call.message.chat.id, language))
            await new_request('new_users', call.message.chat.id)
        else:
            await db.execute('UPDATE users SET user_language = ? WHERE user_id = ?', (language, call.message.chat.id))

        await db.commit()

    await call.message.edit_text(text=f'{lg['language_changed'][language]}')
    await call.message.answer(f'{lg['welcome'][language]}',
                              reply_markup=kb.menu[f'{language}_menu'])


@user.message(F.text.in_(['🗓 Мое расписание', '🗓 My timetable', '🗓 我的日程安排']))
async def take_schedule(message:Message, state: FSMContext):
    async with aiosqlite.connect('psu.db') as db:
        async with db.execute('SELECT url FROM users WHERE user_id = ?', (message.chat.id,)) as cur:
            link = await cur.fetchone()

    link = link[0]
    language = classify(message.text)[0]

    date_title = str(datetime.now().date())
    date_title = f'{date_title[8:]}.{date_title[5:7]}.{date_title[0:4]}'

    if link is None:
        await message.answer(text=lg['need_url'][language],
                             parse_mode='HTML',
                             reply_markup=kb.cancel[language])

        await state.set_state(take_url.lang)
        await state.update_data(lang=language)
        await state.set_state(take_url.url)

    else:
        msg = await message.answer(f'{lg['loading'][language]}')

        url = await fetch_ical(link)
        cal = Calendar.from_ical(url)

        timetable = {'08:00' : '<b>1.</b> ', '09:45': '<b>2.</b> ', '11:30': '<b>3.</b> ', '13:30': '<b>4.</b> ', '15:15': '<b>5.</b> ', '17:00': '<b>6.</b> '}

        for component in cal.walk():
            if component.name == "VEVENT":
                sunject = str(component.get('summary'))
                start = str(component.get('dtstart').dt)
                end = str(component.get('dtend').dt).split()[1].split('+')[0][:5]
                location = str(component.get('location'))
                teacher = str(component.get('description'))

                if str(datetime.now()).split()[0] in start:
                    timetable[start.split()[1].split('+')[0][:5]] += f'<b>{sunject}</b>\n🏛 {location}\n👩‍🏫 <i>{teacher}</i>\n⏱️ <code>{start.split()[1].split('+')[0][:5]} - {end}</code>'

        stroka = f'<b>{lg['days'][language][datetime.now().weekday()]} {date_title}</b>\n\n'
        for i in timetable:
            stroka += f'{timetable[i]}\n\n'

        await new_request('timetable', message.chat.id)

        keyboard = await kb.generate_week_keyboard(int(datetime.now().day), int(datetime.now().month), int(datetime.now().year), datetime.now().weekday())

        await msg.edit_text(stroka, reply_markup=keyboard[language], parse_mode='HTML')

@user.callback_query(F.data.startswith('date_'))
async def week_days(call: CallbackQuery):
    async with aiosqlite.connect('psu.db') as db:
        async with db.execute('SELECT url, user_language FROM users WHERE user_id = ?', (call.message.chat.id,)) as cur:
            take_data = await cur.fetchone()

    link = take_data[0]
    language = take_data[1]

    await call.message.edit_text(f'{lg['loading'][language]}')

    new_date, new_month = map(int, call.data.split('_')[1].split('.'))

    if new_date > months[new_month]:
        new_date -= months[new_month]
        new_month += 1

    elif new_date < 1:
        new_month -= 1
        new_date = months[new_month] + new_date

    if new_month == 0:
        new_year = datetime.now().year - 1

    elif new_month == 13:
        new_year = datetime.now().year + 1

    else:
        new_year = datetime.now().year

    if new_date // 10 == 0:
        new_date = '0' + str(new_date)

    if new_month // 10 == 0:
        new_month = '0' + str(new_month)

    result_date = str(new_year) + '-' + str(new_month) + '-' + str(new_date)
    date_title = f'{result_date[8:]}.{result_date[5:7]}.{result_date[:4]}'

    url = await fetch_ical(link)
    cal = Calendar.from_ical(url)

    timetable = {'08:00': '<b>1.</b> ', '09:45': '<b>2.</b> ', '11:30': '<b>3.</b> ', '13:30': '<b>4.</b> ',
                 '15:15': '<b>5.</b> ', '17:00': '<b>6.</b> '}

    for component in cal.walk():
        if component.name == "VEVENT":
            sunject = str(component.get('summary'))
            start = str(component.get('dtstart').dt)
            end = str(component.get('dtend').dt).split()[1].split('+')[0][:5]
            location = str(component.get('location'))
            teacher = str(component.get('description'))

            if result_date in start:
                timetable[start.split()[1].split('+')[0][
                    :5]] += f'<b>{sunject}</b>\n🏛 {location}\n👩‍🏫 <i>{teacher}</i>\n⏱️ <code>{start.split()[1].split('+')[0][:5]} - {end}</code>'

    stroka = f'<b>{lg['days'][language][date(int(new_year), int(new_month), int(new_date)).weekday()]} {date_title}</b>\n\n'
    for i in timetable:
        stroka += f'{timetable[i]}\n\n'

    keyboard = await kb.generate_week_keyboard(int(new_date), int(new_month), int(new_year), (date(int(new_year), int(new_month), int(new_date)).weekday()))
    await call.message.edit_text(stroka, reply_markup=keyboard[language], parse_mode='HTML')

@user.message(F.text.in_(['🔗 Сократить ссылку', '🔗 Shorten link', '🔗 縮短鏈接']))
async def take_link(message:Message, state: FSMContext):
    language = classify(message.text)[0]
    await state.set_state(cut_link.lang)
    await state.update_data(lang=language)
    await state.set_state(cut_link.link)
    await message.answer(lg['put_cut_url'][language], reply_markup=kb.cancel[language])

@user.message(cut_link.link)
async def received_url(message:Message, state: FSMContext):
    language = await state.get_data()
    language = language['lang']

    if message.text in ['❌ Отмена', '❌ Cancel', '❌ 取消']:
        await state.clear()
        await message.answer(message.text,
                             reply_markup=kb.menu[f'{language}_menu'])
    else:
        url = await short_link(message.text)
        if 'https://clck.ru/' in url:
            await message.answer(f'{url}\n\n{lg['by_psu_bot'][language]}',
                                    reply_markup=kb.menu[f'{language}_menu'],
                                    parse_mode='HTML')
            await state.clear()
            await new_request('cut_link', message.chat.id)

        else:
            await message.answer(f'{lg['link_error'][language]}',
                                 parse_mode='HTML')


@user.message(F.text.in_(['🔖 Сделать QR', '🔖 Create QR-Code', '🔖 製作二維碼']))
async def take_qrlink(message: Message, state: FSMContext):
    language = classify(message.text)[0]
    await state.set_state(qr_link.lang)
    await state.update_data(lang=language)
    await state.set_state(qr_link.link)
    await message.answer(lg['put_qr_url'][language], reply_markup=kb.cancel[language])

@user.message(qr_link.link)
async def send_qr(message:Message, state: FSMContext):
    language = await state.get_data()
    language = language['lang']
    if message.text in ['❌ Отмена', '❌ Cancel', '❌ 取消']:
        await state.clear()
        await message.answer(message.text,
                             reply_markup=kb.menu[f'{language}_menu'])
    else:
        try:
            img = qrcode.make(message.text)
            qr_buffer = BytesIO()
            img.save(qr_buffer, format='PNG')
            qr_buffer.seek(0)
            photo = BufferedInputFile(qr_buffer.getvalue(), filename="qrcode.png")

            await message.answer_photo(photo=photo,
                                       caption=lg['by_psu_bot'][language],
                                       parse_mode='HTML',
                                       reply_markup=kb.menu[f'{language}_menu'])

            await new_request('make_qr', message.chat.id)
            await state.clear()

        except Exception as e:
            await message.answer(f'{lg['qr_error'][language]}',
                                 parse_mode='HTML')

@user.message(F.text.in_(['🗺 Карта ПГНИУ', '🗺 Map of PSU', '🗺 地圖']))
async def take_ru_timetable(message: Message):
    await new_request('check_map', message.chat.id)
    await message.answer_photo(photo='AgACAgIAAxkBAANQagXfW1f3FfOlCiLpgKRceE60xIwAAp0WaxsL1jFIGDqvwWsQyakBAAMCAAN5AAM7BA')

@user.message(F.text.in_(['⚙️ Настройки', '⚙️ Settings', '⚙️ 設定']))
async def settings(message:Message):
    async with aiosqlite.connect('psu.db') as db:
        async with db.execute('SELECT user_language, url FROM users WHERE user_id = ?', (message.chat.id,)) as cur:
            language, link = await cur.fetchone()

    output = (f'{lg['profile'][language]}\n\n'
              f'🆔 ID: <code>{message.chat.id}</code>\n' 
              f'{lg['language'][language]} <code>{language}</code>\n'
              f'{lg['link'][language]} {link}')

    await message.answer(output, parse_mode='HTML', reply_markup=kb.settings[language])

@user.callback_query(F.data.startswith('change_lg'))
async def change_language(call: CallbackQuery):
    language = call.data.split('_')[2]
    await call.message.edit_text(lg['new_language'][language],
                                 reply_markup=kb.choose_language)

@user.callback_query(F.data.startswith('change_link'))
async def change_link(call: CallbackQuery, state: FSMContext):
    language = call.data.split('_')[2]
    await call.message.delete()
    await call.message.answer(text=lg['need_url'][language],
                         parse_mode='HTML',
                         reply_markup=kb.cancel[language])

    await state.set_state(take_url.lang)
    await state.update_data(lang=language)
    await state.set_state(take_url.url)

@user.message(take_url.url)
async def get_url(message: Message, state:FSMContext):
    if message.text in ['❌ Отмена', '❌ Cancel', '❌ 取消']:
        await state.clear()
        await message.answer(message.text,
                             reply_markup=kb.menu[f'{classify(message.text)[0]}_menu'])
    else:
        data = await state.get_data()
        language = data['lang']

        try:
            url = await fetch_ical(message.text)
            cal = Calendar.from_ical(url)
            await state.clear()

            async with aiosqlite.connect('psu.db') as db:
                await db.execute('UPDATE users SET url = ? WHERE user_id = ?', (message.text, message.chat.id))
                await db.commit()

            await message.answer(text=lg['link_added'][language],
                                 reply_markup=kb.menu[f'{language}_menu'])

        except Exception:
            await message.answer(f'{lg['link_error'][language]}',
                                 parse_mode='HTML')

@user.message(F.text.in_(['ℹ️ О боте', 'ℹ️ About the bot', 'ℹ️ 關於機器人']))
async def about_bot(message: Message):
    language = classify(message.text)[0]
    await message.answer(lg['about_bot'][language], parse_mode='HTML', reply_markup=kb.work[language])