#импортируем классы состояний
from aiogram.fsm.state import StatesGroup, State

#создаем описание модели состояния для нашего хендлера обработки входящей даты от пользователя
class DataFromUser(StatesGroup):
    date = State()