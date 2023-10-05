# task_for_UpTrader

<h1 align="center"><a target="_blank" href="">Тестовое задание для UpTrader</a></h1>

### Задание
#### Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

#### Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
#### {% draw_menu 'main_menu' %}
#### При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


### Запуск проекта
#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```

### Запуск на локальной машине:
#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

### Для запуска в Docker:
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd docker
```

### Перед запуском сервера, необходимо создать .env
### Ниже представлены параметры по умолчанию.
```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=app_username
POSTGRES_PASSWORD=uptrader
POSTGRES_DB=app_db
DJANGO_SETTINGS_MODULE=menu.settings
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Создайте суперпользователя Django для входа в админку:
```bash
docker-compose exec backend python manage.py createsuperuser
```

#### После успешной сборки, на сервере выполните команды (только после первого деплоя):
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

#### Теперь по адресу http://localhost:8000/admin/ доступна админка.

