import json
import os
import math
import socket
from jinja2 import Environment, FileSystemLoader
from more_itertools import chunked
from livereload import Server
from decouple import config


META_FILE = config('META_FILE', default='static/meta_data.json')
TEMPLATE_FILE = config('TEMPLATE_FILE', default='index.html')
PAGES_DIR = config('PAGES_DIR', default='pages')
BOOKS_PER_PAGE = config('BOOKS_PER_PAGE', default=10, cast=int)
BOOKS_PER_ROW = config('BOOKS_PER_ROW', default=2, cast=int)
DEFAULT_PORT = config('PORT', default=5500, cast=int)


def render_pages(meta_file, template_file, pages_dir):
    """Генерация HTML-страниц с книгами по страницам"""
    with open(meta_file, 'r', encoding='utf-8') as f:
        books = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    total_pages = math.ceil(len(books) / BOOKS_PER_PAGE)
    pages_books = list(chunked(books, BOOKS_PER_PAGE))

    os.makedirs(pages_dir, exist_ok=True)

    for page_number, page_books in enumerate(pages_books, start=1):
        books_chunks = list(chunked(page_books, BOOKS_PER_ROW))

        rendered = template.render(
            books_chunks=books_chunks,
            page_number=page_number,
            total_pages=total_pages
        )

        output_file = (
            'index.html'
            if page_number == 1
            else os.path.join(pages_dir, f'index{page_number}.html')
        )

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered)


def find_free_port(start_port=5500, max_tries=100):
    """Поиск свободного порта начиная с start_port"""
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("Не удалось найти свободный порт.")


def main():
    """Основная функция запуска генерации и сервера"""
    render_pages(META_FILE, TEMPLATE_FILE, PAGES_DIR)

    port = find_free_port(DEFAULT_PORT)

    server = Server()
    server.watch('templates/*.html', lambda: render_pages(META_FILE, TEMPLATE_FILE, PAGES_DIR))
    server.watch(META_FILE, lambda: render_pages(META_FILE, TEMPLATE_FILE, PAGES_DIR))
    server.serve(root='.', port=port, host='127.0.0.1')


if __name__ == '__main__':
    main()