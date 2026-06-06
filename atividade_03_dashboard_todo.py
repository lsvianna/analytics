"""
Atividade 3: Dashboard interativo de sensores

Objetivo:
Criar um dashboard que permita selecionar um sensor industrial
e visualizar sua evolução ao longo do tempo.

Arquivo utilizado:
dados_simulados.csv

Colunas principais:
- timestamp
- sensor_temp
- sensor_pressao
- sensor_vibracao
- status
"""

# ==========================
# 📦 COMPONENTES
# ==========================
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# TODO 1:
# Carregue o arquivo dados_simulados.csv.
df = pd.read_csv('dados_simulados.csv')

# TODO 2:
# Converta a coluna timestamp para datetime.
df['timestamp'] = pd.to_datetime(df['timestamp'])

# TODO 3:
# Complete a lista com os sensores que poderão ser selecionados.
sensores = [
    'sensor_temp',
    'sensor_pressao',
    'sensor_vibracao'
]

# ==========================
# INSTÂNCIA DO APP
# ==========================
app = Dash(__name__)

# ==========================
# 🎨 LAYOUT
# ==========================
app.layout = html.Div([
    html.H2('Dashboard Interativo de Sensores'),

    html.P(
        'Selecione um sensor para visualizar seus valores '
        'ao longo do tempo.'
    ),

    html.Label('Sensor:'),

    # TODO 4:
    # Verifique como as opções do dropdown são criadas a partir da lista sensores.
    dcc.Dropdown(
        id='dropdown-sensor',
        options=[
            {'label': sensor.replace('_', ' ').title(), 'value': sensor}
            for sensor in sensores
        ],
        value='sensor_temp',
        clearable=False
    ),

    # TODO 5:
    # Este componente receberá o gráfico gerado pelo callback.
    dcc.Graph(id='grafico-sensor')
])

# ==========================
# 🔁 CALLBACK
# ==========================
@app.callback(
    Output('grafico-sensor', 'figure'),
    Input('dropdown-sensor', 'value')
)
def atualizar_grafico(sensor):

    # TODO 6:
    # Crie o gráfico de linha usando timestamp no eixo X
    # e o sensor selecionado no eixo Y.
    fig = px.line(
        df,
        x='timestamp',
        y=sensor,
        title=f'Evolução Temporal - {sensor.replace("_", " ").title()}',
        labels={
            'timestamp': 'Tempo',
            sensor: 'Leitura do Sensor'
        }
    )

    return fig

# ==========================
# 🚀 EXECUÇÃO
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
