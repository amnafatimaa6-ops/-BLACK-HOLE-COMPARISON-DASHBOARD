from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Kerr-Newman Black Hole")

    # ------------------------------------------
    # Background
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
    # Accretion Disk
    # ------------------------------------------

    renderer.add_disk(fig)

    # ------------------------------------------
    # Ergosphere
    # ------------------------------------------

    renderer.add_ergosphere(fig)

    # ------------------------------------------
    # Electric Field
    # ------------------------------------------

    renderer.add_electric_field(fig)

    # ------------------------------------------
    # Charged Orbiting Particles
    # ------------------------------------------

    angles = np.random.uniform(0, 2*np.pi, 280)
    radius = np.random.uniform(2.2, 4.8, 280)

    colors = np.where(
        np.random.rand(280) > 0.5,
        "cyan",
        "white"
    )

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(

                size=4,

                color=colors,

                opacity=0.9

            ),

            hoverinfo="skip"

        )

    )

    # ------------------------------------------
    # Frame Dragging Arrows
    # ------------------------------------------

    angles = np.linspace(0, 2*np.pi, 14)

    for a in angles:

        x = 2.7*np.cos(a)
        y = 2.0*np.sin(a)

        dx = -0.35*np.sin(a)
        dy = 0.35*np.cos(a)

        fig.add_annotation(

            x=x+dx,
            y=y+dy,

            ax=x,
            ay=y,

            xref="x",
            yref="y",

            axref="x",
            ayref="y",

            showarrow=True,

            arrowhead=3,

            arrowcolor="lime"

        )

    # ------------------------------------------
    # Labels
    # ------------------------------------------

    fig.add_annotation(
        x=0,
        y=0,
        text="Event Horizon",
        showarrow=False,
        font=dict(color="white", size=11)
    )

    fig.add_annotation(
        x=2.9,
        y=0,
        text="Accretion Disk",
        showarrow=True,
        arrowhead=2,
        font=dict(color="cyan", size=11)
    )

    fig.add_annotation(
        x=0,
        y=1.9,
        text="Ergosphere",
        showarrow=True,
        arrowhead=2,
        font=dict(color="orange", size=11)
    )

    fig.add_annotation(
        x=4.3,
        y=2.3,
        text="Electric Field",
        showarrow=True,
        arrowhead=2,
        font=dict(color="deepskyblue", size=11)
    )

    # ------------------------------------------
    # Legend
    # ------------------------------------------

    renderer.add_legend(

        fig,

        disk=True,

        ergosphere=True,

        electric=True

    )

    return fig
