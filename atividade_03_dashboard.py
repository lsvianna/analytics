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

# COMPONENTES
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# TODO 1: # Carregue o arquivo dados_simulados.csv.
df =
# TODO 2: # Converta a coluna timestamp para datetime.

# TODO 3: # Complete a lista com os sensores que poderão ser selecionados.
sensores = 

# INSTÂNCIA DO APP
app = Dash(__name__)

# LAYOUT
app.layout = html.Div([
    html.H2('Dashboard Interativo de Sensores'),

    html.P(
        'Selecione um sensor para visualizar seus valores '
        'ao longo do tempo.'
    ),

    html.Label('Sensor:'),

    # TODO 4: Crie um dropdown para selecionar o sensor. Utilize a lista sensores para criar as opções.

    # TODO 5: Crie um gráfico com um componente que receberá o gráfico gerado pelo callback.
])

# CALLBACK
@app.callback(
    Output('grafico-sensor', 'figure'),
    Input('dropdown-sensor', 'value')
)
def atualizar_grafico(sensor):

    # TODO 6: Crie o gráfico de linha usando timestamp no eixo X e o sensor selecionado no eixo Y.
    fig = 

    return fig

# EXECUÇÃO
if __name__ == '__main__':
    app.run(debug=True)
