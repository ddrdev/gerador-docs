from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime
from typing import Dict, List
import locale

def main() -> None:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    filedir = './data.json'

    with open(filedir, 'r', encoding="utf-8") as input_file:
        data = json.load(input_file)

if __name__ == '__main__':
    main()