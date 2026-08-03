from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go


def create(
    mass=10,
    spin=0.7,
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

    fig = renderer.create_figure("Kerr–Newman Black Hole")

    # ---------------------------------------
    # Background Stars
    # ---------------------------------------

    renderer.add_starfield(fig)

    # ---------------------------------------
    # Event Horizon
    # ---------------------------------------

    renderer.add_event_horizon(fig)

    # ---------------------------------------
    # Photon Ring
    # ---------------------------------------

    renderer.add_photon_ring(fig)

    # ---------------------------------------
    # Accretion Disk
    # ---------------------------------------

    renderer.add_disk(fig)

    # ---------------------------------------
    # Ergosphere
    # ---------------------------------------

    renderer.add_ergosphere(fig)

    # ---------------------------------------
    # Electric Field
    # ---------------------------------------

    renderer.add_electric_field(fig)

    # ---------------------------------------
    # Orbiting Charged Particles
    # ---------------------------------------

    angles = np.random.uniform(0, 2*np.pi, particles)

    radius = np.random.uniform(2.2, 5.0, particles)

    colors = np.where(
        np.random.rand(particles) > 0.5,
        "cyan",
        "white"
    )

    sizes = 3 + charge * 4

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(

                size=sizes,

                color=colors,

                opacity=0.9

            ),

            hoverinfo="skip"

        )

    )

    # ---------------------------------------
    # Frame Dragging
    # ---------------------------------------

    drag_radius = 2.3 + spin

    frame_angles = np.linspace(0, 2*np.pi, 16)

    for angle in frame_angles:

        x = drag_radius*np.cos(angle)
        y = drag_radius*np.sin(angle)

        dx = -0.35*np.sin(angle)
        dy = 0.35*np.cos(angle)

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

    # ---------------------------------------
    # Labels
    # ---------------------------------------

    fig.add_annotation(
        x=0,
        y=0,
        text="Event Horizon",
        showarrow=False,
        font=dict(color="white", size=12)
    )

    fig.add_annotation(
        x=3.3,
        y=0,
        text="Accretion Disk",
        showarrow=True,
        arrowhead=2,
        font=dict(color="cyan", size=11)
    )

    fig.add_annotation(
        x=0,
        y=2.2,
        text="Ergosphere",
        showarrow=True,
        arrowhead=2,
        font=dict(color="orange", size=11)
    )

    fig.add_annotation(
        x=4.3,
        y=2.2,
        text=f"Electric Field (Q={charge:.2f})",
        showarrow=True,
        arrowhead=2,
        font=dict(color="deepskyblue", size=11)
    )

    fig.add_annotation(
        x=-3.5,
        y=-2.5,
        text=f"Frame Dragging (a={spin:.2f})",
        showarrow=True,
        arrowhead=2,
        font=dict(color="lime", size=11)
    )

    # ---------------------------------------
    # Legend
    # ---------------------------------------

    renderer.add_legend(
        fig,
        disk=True,
        ergosphere=True,
        electric=True
    )

    return fig
