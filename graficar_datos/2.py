import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import time

# Definir los datos
x = np.linspace(0, 10, 100)
y = np.sin(x)
frames = []

# Crear los frames para la animación
for i in range(100):
    frames.append(go.Frame(data=[go.Scatter(x=x, y=np.sin(x + i / 10))]))

# Configurar la figura y la animación
fig = go.Figure(
    data=[go.Scatter(x=x, y=y)],
    layout=go.Layout(
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[-1, 1]),
        title="Animación con Plotly",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None, {"frame": {"duration": 50, "redraw": True},
                                                     "fromcurrent": True}])])]
    ),
    frames=frames
)

# Mostrar la animación
fig.show()
