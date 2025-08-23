import json
import os
import math
from jinja2 import Environment, FileSystemLoader
from more_itertools import chunked

TEMPLATE_FILE = 'index.html' 
PAGES_DIR = 'pages'
BOOKS_PER_PAGE = 10
BOOKS_PER_ROW = 2

os.makedirs(PAGES_DIR, exist_ok=True)

def render_pages():
    """Генерируем страницы с книгами по страницам"""
    
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

        
        if i == 1:
            output_file = 'index.html'
        else:
            output_file = os.path.join(PAGES_DIR, f'index{i}.html')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(rendered)

    print(f"[INFO] Сгенерировано {total_pages} страниц, index.html в корне, остальные в {PAGES_DIR}/")

if __name__ == '__main__':
    render_pages()