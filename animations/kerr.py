from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Kerr Black Hole")

    # ------------------------------------------------
    # Background
    # ------------------------------------------------

    renderer.add_starfield(fig)

    # ------------------------------------------------
    # Event Horizon
    # ------------------------------------------------

    renderer.add_event_horizon(fig)

    # ------------------------------------------------
    # Photon Ring
    # ------------------------------------------------

    renderer.add_photon_ring(fig)

    # ------------------------------------------------
    # Accretion Disk
    # ------------------------------------------------

    renderer.add_disk(fig)

    # ------------------------------------------------
    # Ergosphere
    # ------------------------------------------------

    renderer.add_ergosphere(fig)

    # ------------------------------------------------
    # Orbiting Matter
    # ------------------------------------------------

    renderer.add_particles(
        fig,
        number=260
    )

    # ------------------------------------------------
    # Frame Dragging Arrows
    # ------------------------------------------------

    angles = np.linspace(0, 2*np.pi, 12)

    for a in angles:

        x = 2.6*np.cos(a)
        y = 2.1*np.sin(a)

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

    # ------------------------------------------------
    # Labels
    # ------------------------------------------------

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

        x=2.9,
        y=0,

        text="Accretion Disk",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="cyan",
            size=11
        )

    )

    fig.add_annotation(

        x=0,
        y=1.9,

        text="Ergosphere",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="orange",
            size=11
        )

    )

    # ------------------------------------------------
    # Legend
    # ------------------------------------------------

    renderer.add_legend(

        fig,

        disk=True,

        ergosphere=True

    )

    return fig
