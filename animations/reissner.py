from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Reissner–Nordström")

    renderer.add_starfield(fig)

    renderer.add_event_horizon(fig)

    renderer.add_photon_ring(fig)

    renderer.add_electric_field(fig)

    # Charged particles
    angles = np.random.uniform(0, 2*np.pi, 220)
    radius = np.random.uniform(2.2, 4.8, 220)

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(
                size=4,
                color="deepskyblue",
                opacity=.9
            ),

            hoverinfo="skip"

        )

    )

    fig.add_annotation(
        x=0,
        y=0,
        text="Event Horizon",
        showarrow=False,
        font=dict(color="white")
    )

    fig.add_annotation(
        x=4.3,
        y=2.2,
        text="Electric Field",
        showarrow=True,
        arrowhead=2,
        font=dict(color="deepskyblue")
    )

    fig.add_annotation(
        x=1.7,
        y=1.5,
        text="Photon Ring",
        showarrow=True,
        arrowhead=2,
        font=dict(color="gold")
    )

    renderer.add_legend(
        fig,
        electric=True
    )

    return fig
