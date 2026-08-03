from simulator import BlackHoleRenderer
import numpy as np


def create(
    mass=10,
    spin=0.7,
    charge=0,
    particles=250,
    speed=5
):

    renderer = BlackHoleRenderer(
        mass=mass,
        spin=spin,
        charge=charge,
        particles=particles,
        speed=speed
    )

    fig = renderer.create_figure("Kerr Black Hole")

    # -----------------------------------
    # Background
    # -----------------------------------

    renderer.add_starfield(fig)

    # -----------------------------------
    # Event Horizon
    # -----------------------------------

    renderer.add_event_horizon(fig)

    # -----------------------------------
    # Photon Ring
    # -----------------------------------

    renderer.add_photon_ring(fig)

    # -----------------------------------
    # Accretion Disk
    # -----------------------------------

    renderer.add_disk(fig)

    # -----------------------------------
    # Ergosphere
    # -----------------------------------

    renderer.add_ergosphere(fig)

    # -----------------------------------
    # Orbiting Matter
    # -----------------------------------

    renderer.add_particles(fig)

    # -----------------------------------
    # Frame Dragging
    # -----------------------------------

    radius = 2.3 + spin

    angles = np.linspace(0, 2 * np.pi, 16)

    for angle in angles:

        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        dx = -0.35 * np.sin(angle)
        dy = 0.35 * np.cos(angle)

        fig.add_annotation(

            x=x + dx,
            y=y + dy,

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

    # -----------------------------------
    # Labels
    # -----------------------------------

    fig.add_annotation(

        x=0,
        y=0,

        text="Event Horizon",

        showarrow=False,

        font=dict(
            color="white",
            size=12
        )

    )

    fig.add_annotation(

        x=3.3,
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
        y=2.3,

        text="Ergosphere",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="orange",
            size=11
        )

    )

    fig.add_annotation(

        x=-3.2,
        y=-2.5,

        text="Frame Dragging",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="lime",
            size=11
        )

    )

    # -----------------------------------
    # Legend
    # -----------------------------------

    renderer.add_legend(

        fig,

        disk=True,

        ergosphere=True

    )

    return fig
