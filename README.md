# Асинхронный бот для описания инструментов

## Описание

Этот проект представляет собой асинхронный инструмент командной строки, который используется для получения описаний автомобильных инструментов и запчастей на русском языке. Бот поддерживает проверку интернет-соединения, асинхронную обработку запросов и отображает анимацию загрузки в процессе выполнения.

## Ввод -> Вывод (Пример)

Деталь: свеча зажигания
1.Описание товара: Свеча зажигания — это электрическое устройство для зажигания топливной смеси в двигателе.
2.Применяется в автомобилях: Применяется в автомобилях различных марок.
3.Другие названия запчасти: Искровая свеча, зажигалка.

## Особенности

- **Асинхронная обработка:** Эффективно обрабатывает несколько запросов с использованием библиотеки asyncio в Python.
- **Анимация загрузки:** Отображает анимацию загрузки во время обработки пользовательского ввода.
- **Проверка интернет-соединения:** Предотвращает попытки получения ответов без подключения к интернету.
- **Определение языка:** Гарантирует, что ответ будет на русском языке.
- **Обработка тайм-аутов:** Управляет тайм-аутами ответов для предотвращения зависания программы.

## Требования

- Python 3.x
- Библиотеки: asyncio, g4f, requests, sys, threading, re

## Установка

Для установки необходимых библиотек используйте `pip`:

```bash
pip install asyncio requests g4f
