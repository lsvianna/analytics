"""
Atividade 2: Callback textual com Dash

Objetivo:
Criar uma aplicação em que o usuário digita o nome de um sensor
e o sistema retorna uma explicação sobre ele.

Sensores possíveis:
- sensor_temp
- sensor_pressao
- sensor_vibracao
"""

# ==========================
# 📦 COMPONENTES
# ==========================
from dash import Dash, html, dcc, Input, Output

# TODO 1:
# Complete as descrições dos sensores.
descricoes = {
    'sensor_temp': 'TODO: descreva o sensor de temperatura.',
    'sensor_pressao': 'TODO: descreva o sensor de pressão.',
    'sensor_vibracao': 'TODO: descreva o sensor de vibração.'
}

titulo = html.H2('Consulta de Sensores Industriais')

descricao = html.P(
    'Digite o nome de um sensor para visualizar sua descrição.'
)

# TODO 2:
# Confira o id do campo de entrada.
# Ele será usado como Input no callback.
campo_sensor = dcc.Input(
    id='input-sensor',
    type='text',
    placeholder='Exemplo: sensor_temp'
)

# TODO 3:
# Confira o id da área de saída.
# Ele será usado como Output no callback.
saida = html.Div(id='saida-descricao')

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

    html.Label('Sensor:'),
    campo_sensor,

    html.Br(),
    html.Br(),

    saida
])

# ==========================
# 🔁 CALLBACK
# ==========================
@app.callback(
    Output('saida-descricao', 'children'),
    Input('input-sensor', 'value')
)
def consultar_sensor(sensor):

    # TODO 4:
    # Teste a aplicação sem digitar nada e observe esta mensagem.
    if not sensor:
        return 'Digite o nome de um sensor.'

    sensor = sensor.strip()

    # TODO 5:
    # Verifique se o sensor digitado existe no dicionário.
    if sensor in descricoes:
        return descricoes[sensor]

    # TODO 6:
    # Personalize a mensagem para sensores não encontrados.
    return 'Sensor não encontrado. Tente: sensor_temp, sensor_pressao ou sensor_vibracao.'

# ==========================
# 🚀 EXECUÇÃO
# ==========================
if __name__ == '__main__':
    app.run(debug=True)
