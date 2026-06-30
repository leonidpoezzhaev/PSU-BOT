from aiogram.fsm.state import StatesGroup, State

class take_url(StatesGroup):
    lang = State()
    url = State()

class cut_link(StatesGroup):
    lang = State()
    link = State()

class qr_link(StatesGroup):
    lang = State()
    link = State()

class send_message(StatesGroup):
    ru = State()
    en = State()
    zh = State()
    photo = State()
    button = State()
    is_good = State()
