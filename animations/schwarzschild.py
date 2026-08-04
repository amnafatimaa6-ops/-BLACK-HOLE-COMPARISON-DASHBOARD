from simulator import BlackHoleRenderer


def create(
    mass=10,
    particles=250,
    speed=5,
):

    renderer = BlackHoleRenderer(
        mass=mass,
        particles=particles,
        speed=speed,
    )

    fig = renderer.create_figure(
        "Schwarzschild"
    )

    renderer.add_event_horizon(fig)
    renderer.add_photon_ring(fig)
    renderer.add_particles(fig)

    renderer.add_labels(fig)

    renderer.add_legend(fig)

    return fig
