from simulator import BlackHoleRenderer

renderer = BlackHoleRenderer()


def create():

    fig = renderer.create_figure("Schwarzschild Black Hole")

    # -----------------------------
    # Background
    # -----------------------------

    renderer.add_starfield(fig)

    # -----------------------------
    # Event Horizon
    # -----------------------------

    renderer.add_event_horizon(fig)

    # -----------------------------
    # Photon Ring
    # -----------------------------

    renderer.add_photon_ring(fig)

    # -----------------------------
    # Orbiting Matter
    # -----------------------------

    renderer.add_particles(
        fig,
        number=220
    )

    # -----------------------------
    # Labels
    # -----------------------------

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

        x=1.6,
        y=1.45,

        text="Photon Ring",

        showarrow=True,

        arrowhead=2,

        font=dict(
            color="gold",
            size=11
        )

    )

    # -----------------------------
    # Legend
    # -----------------------------

    renderer.add_legend(fig)

    return fig
