from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime
from typing import Dict, List
import locale
from pathlib import Path

def convert_date(value : str) -> str:
    return datetime.strptime(value, "%B de %Y").strftime("%b/%Y") if value else "Presente"

def date_format(value : Dict) -> str:
    return f'{convert_date(value["inicio"])} - {convert_date(value["fim"])}' if isinstance(value, dict) else convert_date(value)

def concat_items(values : List, sep : str = ", ") -> str:
    return sep.join(values)

def main() -> None:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    input_path = Path('data.json')
    output_path = Path('output')
    output_name = 'CV.pdf'

    with open(input_path, 'r', encoding="utf-8") as input_file:
        data = json.load(input_file)

        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)

        env.filters["date_format"] = date_format
        env.filters["concat_items"] = concat_items

        template = env.get_template('template.html')
        css_template = env.get_template('style.css')

        page = template.render(data=data)
        stylesheet = css_template.render()

        html = HTML(string=page)
        style = CSS(string=stylesheet)

        pdf = html.write_pdf(target = None, stylesheets = [style])

        output_path.mkdir(exist_ok=True)

        with open(output_path / output_name, 'wb') as output_file:
            output_file.write(pdf)

if __name__ == '__main__':
    main()