from simulator import BlackHoleRenderer


def create(
    mass=10,
    spin=0.7,
    particles=250,
    speed=5,
):

    renderer = BlackHoleRenderer(
        mass=mass,
        spin=spin,
        particles=particles,
        speed=speed,
    )

    fig = renderer.create_figure(
        "Kerr"
    )

    renderer.add_event_horizon(fig)

    renderer.add_photon_ring(fig)

    renderer.add_disk(fig)

    renderer.add_ergosphere(fig)

    renderer.add_particles(fig)

    renderer.add_labels(
        fig,
        disk=True,
        ergosphere=True,
    )

    renderer.add_legend(
        fig,
        disk=True,
        ergosphere=True,
    )

    return fig
