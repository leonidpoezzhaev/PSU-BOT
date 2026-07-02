from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime

async def generate_week_keyboard(day, month, year):
    weekday = datetime(year, month, day).isoweekday()
    
    week = {
        'ru': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Пн',
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Вт',
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Ср',
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='Чт',
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Пт',
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Сб',
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')]
            ]
        ),

        'en': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Mon',
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Tue',
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Wed',
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='Thr',
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Fri',
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='Sat',
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')]
            ]
        ),

        'zh': InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='星期一',
                                      callback_data=f'date_{day + (1 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期二',
                                      callback_data=f'date_{day + (2 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期三',
                                      callback_data=f'date_{day + (3 - weekday)}.{month}')],

                [InlineKeyboardButton(text='星期四',
                                      callback_data=f'date_{day + (4 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期五',
                                      callback_data=f'date_{day + (5 - weekday)}.{month}'),
                 InlineKeyboardButton(text='星期六 ',
                                      callback_data=f'date_{day + (6 - weekday)}.{month}')]
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