## Проект «Yatube_API»

Yatube_API — проект, позволяющий пользователям публиковать записи, управлять подписками и взаимодействовать с платформой через программный интерфейс.

### Реализованы возможности

- Создания и управления постами
- Добавления комментариев
- Системы подписок на авторов
- JWT-аутентификации

### Польза проекта

Yatube_API даёт возможность создавать мобильные и веб-приложения для соцсети, используя готовую backend-инфраструктуру без необходимости её изменений.

### Как запустить (установить) проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Valeron006/api_final_yatube-1.git`

`cd api_final_yatube`


Создать и активировать виртуальное окружение:

+ `python -m venv venv`
+ `source venv/Scripts/activate`
+ `python -m pip install --upgrade pip`

Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

Выполнить миграции:

`python manage.py makemigrations`
`python manage.py migrate`


Запустить проект:
`python manage.py runserver`
#### После запуска проекта, документация будет доступна по адресу:
`http://127.0.0.1:8000/redoc/`

#### Примеры запросов:

POST-запрос для получения всех постов.

`GET http://127.0.0.1:8000/api/posts/`

Ответ:

```
[
    {
        "id": 1,
        "author": 1,
        "text": "Мой первый пост!",
        "pub_date": "2023-10-01T12:00:00Z",
        "group": null
    },
    {
        "id": 2,
        "author": 2,
        "text": "Второй пост в группе",
        "pub_date": "2023-10-02T14:30:00Z",
        "group": 1
    }
]
```


POST-запрос, создание группы.

`POST http://127.0.0.1:8000/api/groups/`
"Content-Type: application/json"
'{"title": "Новая группа", "slug": "newgroup", "description": "Описание"}'

Ответ:

```
{
    "id": 2,
    "title": "Новая группа",
    "slug": "newgroup",
    "description": "Описание"
}
```

GET-запрос, все комментарии к посту с id =1.

`GET http://127.0.0.1:8000/api/posts/1/comments/`

```
[
    {
        "id": 1,
        "post": 1,
        "author": 2,
        "text": "Отличный пост!",
        "created": "2023-10-01T12:30:00Z"
    }
]
```

POST-запрос, подписка на пользователя

`POST http://127.0.0.1:8000/api/follow/`
"Content-Type: application/json"
'{"following": 2}'
"Authorization: Token ваш_токен"

Ответ:

```
{
    "id": 2,
    "user": 1,
    "following": 3
}