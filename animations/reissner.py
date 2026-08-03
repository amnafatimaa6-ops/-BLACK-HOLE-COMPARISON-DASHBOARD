from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go


def create(
    mass=10,
    spin=0,
    charge=0.2,
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

    fig = renderer.create_figure("Reissner–Nordström Black Hole")

    # ----------------------------------------
    # Background
    # ----------------------------------------

    renderer.add_starfield(fig)

    # ----------------------------------------
    # Event Horizon
    # ----------------------------------------

    renderer.add_event_horizon(fig)

    # ----------------------------------------
    # Photon Ring
    # ----------------------------------------

    renderer.add_photon_ring(fig)

    # ----------------------------------------
    # Electric Field
    # ----------------------------------------

    renderer.add_electric_field(fig)

    # ----------------------------------------
    # Charged Particles
    # ----------------------------------------

    angles = np.random.uniform(0, 2*np.pi, particles)

    radius = np.random.uniform(2.0, 5.0, particles)

    particle_size = 3 + charge * 4

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(

                size=particle_size,

                color="deepskyblue",

                opacity=0.9

            ),

            hoverinfo="skip"

        )

    )

    # ----------------------------------------
    # Labels
    # ----------------------------------------

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

        x=1.6,
        y=1.5,

        text="Photon Ring",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="gold",
            size=11
        )

    )

    fig.add_annotation(

        x=4.3,
        y=2.2,

        text=f"Electric Field (Q={charge:.2f})",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="deepskyblue",
            size=11
        )

    )

    # ----------------------------------------
    # Legend
    # ----------------------------------------

    renderer.add_legend(

        fig,

        electric=True

    )

    return fig
