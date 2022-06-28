# Descrição

Projeto realizado em Python para gerar dinamicamente relatórios em formato .pdf através de dados estruturados (ex: JSON) e templates definidos em HTML e estilizados em CSS.

# Aplicação

A aplicação deste projeto foi utilizada para a geração de um currículo.

# Estrutura dos dados

Os dados foram estruturados em sete categorias primárias: 
- <ins>pessoal</ins>: dados pessoais, como: nome, e-mail, link para redes sociais, e outras informações;
- <ins>formacao-academica</ins>: informações relativas a formação acadêmica, dispostas em formato de lista;
- <ins>qualificacoes</ins>: informações relativas a conhecimentos técnicos, dispostas em formato de lista e categorizados;
- <ins>idiomas</ins>: informações relativas a idiomas, dispostas em formato de lista;
- <ins>certificados</ins>: informações relativas a certificados, dispostas em formato de lista;
- <ins>experiencia</ins>: informações relativas a experiência profissional, dispostas em formato de lista;
- <ins>projetos</ins>: informações relativas a projetos selecionados, dispostas em formato de lista.

Foram criadas seções para cada uma destas categorias no template HTML, de forma a posicionar os elementos nas posições desejadas e estilizá-los. Os elementos dispostos em listas são populados automaticamente em _loops for_, através do módulo Jinja2.

O template HTML deve ser construído de acordo com cada caso, de forma a acomodar os dados na página, tanto em posicionamento quanto estilo.

# Tecnologias utilizadas

- Python - linguagem de programação;
- HTML - linguagem de marcação;
- CSS - linguagem de estilo;
- JSON - formato para armazenagem de dados;
- Principais ferramentas/bibliotecas:
    - WeasyPrint - ferramenta para renderizar documentos HTML e CSS e exportá-los para o formato pdf;
    - Jinja2 - mecanismo para criação de templates.
