import json
from jinja2 import Environment, FileSystemLoader
from more_itertools import chunked  # позволяет делить список на чанки

# Загружаем книги
with open('static/meta_data.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

# Разбиваем книги на чанки по 2
books_chunks = list(chunked(books, 2))

# Настраиваем Jinja2
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')

# Рендерим
output = template.render(books_chunks=books_chunks)

# Сохраняем
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("Сайт успешно сгенерирован!")