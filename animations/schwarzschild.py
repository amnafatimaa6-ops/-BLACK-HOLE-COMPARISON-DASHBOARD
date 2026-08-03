from simulator import BlackHoleRenderer


def create(
    mass=10,
    spin=0,
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


    fig = renderer.create_figure(
        "Schwarzschild Black Hole"
    )


    # -----------------------------
    # Space Background
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
    # Matter Around Black Hole
    # -----------------------------

    renderer.add_particles(fig)


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
            size=12
        )

    )


    fig.add_annotation(

        x=1.5,
        y=1.2,

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
