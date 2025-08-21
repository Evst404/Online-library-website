import json
from jinja2 import Environment, FileSystemLoader

# Загружаем метаданные
with open('static/meta_data.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')

output = template.render(books=books)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("Сайт успешно сгенерирован!")