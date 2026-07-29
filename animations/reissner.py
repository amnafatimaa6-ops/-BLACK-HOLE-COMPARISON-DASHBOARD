from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Reissner–Nordström Black Hole")

    # ------------------------------------------
    # Background Stars
    # ------------------------------------------

    renderer.add_starfield(fig)

    # ------------------------------------------
    # Event Horizon
    # ------------------------------------------

    renderer.add_event_horizon(fig)

    # ------------------------------------------
    # Photon Ring
    # ------------------------------------------

    renderer.add_photon_ring(fig)

    # ------------------------------------------
    # Electric Field
    # ------------------------------------------

    renderer.add_electric_field(fig)

    # ------------------------------------------
    # Charged Particles
    # ------------------------------------------

    angles = np.random.uniform(0, 2*np.pi, 220)
    radius = np.random.uniform(2.0, 4.8, 220)

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(

                size=4,

                color="deepskyblue",

                opacity=0.9

            ),

            hoverinfo="skip"

        )

    )

    # ------------------------------------------
    # Labels
    # ------------------------------------------

    fig.add_annotation(

        x=0,
        y=0,

        text="Event Horizon",

        showarrow=False,

        font=dict(
            color="white",
            size=11
        )

    )

    fig.add_annotation(

        x=4.2,
        y=2.2,

        text="Electric Field",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="deepskyblue",
            size=11
        )

    )

    fig.add_annotation(

        x=1.7,
        y=1.5,

        text="Photon Ring",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="gold",
            size=11
        )

    )

    # ------------------------------------------
    # Legend
    # ------------------------------------------

    renderer.add_legend(

        fig,

        electric=True

    )

    return fig
