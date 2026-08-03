import numpy as np
import plotly.graph_objects as go


class BlackHoleRenderer:

    def __init__(
        self,
        mass=10,
        spin=0.7,
        charge=0.2,
        particles=250,
        speed=5
    ):

        self.mass = mass
        self.spin = spin
        self.charge = charge
        self.particles = particles
        self.speed = speed

        self.theta = np.linspace(
            0,
            2*np.pi,
            500
        )


    # ======================================
    # Figure Setup
    # ======================================

    def create_figure(self, title):

        fig = go.Figure()


        fig.update_layout(

            title=dict(
                text=title,
                x=0.5
            ),

            template="plotly_dark",

            paper_bgcolor="#010409",

            plot_bgcolor="#010409",


            width=450,

            height=450,


            margin=dict(
                l=10,
                r=10,
                t=50,
                b=10
            ),


            xaxis=dict(
                visible=False,
                range=[
                    -6,
                    6
                ]
            ),


            yaxis=dict(
                visible=False,
                range=[
                    -6,
                    6
                ],
                scaleanchor="x"
            )

        )


        return fig



    # ======================================
    # Star Field
    # ======================================

    def add_starfield(
        self,
        fig,
        number=150
    ):

        np.random.seed(42)


        x=np.random.uniform(
            -6,
            6,
            number
        )

        y=np.random.uniform(
            -6,
            6,
            number
        )


        fig.add_trace(

            go.Scatter(

                x=x,

                y=y,

                mode="markers",

                marker=dict(

                    color="white",

                    size=np.random.uniform(
                        1,
                        3,
                        number
                    )

                ),

                hoverinfo="skip"

            )

        )



    # ======================================
    # Event Horizon
    # ======================================

    def add_event_horizon(
        self,
        fig
    ):


        radius = 1 + (
            self.mass/100
        )


        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(
                    self.theta
                ),

                y=radius*np.sin(
                    self.theta
                ),

                fill="toself",

                fillcolor="black",

                line=dict(
                    color="white",
                    width=2
                ),

                hoverinfo="skip"

            )

        )



    # ======================================
    # Photon Ring
    # ======================================

    def add_photon_ring(
        self,
        fig
    ):


        radius=1.45


        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(
                    self.theta
                ),

                y=radius*np.sin(
                    self.theta
                ),

                mode="lines",

                line=dict(

                    color="gold",

                    width=3

                )

            )

        )



    # ======================================
    # Accretion Disk
    # ======================================

    def add_disk(
        self,
        fig
    ):


        radius=3.2


        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(
                    self.theta
                ),

                y=0.7*radius*np.sin(
                    self.theta
                ),

                mode="lines",

                line=dict(

                    color="cyan",

                    width=5

                )

            )

        )



    # ======================================
    # Ergosphere
    # ======================================

    def add_ergosphere(
        self,
        fig
    ):


        radius=2


        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(
                    self.theta
                ),

                y=1.4*np.sin(
                    self.theta
                ),

                mode="lines",

                line=dict(

                    color="orange",

                    dash="dash",

                    width=2

                )

            )

        )



    # ======================================
    # Electric Field
    # ======================================

    def add_electric_field(
        self,
        fig
    ):


        angles=np.linspace(
            0,
            2*np.pi,
            20
        )


        for angle in angles:


            fig.add_trace(

                go.Scatter(

                    x=[
                        np.cos(angle),
                        4*np.cos(angle)
                    ],

                    y=[
                        np.sin(angle),
                        4*np.sin(angle)
                    ],

                    mode="lines",

                    line=dict(

                        color="deepskyblue",

                        dash="dot"

                    )

                )

            )



    # ======================================
    # Particles
    # ======================================

    def add_particles(
        self,
        fig
    ):


        angles=np.random.uniform(
            0,
            2*np.pi,
            self.particles
        )


        radius=np.random.uniform(
            2,
            5,
            self.particles
        )


        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(
                    angles
                ),

                y=radius*np.sin(
                    angles
                ),

                mode="markers",

                marker=dict(

                    color="white",

                    size=3

                )

            )

        )



    # ======================================
    # Legend
    # ======================================

    def add_legend(
        self,
        fig,
        disk=False,
        ergosphere=False,
        electric=False
    ):


        text="""

<b>Legend</b><br>

⚫ Event Horizon<br>

🟡 Photon Ring<br>

⚪ Matter Particles<br>

"""


        if disk:

            text += "🔵 Accretion Disk<br>"


        if ergosphere:

            text += "🟠 Ergosphere<br>"


        if electric:

            text += "⚡ Electric Field"


        fig.add_annotation(

            x=5,

            y=5,

            text=text,

            showarrow=False,

            bgcolor="rgba(0,0,0,0.6)"

        )


        return fig
