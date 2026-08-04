from simulator import BlackHoleRenderer


def create(
    mass=10,
    charge=0.2,
    particles=250,
    speed=5,
):

    renderer = BlackHoleRenderer(
        mass=mass,
        charge=charge,
        particles=particles,
        speed=speed,
    )

    fig = renderer.create_figure(
        "Reissner–Nordström"
    )

    renderer.add_event_horizon(fig)

    renderer.add_photon_ring(fig)

    renderer.add_electric_field(fig)

    renderer.add_particles(fig)

    renderer.add_labels(
        fig,
        electric=True,
    )

    renderer.add_legend(
        fig,
        electric=True,
    )

    return fig
