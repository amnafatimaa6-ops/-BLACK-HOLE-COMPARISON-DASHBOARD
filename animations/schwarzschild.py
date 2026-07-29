import numpy as np
import plotly.graph_objects as go


def create():

    fig = go.Figure()

    theta = np.linspace(0,2*np.pi,400)

    # Event Horizon
    fig.add_trace(

        go.Scatter(
            x=np.cos(theta),
            y=np.sin(theta),
            fill="toself",
            mode="lines",
            line=dict(color="black",width=3),
            hoverinfo="skip"
        )
    )


    # Photon Ring

    r=1.4

    fig.add_trace(

        go.Scatter(
            x=r*np.cos(theta),
            y=r*np.sin(theta),
            mode="lines",
            line=dict(color="gold",dash="dot")
        )
    )


    # Orbiting particles

    r=3

    angles=np.linspace(0,2*np.pi,120)

    fig.add_trace(

        go.Scatter(
            x=r*np.cos(angles),
            y=r*np.sin(angles),

            mode="markers",

            marker=dict(
                size=4,
                color="white"
            )
        )
    )

    fig.update_layout(
        template="plotly_dark",
        width=320,
        height=320,
        margin=dict(l=0,r=0,t=0,b=0),
        xaxis=dict(visible=False,range=[-5,5]),
        yaxis=dict(visible=False,range=[-5,5],scaleanchor="x")
    )

    return fig
