import json
import os
from jinja2 import Environment, FileSystemLoader
from livereload import Server

TEMPLATE_FILE = 'template.html'
OUTPUT_FILE = 'index.html'

def on_reload():
    """Рендерим шаблон template.html в index.html"""
    # Загружаем книги
    with open('static/meta_data.json', 'r', encoding='utf-8') as f:
        books = json.load(f)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(TEMPLATE_FILE)
    rendered = template.render(books=books)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(rendered)
    
    print(f"[INFO] Сгенерирован {OUTPUT_FILE} с {len(books)} книгами")

# Запуск livereload сервера
server = Server()
server.watch('templates/*.html', on_reload)      
server.watch('static/meta_data.json', on_reload) 
server.serve(root='.', port=5500, host='127.0.0.1')