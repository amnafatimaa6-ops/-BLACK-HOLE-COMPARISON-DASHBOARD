import numpy as np
import plotly.graph_objects as go


def create():

    fig=go.Figure()

    theta=np.linspace(0,2*np.pi,400)

    # Horizon

    fig.add_trace(

        go.Scatter(
            x=np.cos(theta),
            y=np.sin(theta),
            fill="toself",
            mode="lines",
            line=dict(color="black",width=3)
        )
    )

    # Ergosphere

    fig.add_trace(

        go.Scatter(

            x=1.7*np.cos(theta),
            y=1.3*np.sin(theta),

            mode="lines",

            line=dict(color="orange")
        )
    )

    # Accretion Disk

    disk=np.linspace(0,2*np.pi,250)

    fig.add_trace(

        go.Scatter(

            x=3*np.cos(disk),
            y=.8*np.sin(disk),

            mode="lines",

            line=dict(color="cyan")
        )
    )

    fig.update_layout(

        template="plotly_dark",

        width=320,
        height=320,

        margin=dict(l=0,r=0,t=0,b=0),

        xaxis=dict(range=[-5,5],visible=False),

        yaxis=dict(range=[-5,5],visible=False,scaleanchor="x")

    )

    return fig
