import logging
import os

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types
from aiogram.types import FSInputFile

#иморт кнопок
from bot.markups.image_markup import ImageButtons

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:image')

class ImageHandler:

    #получить фотографию
    @router.callback_query(F.data == 'get_image')
    async def get_image(callback: types.CallbackQuery) -> None:

        #удаляем предидущее сообщение
        await callback.message.delete()

        #получаем путь текущей папки
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Путь к изображению, находящемуся в директории выше
        image_path = os.path.join(current_dir, '..', '..', 'images' ,'test.jpg')

        #конвертирование для отправки через бота
        photo = FSInputFile(image_path)

        #отправка фото
        await callback.message.answer_photo(
            photo=photo,
            caption='Получай картинку!',
            reply_markup=await ImageButtons.get_image()
        )
