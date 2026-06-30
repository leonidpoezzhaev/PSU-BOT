TOKEN = '' #insert your bot token here
ADMIN_CHAT = 0 #insert your telegram id here

language = {
    'language_changed':{
        'ru': 'Язык выбран!',
        'en': 'Language selected!',
        'zh': '已選擇語言！'
    },
    'welcome':{
        'ru': 'Добро пожаловать в бота!',
        'en': 'Welcome to the bot!',
        'zh': '歡迎使用機器人！'
    },
    'need_url':{
        'ru': 'Введите ссылку на расписание (iCal):\n\n'
              '<b>Где взять ссылку?</b>\n'
              '<a href="https://student.psu.ru/">Етис</a> -> Мое расписание ->\n'
              'Синхронизация календаря с внешними сервисами <b>показать</b> ->\n'
              'Подписаться -> Скопировать',
        'en': 'Enter the schedule link (iCal):\n\n'
              '<b>Where can I get the link?</b>\n'
              '<a href="https://student.psu.ru/">Etis</a> -> My schedule ->\n'
              'Synchronize your calendar with external services <b>show</b> ->\n'
              'Subscribe -> Copy',
        'zh': '輸入課程表連結（iCal）：\n\n'
              '<b>在哪裡可以找到連結？ </b>\n'
              '<a href="https://student.psu.ru/">埃蒂斯</a> -> 我的課程表 ->\n'
              '將您的行事曆與外部服務同步 <b>顯示</b> ->\n'
              '訂閱 -> 複製'
    },
    'link_added':{
        'ru': 'Ссылка успешно добавлена!\n\n'
              'Чтобы посмотреть расписание, нажмите по соответствующей кнопке.',
        'en': 'Link successfully added!\n\n'
              'To view the schedule, click the corresponding button.',
        'zh': '連結已成功加入！ \n\n'
              '要查看日程安排，請點擊相應的按鈕。'
    },
    'link_error':{
        'ru': 'Ошибка. Пожалуйста, отправьте ссылку заново.',
        'en': 'Error. Please resubmit the link.',
        'zh': '錯誤。請重新提交連結。'
    },
    'days':{
        'ru': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'zh': ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    },
    'loading':{
        'ru': 'Загружаю расписание...',
        'en': 'Loading timetable...',
        'zh': '裝載計劃表...'
    },
    'put_cut_url':{
        'ru': 'Введите ссылку, которую нужно сократить:',
        'en': 'Enter the link you want to shorten:',
        'zh': '請輸入您要縮短的連結：'
    },
    'by_psu_bot':{
        'ru': 'Сделано в <a href="t.me/PSUstudent_bot">🎓PSU Bot</a>',
        'en': 'Made in <a href="t.me/PSUstudent_bot">🎓PSU Bot</a>',
        'zh': '製造於 <a href="t.me/PSUstudent_bot">🎓PSU Bot</a>'
    },
    'put_qr_url':{
        'ru': 'Введите ссылку/текст для генерации QR-Кода:',
        'en': 'Enter link/text to generate QR-Code:',
        'zh': '輸入連結/文字以產生二維碼：'
    },
    'qr_error':{
        'ru': 'Ошибка генерации.\n\n''Введите текст/ссылку длиной менее <code>1165</code> символов.\n\n',
        'en': 'Generation error.\n\n''Enter text/link less than <code>1165</code> characters long.\n\n',
        'zh': '產生錯誤。\n\n請輸入長度少於<code>1165</code>個字元的文字/連結。\n\n'
    },
    'profile':{
        'ru': '👤 Профиль',
        'en': '👤 Profile',
        'zh': '👤 我的個人資料'
    },
    'language':{
        'ru': '🇷🇺 Язык:',
        'en': '🇬🇧 Language:',
        'zh': '🇨🇳 語言:'
    },
    'link':{
        'ru': '🔗 Ссылка:',
        'en': '🔗 Link:',
        'zh': '🔗 連結:'
    },
    'about_bot':{
        'ru': '<b>🤖 PSU Bot</b> · <code>v1.0</code>\n\n'
              ''
              '<b>👤 Разработка</b>\n'
              '├ <b>Разработчик:</b> @lupiktg\n'
              '└ <b>Муза:</b> @fofisofia8\n\n'
              ''
              '<b>⚙️ Технологии</b>\n'
              '├ <b>Язык:</b> Python 3.14\n'
              '├ <b>Фреймворк:</b> Aiogram 3.25\n'
              '└ <b>БД:</b> SQLite\n\n'
              ''
              '<b>🧾 Контакты</b>\n'
              '└ <b>ТГ Канал:</b> @psustudentru\n\n'
              ''
              '<b>📚 Библиотеки</b>\n'
              '<blockquote>aiogram, aiosqlite, aiohttp, asyncio, langid, icalendar, calendar, datetime, qrcode, io, matplotlib, pandas</blockquote>\n\n'
              ''
              '<tg-spoiler>Нужен свой бот Telegram или решение лабораторной задачи? Жми по кнопке ниже, сделаю быстро и за приемлемую цену.</tg-spoiler>',

        'en': '<b>🤖 PSU Bot</b> · <code>v1.0</code>\n\n'
              ''
              '<b>👤 Development</b>\n'
              '├ <b>Developer:</b> @lupiktg\n'
              '└ <b>Muse:</b> @fofisofia8\n\n'
              ''
              '<b>⚙️ Technologies</b>\n'
              '├ <b>Language:</b> Python 3.14\n'
              '├ <b>Framework:</b> Aiogram 3.25\n'
              '└ <b>DB:</b> SQLite\n\n'
              ''
              '<b>🧾 Contacts</b>\n'
              '└ <b>TG Channel:</b> @psustudenten\n\n'
              ''
              '<b>📚 Libraries</b>\n'
              '<blockquote>aiogram, aiosqlite, aiohttp, asyncio, langid, icalendar, calendar, datetime, qrcode, io, matplotlib, pandas</blockquote>\n\n'
              '<tg-spoiler>Need your own Telegram bot or a lab problem solution? Click the button below, I will get it done quickly and at a reasonable price.</tg-spoiler>',

        'zh': '<b>🤖 PSU Bot</b> · <code>v1.0</code>\n\n'
              ''
              '<b>👤 开发</b>\n'
              '├ <b>開發者:</b> @lupiktg\n'
              '└ <b>缪斯女神:</b> @fofisofia8\n\n'
              ''
              '<b>⚙️ 技术</b>\n'
              '├ <b>语言:</b> Python 3.14\n'
              '├ <b>框架:</b> Aiogram 3.25\n'
              '└ <b>数据库:</b> SQLite\n\n'
              ''
              '<b>🧾 聯絡方式</b>\n'
              '└ <b>TG 頻道:</b> @psustudentzh\n\n'
              ''
              '<b>📚 库</b>\n'
              '<blockquote>aiogram, aiosqlite, aiohttp, asyncio, langid, icalendar, calendar, datetime, qrcode, io, matplotlib, pandas</blockquote>\n\n'
              '<tg-spoiler>需要客製化 Telegram 機器人或解決實驗室問題？點擊下方按鈕；我會快速且有效率地完成，價格合理。</tg-spoiler>'
    },
    'new_language':{
        'ru': 'Выберите новый язык:',
        'en': 'Select a new language:',
        'zh': '選擇一種新語言: '
    },
    'new_link':{
        'ru': 'Введите новую ссылку:',
        'en': 'Enter a new link:',
        'zh': '輸入新連結：'
    }
}

weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']