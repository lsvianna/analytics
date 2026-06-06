"""
Atividade 1: Tela inicial de um dashboard industrial

Objetivo:
Criar a página inicial de um dashboard de monitoramento de sensores.

Requisitos:
1. Criar um título principal.
2. Criar um parágrafo explicando o objetivo do dashboard.
3. Criar uma lista em Markdown com os sensores monitorados.
4. Criar um texto curto explicando como o dashboard pode apoiar a decisão.
"""

# ==========================
# 📦 COMPONENTES
# ==========================
from dash import Dash, html, dcc

# TODO 1:
# Substitua o texto abaixo por um título adequado para o dashboard.
titulo = html.H1('TODO: título do dashboard')

# TODO 2:
# Substitua o texto abaixo por uma descrição do objetivo do dashboard.
descricao = html.P(
    'TODO: escreva aqui o objetivo do dashboard.'
)

# TODO 3:
# Complete a lista de sensores monitorados.
sensores_markdown = dcc.Markdown(
    """
    **Sensores monitorados:**

    - TODO
    - TODO
    - TODO
    """
)

# TODO 4:
# Explique, em poucas linhas, como esse dashboard pode apoiar a decisão.
utilidade_markdown = dcc.Markdown(
    """
    **Utilidade para a gestão:**

    TODO: explique como a visualização dos sensores pode apoiar
    o acompanhamento do processo industrial.
    """
)

# ==========================
# INSTÂNCIA DO APP
# ==========================
app = Dash(__name__)

# ==========================
# 🎨 LAYOUT
# ==========================
app.layout = html.Div([
    titulo,
    descricao,
    sensores_markdown,
    utilidade_markdown
])

# ==========================
# 🚀 EXECUÇÃO
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
