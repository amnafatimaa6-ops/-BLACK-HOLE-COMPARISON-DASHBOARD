from simulator import BlackHoleRenderer
import numpy as np
import plotly.graph_objects as go

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Kerr-Newman Black Hole")

    renderer.add_starfield(fig)

    renderer.add_event_horizon(fig)

    renderer.add_photon_ring(fig)

    renderer.add_disk(fig)

    renderer.add_ergosphere(fig)

    renderer.add_electric_field(fig)

    angles = np.random.uniform(0, 2*np.pi, 300)
    radius = np.random.uniform(2.2, 4.8, 300)

    colors = np.where(
        np.random.rand(300) > .5,
        "white",
        "cyan"
    )

    fig.add_trace(

        go.Scatter(

            x=radius*np.cos(angles),

            y=radius*np.sin(angles),

            mode="markers",

            marker=dict(

                size=4,

                color=colors,

                opacity=.9

            ),

            hoverinfo="skip"

        )

    )

    # Frame dragging
    frame_angles = np.linspace(0, 2*np.pi, 14)

    for a in frame_angles:

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

    fig.add_annotation(
        x=0,
        y=0,
        text="Event Horizon",
        showarrow=False,
        font=dict(color="white")
    )

    fig.add_annotation(
        x=2.9,
        y=0,
        text="Accretion Disk",
        showarrow=True,
        arrowhead=2,
        font=dict(color="cyan")
    )

    fig.add_annotation(
        x=0,
        y=1.9,
        text="Ergosphere",
        showarrow=True,
        arrowhead=2,
        font=dict(color="orange")
    )

    fig.add_annotation(
        x=4.2,
        y=2.2,
        text="Electric Field",
        showarrow=True,
        arrowhead=2,
        font=dict(color="deepskyblue")
    )

    renderer.add_legend(
        fig,
        disk=True,
        ergosphere=True,
        electric=True
    )

    return fig
