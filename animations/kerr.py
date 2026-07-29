from simulator import BlackHoleRenderer
import numpy as np

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Kerr Black Hole")

    renderer.add_starfield(fig)

    renderer.add_event_horizon(fig)

    renderer.add_photon_ring(fig)

    renderer.add_disk(fig)

    renderer.add_ergosphere(fig)

    renderer.add_particles(fig, number=260)

    # Frame Dragging
    angles = np.linspace(0, 2*np.pi, 14)

    for a in angles:

        x = 2.7 * np.cos(a)
        y = 2.0 * np.sin(a)

        dx = -0.35 * np.sin(a)
        dy = 0.35 * np.cos(a)

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

    fig.add_annotation(
        x=0,
        y=0,
        text="Event Horizon",
        showarrow=False,
        font=dict(color="white", size=11)
    )

    fig.add_annotation(
        x=2.8,
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

    renderer.add_legend(
        fig,
        disk=True,
        ergosphere=True
    )

    return fig
