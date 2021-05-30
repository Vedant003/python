import plotly.graph_objects as go
import plotly.offline as pyo
#This is Comment
#Error
#Error
categories = ['Damage', 'Fire Rate', 'Range',
              'Recoil', 'Bullet Speed']
categories = [*categories, categories[0]]

AWM = [100, 85, 100, 56, 91]
M24 = [89, 80, 93, 53, 79]
Kar98K = [81, 90,  80, 50, 76]


AWM = [*AWM, AWM[0]]
M24 = [*M24, M24[0]]
Kar98K = [*Kar98K, Kar98K[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=AWM, theta=categories, fill='toself', name='AWM'),
        go.Scatterpolar(r=M24, theta=categories, fill='toself', name='M24'),
        go.Scatterpolar(r=Kar98K, theta=categories,
                        fill='toself', name='Kar98K')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Snipers Comparsion'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)
pyo.plot(fig)
