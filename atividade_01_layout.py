"""
Atividade 1: Tela inicial de um dashboard industrial

Objetivo:
Criar a página inicial de um dashboard de monitoramento de sensores.

Requisitos:
1. Criar um título principal.
2. Criar um parágrafo explicando o objetivo do dashboard.
3. Criar uma lista em Markdown com os sensores monitorados.
"""

# COMPONENTES
from dash import Dash, html, dcc

# TODO 1: Criar um título principal.

# TODO 2: 2. Criar um parágrafo explicando o objetivo do dashboard.

# TODO 3: Criar uma lista em Markdown com os sensores monitorados.

# INSTÂNCIA DO APP
app = Dash(__name__)

# LAYOUT
app.layout = html.Div([
    titulo,
    descricao,
    sensores_markdown,
])

# EXECUÇÃO
if __name__ == '__main__':
    app.run(debug=True)
