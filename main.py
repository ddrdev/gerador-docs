from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime
from typing import Dict, List
import locale
from pathlib import Path
import os
import qrcode

def convert_date(value : str) -> str:
    return datetime.strptime(value, "%B de %Y").strftime("%b/%Y") if value else "Presente"

def date_format(value : Dict) -> str:
    return f'{convert_date(value["inicio"])} - {convert_date(value["fim"])}' if isinstance(value, dict) else convert_date(value)

def concat_items(values : List, sep : str = ", ") -> str:
    return sep.join(values)

def generate_qrcode(url : str) -> None:
    qr = qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qrcode_path = Path('qrcode')
    qrcode_path.mkdir(exist_ok=True)
    filename = 'qrcode.png'
    img.save(qrcode_path / filename)

def main() -> None:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    input_path = Path('data.json')
    output_path = Path('output')
    
    resume_url = 'https://github.com/ddrdev/gerador-docs'

    with open(input_path, 'r', encoding="utf-8") as input_file:
        data = json.load(input_file)

        output_name = f'CV_{data["pessoal"]["nome"].replace(" ","_")}.pdf'

        loader = FileSystemLoader('templates')
        env = Environment(loader=loader)

        env.filters["date_format"] = date_format
        env.filters["concat_items"] = concat_items

        template = env.get_template('template.html')
        css_template = env.get_template('style.css')

        gen_date=datetime.today().strftime("%d de %B de %Y às %H:%M:%S")

        generate_qrcode(resume_url)

        page = template.render(data=data)
        stylesheet = css_template.render(gen_date=gen_date)

        base_url = os.path.dirname(os.path.realpath(__file__))

        html = HTML(string=page, base_url=base_url)
        style = CSS(string=stylesheet)

        pdf = html.write_pdf(target = None, stylesheets = [style])

        output_path.mkdir(exist_ok=True)

        with open(output_path / output_name, 'wb') as output_file:
            output_file.write(pdf)

if __name__ == '__main__':
    main()