import plotly.graph_objs as go
import pandas as pd

# Prepare data for Argentina similar to Brasil
argentina_series = df.loc['Argentina', anos]
argentina_dict = {'ano': argentina_series.index.tolist(), 'imigrantes': argentina_series.values.tolist()}
dados_argentina = pd.DataFrame(argentina_dict)

# Garantir que a coluna 'ano' seja do tipo numérico (int)
dados_brasil['ano'] = dados_brasil['ano'].astype(int)
dados_argentina['ano'] = dados_argentina['ano'].astype(int)

# Criando uma figura
fig = go.Figure()

# Adicionando a linha inicial com o primeiro ponto do Brasil
fig.add_trace(
    go.Scatter(x=[dados_brasil['ano'].iloc[0]], y=[dados_brasil['imigrantes'].iloc[0]], mode='lines', name='Imigrantes do Brasil', line=dict(width=4))
)

# Adicionando a linha inicial com o primeiro ponto da Argentina
fig.add_trace(
    go.Scatter(x=[dados_argentina['ano'].iloc[0]], y=[dados_argentina['imigrantes'].iloc[0]], mode='lines', name='Imigrantes da Argentina', line=dict(width=4))
)

# Definindo as configurações de layout
fig.update_layout(
    title=dict(
        text='<b>Imigração do Brasil e da Argentina para o Canadá no período de 1980 a 2013</b>',
        x=0.1,
        font=dict(size=18)
    ),
    xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Ano</b>'),
    yaxis=dict(range=[0, 3000], autorange=False, title='<b>Número de imigrantes</b>'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': False}, 'fromcurrent': True}]
        )]
    )],
    width=1200,
    height=600
)

# Definindo as configurações de animação
frames = []
for i in range(len(dados_brasil)):
    frame_data = [
        go.Scatter(x=list(dados_brasil['ano'].iloc[:i+1]), y=list(dados_brasil['imigrantes'].iloc[:i+1]), name='Imigrantes do Brasil', mode='lines', line=dict(width=4)),
        go.Scatter(x=list(dados_argentina['ano'].iloc[:i+1]), y=list(dados_argentina['imigrantes'].iloc[:i+1]), name='Imigrantes da Argentina', mode='lines', line=dict(width=4))
    ]
    frame = go.Frame(data=frame_data)
    frames.append(frame)
fig.frames = frames

# Mostrando a figura
fig.show()
