# test-chat
## Тестовое задание - Простой чат
- Позволяет вести приватную переписку с другими пользователями
- Поиск собеседника по никнейму
- При регистрации проверяет никнейм на занятость
- Интерфейс администратора

Проект в сети - https://boiling-bastion-95643.herokuapp.com/

## Подготовка рабочей среды
Перейдите в свою рабочую директорию и выполните следующие команды:
```
git clone https://github.com/avcherezov/test-chat.git
cd test-chat
```
Создайте и активируйте виртуальное окружение:
```
source -m venv venv
source venv/Scripts/activate
```
Установите необходимые зависимости:
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Создайте суперпользователя:
```
python manage.py createsuperuser
```
Запустите сервер разработки:
```
python manage.py runserver
```

## Стэк
Django, PostgreSQL, Gunicorn, Heroku
