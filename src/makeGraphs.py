import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='username', api_key='api_key')

avengers = go.Bar(
            x=['12AM - 4AM', '4AM - 8AM', '8AM - 12PM', '12PM - 4PM', '4PM - 8PM', '8PM - 12PM'],
            y=[121814, 101952, 117898, 151041, 134535, 103584],
        name='Avengers',
        marker=dict(
        color='rgb(102, 0, 0)'
    )
    )

gameofthrones = go.Bar(
            x=['12AM - 4AM', '4AM - 8AM', '8AM - 12PM', '12PM - 4PM', '4PM - 8PM', '8PM - 12PM'],
            y=[52152, 31008, 30496, 34854, 33021, 25392],
            name='Game of Thrones',
            marker=dict(
            color='rgb(26, 118, 255)'
    )
    )

unknown = go.Bar(
            x=['12AM - 4AM', '4AM - 8AM', '8AM - 12PM', '12PM - 4PM', '4PM - 8PM', '8PM - 12PM'],
            y=[213696, 157710, 173116, 224533, 205114, 158295],
            name='Unknown',
            marker=dict(
            color='rgb(16, 150, 200)'
    )
    )


data = [avengers, gameofthrones, unknown]
layout = go.Layout(
    title='GoT vs AVg',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Viewers (millions)',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='style-bar')
#py.iplot(data, filename='basic-bar')
