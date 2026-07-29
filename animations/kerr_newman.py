import numpy as np
import plotly.graph_objects as go


def create():

    fig=go.Figure()

    theta=np.linspace(0,2*np.pi,400)

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

    # Disk

    fig.add_trace(

        go.Scatter(

            x=3*np.cos(theta),

            y=.8*np.sin(theta),

            mode="lines",

            line=dict(color="cyan")

        )
    )

    # Electric field

    for a in np.linspace(0,2*np.pi,18):

        fig.add_trace(

            go.Scatter(

                x=[np.cos(a),4*np.cos(a)],

                y=[np.sin(a),4*np.sin(a)],

                mode="lines",

                line=dict(color="deepskyblue",dash="dot")

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
