Асинхронный бот для описания инструментов
Особенности:
Асинхронная обработка: Эффективно обрабатывает несколько запросов с использованием библиотеки asyncio в Python.
Анимация загрузки: Отображает анимацию загрузки во время обработки пользовательского ввода.
Проверка интернет-соединения: Проверяет наличие интернет-соединения перед попыткой получить ответы.
Определение языка: Гарантирует, что ответ будет на русском языке.
Обработка тайм-аутов: Управляет тайм-аутами ответов, чтобы предотвратить зависание программы.
Требования:
Python 3.x
Библиотеки: asyncio, g4f, requests, sys, threading, re
Установка:
pip install asyncio requests g4f
Основные компоненты кода
Проверка интернет-соединения: Функция check_internet_connection проверяет доступность интернета перед отправкой запроса.
Анимация загрузки: Функция loading_animation отображает анимацию загрузки во время обработки запроса.
Асинхронный запрос: Функция fetch_response выполняет асинхронный запрос к модели ИИ для получения ответа.
Главная функция: Основной цикл программы в функции main обрабатывает ввод пользователя, проверяет соединение, запускает анимацию и отображает ответ.
