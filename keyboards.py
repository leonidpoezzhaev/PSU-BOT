from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime

async def generate_week_keyboard(day, month, year, selected_day):
    weekday = datetime(year, month, day).isoweekday()
    another_color = ''
    days = [another_color, another_color, another_color, another_color, another_color, another_color]
    days[selected_day] = 'success'

    week = {
        'ru': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Пн', style=days[0],
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Вт', style=days[1],
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Ср', style=days[2],
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='Чт', style=days[3],
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Пт', style=days[4],
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Сб', style=days[5],
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')],

                [InlineKeyboardButton(text='⬅️ Пред неделя',
                                      callback_data=f'date_{day - 7}.{month}'),
                 InlineKeyboardButton(text='➡️ След неделя',
                                      callback_data=f'date_{day + 7}.{month}')]
            ]
        ),

        'en': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Mon', style=days[0],
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Tue', style=days[1],
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Wed', style=days[2],
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='Thr', style=days[3],
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Fri', style=days[4],
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Sat', style=days[5],
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')],

                [InlineKeyboardButton(text='⬅️ Prev week',
                                      callback_data=f'date_{day - 7}.{month}'),
                 InlineKeyboardButton(text='➡️ Next week',
                                      callback_data=f'date_{day + 7}.{month}')]
            ]
        ),

        'zh': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='星期一', style=days[0],
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期二', style=days[1],
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期三', style=days[2],
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='星期四', style=days[3],
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期五', style=days[4],
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期六 ', style=days[5],
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')],

                [InlineKeyboardButton(text='⬅️ 上週',
                                      callback_data=f'date_{day - 7}.{month}'),
                 InlineKeyboardButton(text='➡️ 下週',
                                      callback_data=f'date_{day + 7}.{month}')]
            ]
        )
    }
    return week

choose_language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🇷🇺 Русский', callback_data='select_ru')],
        [InlineKeyboardButton(text='🇬🇧 English', callback_data='select_en')],
        [InlineKeyboardButton(text='🇨🇳 中國人', callback_data='select_zh')]
    ]
)

menu = {
    'ru_menu': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🗓 Мое расписание')],
            [KeyboardButton(text='🔗 Сократить ссылку'), KeyboardButton(text='🔖 Сделать QR')],
            [KeyboardButton(text='🗺 Карта ПГНИУ')],
            [KeyboardButton(text='⚙️ Настройки'), KeyboardButton(text='ℹ️ О боте')]
        ],
        resize_keyboard=True
    ),

    'en_menu': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🗓 My timetable')],
            [KeyboardButton(text='🔗 Shorten link'), KeyboardButton(text='🔖 Create QR-Code')],
            [KeyboardButton(text='🗺 Map of PSU')],
            [KeyboardButton(text='⚙️ Settings'), KeyboardButton(text='ℹ️ About the bot')]
        ],
        resize_keyboard=True
    ),

    'zh_menu': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🗓 我的日程安排')],
            [KeyboardButton(text='🔗 縮短鏈接'), KeyboardButton(text='🔖 製作二維碼')],
            [KeyboardButton(text='🗺 地圖')],
            [KeyboardButton(text='⚙️ 設定'), KeyboardButton(text='ℹ️ 關於機器人')]
        ],
        resize_keyboard=True
    )
}

cancel = {
    'ru': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='❌ Отмена')]
        ],
        resize_keyboard = True
    ),

    'en': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='❌ Cancel')]
        ],
        resize_keyboard = True
    ),

    'zh': ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='❌ 取消')]
        ],
        resize_keyboard = True
    )
}

settings = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚩 Поменять язык', callback_data='change_lg_ru')],
            [InlineKeyboardButton(text='🔗 Поменять ссылку', callback_data='change_link_ru')]
        ]
    ),

    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚩 Change language', callback_data='change_lg_en')],
            [InlineKeyboardButton(text='🔗 Change link', callback_data='change_link_en')]
        ]
    ),

    'zh': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🚩 更改語言', callback_data='change_lg_zh')],
            [InlineKeyboardButton(text='🔗 更改鏈接', callback_data='change_link_zh')]
        ]
    )
}

work = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Клик',
                                  url='https://t.me/lupiktg?text=Привет,%20я%20из%20PSU%20Bot.%20Нужна%20помощь')]
        ]
    ),

    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Click",
                                  url='https://t.me/lupiktg?text=Hello,%20I%20from%20PSU%20Bot.%20Need%20help')]
        ]
    ),

    'zh': InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='點選',
                                  url='https://t.me/lupiktg?text=Hello,%20I%20from%20PSU%20Bot.%20Need%20help')]
        ]
    )
}

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💬 Рассылка', callback_data='mailing')],
        [InlineKeyboardButton(text='📄 Скачать БД', callback_data='download_bd')],
        [InlineKeyboardButton(text='📊 Статистика', callback_data='check_statistics')]
    ]
)

skip_or_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Skip')],
        [KeyboardButton(text='❌ Отмена')]
    ],
    resize_keyboard=True
)

is_good_message = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅Отправить')],
        [KeyboardButton(text='❌ Отмена')]
    ],
    resize_keyboard=True
)

select_statistics = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сегодняшняя активность', callback_data='stats:today')],
        [InlineKeyboardButton(text='Пользователи', callback_data='stats:usage')],
        [InlineKeyboardButton(text='Новые пользователи', callback_data='stats:new_users')]
    ]
)

statistics_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='stats:usage')],
        [InlineKeyboardButton(text='Новые пользователи', callback_data='stats:new_users')]
    ]
)

statistics_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сегодняшняя активность', callback_data='stats:today')],
        [InlineKeyboardButton(text='Пользователи', callback_data='stats:usage')]
    ]
)

statistics_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сегодняшняя активность', callback_data='stats:today')],
        [InlineKeyboardButton(text='Новые пользователи', callback_data='stats:new_users')]
    ]
)