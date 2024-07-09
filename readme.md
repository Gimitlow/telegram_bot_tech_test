# О проекте
Набор кнопок с демонстрацией возможностей aiogram

# Как запустить 
* Клонируем проект и устанавливаем requirements
```
git clone https://github.com/Gimitlow/telegram_bot_tech_test.git
pip install -r requirements.txt
```
* Перетаскиваем файл с JSON настройками сервисного аккаунта Google Clloud Console в корневую папку проекта. ВНИМАНИЕ! Для редактирования таблицы сервисным аккаунтом, ему должны быть расширены права до редактора, через Поделиться в Google Sheets. Также должны быть настроены права в Google Cloud Console.

* Создаем .env файл и записываем туда следующие переменные
```
#общие настройки   
TOKEN='' #токен бота

#настройки логгера (можно не менять)
FILELOG='logs.txt'
FORMAT='%(asctime)s %(message)s'
DATETIME='%Y-%m-%d %H:%M:%S'    

#настройка интеграции с yoomoney
RECEIVER='' #номер счета
PAYMENT_SUM=2 #сумма
REDIRECT_URL='' #ссылка для редиректа после оплаты

#настрокий для googleAPI
GOOGLE_JSON_NAME='' #название файла json c настройками сервисного аккаунта
SHEET_ID='' #id таблицы
```

* Запускаем проект
```
python app.py
```

# Обратная связь

[Написать в телеграм](https://t.me/mad_CatLon)