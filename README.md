# Бот Python Meetup Bot

Бот по проекту Devman.

## Запуск:

Python3 должен быть уже установлен.
* Скачайте код
* Установите зависимости  
```pip install -r requirements.txt```
* Запустите бот командой  
```python3 manage.py bot```
На команду `/hello` должен отреагировать, значит проект развернулся, все ок.

## Переменные окружения

Для корректной работы кода необходимо указать переменные окружения. Для этого создайте файл `.env` рядом с `manage.py` и запишите туда следующие обязательные переменые:
* `TELEGRAM_API_KEY` - Токен ключ бота в Телеграм.
* `DJANGO_SECRET_KEY` - Секретный ключ Django.


## Внимание django-admin-shortcuts==2.0 
Библиотека имеет конфликт с django версией 4, чтобы все работало необходимо самому поравить библиотеку, как в пул реквесте по [ссылке](https://github.com/alesdotio/django-admin-shortcuts/pull/40/commits/9fa4c1e7349a0da4dcbb77ec3aef19cd0f4be8d5)