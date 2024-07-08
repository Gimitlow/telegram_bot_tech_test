import os
import uuid

#импорт библиотеки для работы с YooMoney
from yoomoney import Authorize, Quickpay
#библиотека для работы с виртуальным окружением
from dotenv import load_dotenv

#импорт переменных среды из .env
load_dotenv()

RECEIVER = os.getenv('RECEIVER')
REDIRECT_URL = os.getenv('REDIRECT_URL')
PAYMENT_SUM = os.getenv('PAYMENT_SUM')

class YooMoneyIntegration:

    #получение ссылки на оплату сервиса
    async def get_order() -> None:
        
        payment_id = uuid.uuid4()

        #формирование перевода
        payment = Quickpay(
            receiver="410019014512803",
            quickpay_form="shop",
            targets="Тех тест бот",
            paymentType="SB",
            sum=PAYMENT_SUM,
            label=payment_id,
            successURL=REDIRECT_URL
        )
        
        return payment.redirected_url, PAYMENT_SUM

    #можно было бы дописать функцию проверки платежа, но в тех задании не было сказано про проверку платежа
    #как вариант реализации запуск второго потока через библиотеку multiprocessing, в котором будет осуществляться
    #проверка платежа по id lable