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

# COMPONENTES
from dash import Dash, html, dcc, Input, Output

# TODO 1:
# Complete o dicionário com o sensor e suas descrições.
descricoes = {

}

titulo = html.H2('Consulta de Sensores Industriais')

descricao = html.P(
    'Digite o nome de um sensor para visualizar sua descrição.'
)

# TODO 2: Utilize um campo de entrada (dcc.Input) para o usuário digitar o nome do sensor.
# Atente-se ao id do campo de entrada.
campo_sensor = 

# TODO 3: Crie uma área de saída (html.Div) para exibir a descrição do sensor.
# Atente-se ao id da área de saída.
saida = 

# INSTÂNCIA DO APP
app = Dash(__name__)

# LAYOUT
app.layout = html.Div([
    titulo,
    descricao,

    html.Label('Sensor:'),
    campo_sensor,

    html.Br(),
    html.Br(),

    saida
])


# CALLBACK
@app.callback(
    Output('saida-descricao', 'children'),
    Input('input-sensor', 'value')
)
def consultar_sensor(sensor):

    # TODO 4: Utilize uma condicional para verificar se o campo de entrada está vazio.
    # Teste a aplicação sem digitar nada e observe esta mensagem.

    sensor = sensor.strip()

    # TODO 5: Utilize uma condicional para verificar se o sensor digitado existe no dicionário.
    # Verifique se o sensor digitado existe no dicionário.

    # TODO 6: Retorne a descrição do sensor utilizando o dicionário. Teste a aplicação digitando os nomes dos sensores.

# EXECUÇÃO
if __name__ == '__main__':
    app.run(debug=True)
