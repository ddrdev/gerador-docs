from fileinput import filename
from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime
from typing import Dict, List
import locale
from pathlib import Path

def main() -> None:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    input_path = Path('data.json')
    output_path = Path('output')
    output_name = 'CV.pdf'

    with open(input_path, 'r', encoding="utf-8") as input_file:
        data = json.load(input_file)

        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)

        template = env.get_template('template.html')

        page = template.render(data=data)

        html = HTML(string=page)

        pdf = html.write_pdf(target=None)

        output_path.mkdir(exist_ok=True)

        with open(output_path / output_name, 'wb') as output_file:
            output_file.write(pdf)

if __name__ == '__main__':
    main()