import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
from g4f.client import Client
import time
import sys
import threading
import re
import requests

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

def check_internet_connection(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def loading_animation():
    chars = "|/-\\"
    while not stop_loading:
        for char in chars:
            if stop_loading:
                break
            sys.stdout.write(f"\r{char}  Думаем над '{userinput}'  {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * len(f"{char}  Думаем над '{userinput}'  {char}") + "\r")

def has_russian_chars(text):
    return bool(re.search('[а-яА-Я]', text))

async def fetch_response(client, pretext, userinput):
    response = await asyncio.to_thread(
        client.chat.completions.create,
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pretext + userinput}]
    )
    return response.choices[0].message.content

async def main():
    global stop_loading
    global userinput

    while True:
        client = Client()
        userinput = input("Деталь: ")

        if not check_internet_connection():
            print("Нет подключения к интернету. Проверьте соединение и попробуйте снова.")
            continue

        pretext = """
        Переведи ответ на русский язык,
        Если вопрос не связан с инструментами или автомобильной тематикой, отвечай на него одной строчкой - "Затрудняюсь ответить на этот вопрос" 
        Не указывай источники и ссылки,
        Не делай текст жирным,
        В ответе должно быть 3 строчки:
        1. Описание товара: (Тут должно быть описание товара)
        2. Применяется в автомобилях: (Тут должна быть марка авто)
        3. Другие названия запчасти: (Тут должны быть другие названия запчасти)
        Для всех пунктов изучи источники и дай ответ.
        Пиши ответ в таком формате как я описал 1. Описание товара: ответ, 2. Применяется в автомобилях: ответ, 3. Другие названия запчасти: ответ. с пунктами.
        Не используй форматирование по типу ###,** и так далее
        после написания третьего пункта не пиши ничего, мне нужно только 3 пункта
        Вопрос: """

        while True:
            stop_loading = False
            loading_thread = threading.Thread(target=loading_animation)
            loading_thread.start()

            try:
                try:
                    response = await asyncio.wait_for(fetch_response(client, pretext, userinput), timeout=20)
                except asyncio.TimeoutError:
                    stop_loading = True
                    loading_thread.join()
                    sys.stdout.write("\r" + " " * len(f"  Думаем над '{userinput}'  ") + "\r")
                    print("Ожидайте, система перегружена запросами")
                    continue

                content = response
                if has_russian_chars(content):
                    stop_loading = True
                    loading_thread.join()
                    sys.stdout.write("\r" + " " * len(f"  Думаем над '{userinput}'  ") + "\r")
                    print(content)
                    break
            finally:
                stop_loading = True
                loading_thread.join()

if __name__ == "__main__":
    asyncio.run(main())
