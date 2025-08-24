import json
import os
import math
import socket
from jinja2 import Environment, FileSystemLoader
from more_itertools import chunked
from livereload import Server

TEMPLATE_FILE = 'index.html'
BOOKS_PER_PAGE = 10
BOOKS_PER_ROW = 2
PAGES_DIR = 'pages'
DEFAULT_PORT = 5500

os.makedirs(PAGES_DIR, exist_ok=True)

def render_pages():
    """Генерируем страницы с книгами по страницам."""
    with open('static/meta_data.json', 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(TEMPLATE_FILE)

    total_pages = math.ceil(len(books) / BOOKS_PER_PAGE)
    pages_books = list(chunked(books, BOOKS_PER_PAGE))

    for i, page_books in enumerate(pages_books, start=1):
        books_chunks = list(chunked(page_books, BOOKS_PER_ROW))

        rendered = template.render(
            books_chunks=books_chunks,
            page_number=i,
            total_pages=total_pages
        )

        output_file = 'index.html' if i == 1 else os.path.join(PAGES_DIR, f'index{i}.html')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered)

        print(f"[INFO] Сгенерирована страница {output_file}")

    print(f"[INFO] Всего сгенерировано {total_pages} страниц.")

def find_free_port(start_port=5500, max_tries=100):
    """Ищем свободный порт, начиная с start_port."""
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("Не удалось найти свободный порт.")

if __name__ == '__main__':
    render_pages()

    port = find_free_port(DEFAULT_PORT)
    if port != DEFAULT_PORT:
        print(f"[INFO] Порт {DEFAULT_PORT} занят, используем свободный порт {port}")

    server = Server()
    server.watch('templates/*.html', render_pages)
    server.watch('static/meta_data.json', render_pages)
    server.serve(root='.', port=port, host='127.0.0.1')