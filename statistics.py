import aiosqlite
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

matplotlib.use('Agg')

async def new_request(type, id):
    time = str(datetime.now()).split()[0]
    id = str(id)

    async with aiosqlite.connect('psu.db') as db:
        async with db.execute(f'SELECT {type}, users, use_bot FROM statistics WHERE date = ?', (time,)) as cur:
            date = await cur.fetchone()

        if date is None:
            await db.execute(f'INSERT INTO statistics (date, {type}, use_bot, users) VALUES (?, ?, ?, ?)', (time, 1, 1, id))
            await db.commit()
        else:
            countt = int(date[0]) + 1
            users = str(date[1])
            use_bot = int(date[2])

            await db.execute(f'UPDATE statistics SET {type} = ? WHERE date = ?', (countt, time))
            await db.commit()

            if id not in users:
                users = users + ';' + id
                await db.execute(f'UPDATE statistics SET use_bot = ?, users = ? WHERE date = ?', (use_bot+1, users, time))
                await db.commit()


async def generate_diagram(diagram_type: str) -> BytesIO:
    async with aiosqlite.connect('psu.db') as db:
        async with db.execute('SELECT date, use_bot, timetable, cut_link, make_qr, check_map, new_users FROM statistics') as cur:
            rows = await cur.fetchall()

    columns = ['date', 'use_bot', 'timetable', 'cut_link', 'make_qr', 'check_map', 'new_users']
    df = pd.DataFrame(rows, columns=columns)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    img_stream = BytesIO()

    if diagram_type == 'today':
        today = pd.Timestamp.now().normalize()
        today_data = df[df['date'] == today]
        command_cols = ['timetable', 'cut_link', 'make_qr', 'check_map']

        if today_data.empty:
            plt.figure(figsize=(6, 6))
            plt.text(0.5, 0.5, "Нет данных за сегодня", ha='center', va='center', fontsize=14)
            plt.title(f"Статистика за {today.strftime('%Y-%m-%d')}")
        else:
            totals = today_data[command_cols].sum()
            if totals.sum() == 0:
                plt.figure(figsize=(6, 6))
                plt.text(0.5, 0.5, "Сегодня команды не использовались", ha='center', va='center', fontsize=14)
                plt.title(f"Статистика за {today.strftime('%Y-%m-%d')}")
            else:
                non_zero = totals[totals > 0]
                plt.figure(figsize=(6, 6))
                plt.pie(non_zero, labels=non_zero.index, autopct='%1.1f%%', startangle=90)
                plt.title(f"Использование команд за {today.strftime('%Y-%m-%d')}")

    elif diagram_type == 'new_users':
        if df.empty or df['new_users'].sum() == 0:
            plt.figure(figsize=(10, 5))
            plt.text(0.5, 0.5, "Нет данных о новых пользователях", ha='center', va='center', fontsize=14)
            plt.title("Новые пользователи по дням")
        else:
            plt.figure(figsize=(10, 5))
            plt.plot(df['date'], df['new_users'], marker='s', linestyle='-', color='g', linewidth=2)
            plt.xlabel('Дата')
            plt.ylabel('Новых пользователей')
            plt.title('Ежедневный прирост новых пользователей')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            plt.tight_layout()

    elif diagram_type == 'usage':
        if df.empty or df['use_bot'].sum() == 0:
            plt.figure(figsize=(10, 5))
            plt.text(0.5, 0.5, "Нет данных об использовании бота", ha='center', va='center', fontsize=14)
            plt.title("Использование бота по дням")
        else:
            plt.figure(figsize=(10, 5))
            plt.plot(df['date'], df['use_bot'], marker='o', linestyle='-', color='b', linewidth=2)
            plt.xlabel('Дата')
            plt.ylabel('Количество использований')
            plt.title('Ежедневное использование бота')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            plt.tight_layout()

    else:
        raise ValueError("Недопустимый тип диаграммы. Используйте 'today', 'new_users' или 'usage'.")

    plt.savefig(img_stream, format='png', dpi=100, bbox_inches='tight')
    plt.close()
    img_stream.seek(0)

    return img_stream