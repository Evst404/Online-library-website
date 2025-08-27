# Онлайн-библиотека

<img width="1445" height="896" alt="image" src="https://github.com/user-attachments/assets/dd446b54-a02e-41fb-ada3-5844fc9c0356" />

## Описание проекта
Это статический сайт-библиотека на HTML с использованием Jinja2-шаблонов.  
Сайт отображает книги в виде карточек с изображениями, автором, жанрами и кнопкой «Читать».  
Поддерживается пагинация и полностью оффлайн-работа: все CSS, JS, изображения и файлы книг загружаются локально.

## Как запустить

1. Склонировать проект или скачать архив:
```
git clone https://github.com/evst404/Online-library-website.git
cd Online-library-website
```

2. Установить зависимости:
```
pip install -r requirements.txt
```

3. Создать файл .env в корне проекта с настройками. Пример:
```
META_FILE=static/meta_data.json
TEMPLATE_FILE=index.html
PAGES_DIR=pages
BOOKS_PER_PAGE=10
BOOKS_PER_ROW=2
PORT=5500
```

4. Запустить генерацию страниц и локальный сервер:
```
python render_website.py
```

или через стандартный HTTP-сервер Python:
```
python -m http.server $PORT
```

5. Открыть браузер по адресу:

[ http://127.0.0.1:5500/index.html ](http://127.0.0.1:5500/index.html)


Все ресурсы загружаются локально — интернет не требуется.
[Локальная онлайн-версия (http://127.0.0.1:5500/index.html)](http://127.0.0.1:5500/index.html)  
*(если используете `livereload` или `python -m http.server`, проверьте свой порт — по умолчанию `5500` или `8000`)*

## Основные функции

1. Пагинация с кнопками «Назад», «Вперёд» и номерами страниц.
2. Карточки книг с изображениями, автором, жанрами и ссылкой на чтение.
3. Полностью оффлайн: Bootstrap, jQuery, Popper и CSS подключены локально.
4. Поддержка нескольких страниц (`index2.html`, `index3.html` и т.д.) с правильными относительными путями.
5. Добавление новых книг.

## Ссылка на сайт

GitHub Pages: [https://evst404.github.io/Online-library-website/index.html](https://evst404.github.io/Online-library-website/index.html)
