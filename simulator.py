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
            2 * np.pi,
            600
        )

    # ==========================================================
    # Create Figure
    # ==========================================================

    def create_figure(self, title):

        fig = go.Figure()

        fig.update_layout(

            title=dict(
                text=title,
                x=0.5,
                font=dict(
                    size=22,
                    color="white"
                )
            ),

            template="plotly_dark",

            paper_bgcolor="#020617",
            plot_bgcolor="#020617",

            width=500,
            height=500,

            margin=dict(
                l=5,
                r=5,
                t=55,
                b=5
            ),

            xaxis=dict(
                visible=False,
                range=[-6, 6]
            ),

            yaxis=dict(
                visible=False,
                range=[-6, 6],
                scaleanchor="x"
            ),

            showlegend=False

        )

        # Automatically generate the background
        self.add_nebula(fig)
        self.add_galaxy(fig)
        self.add_starfield(fig)

        return fig

    # ==========================================================
    # Star Field
    # ==========================================================

    def add_starfield(
        self,
        fig,
        number=350
    ):

        np.random.seed(42)

        x = np.random.uniform(-6, 6, number)
        y = np.random.uniform(-6, 6, number)

        colours = np.random.choice(

            [
                "white",
                "#D6ECFF",
                "#FFE082",
                "#FFD54F",
                "#90CAF9"
            ],

            number

        )

        sizes = np.random.uniform(
            1,
            3.8,
            number
        )

        opacity = np.random.uniform(
            0.35,
            1,
            number
        )

        fig.add_trace(

            go.Scatter(

                x=x,

                y=y,

                mode="markers",

                marker=dict(

                    color=colours,

                    size=sizes,

                    opacity=opacity

                ),

                hoverinfo="skip"

            )

        )

    # ==========================================================
    # Procedural Nebula
    # ==========================================================

    def add_nebula(self, fig):

        np.random.seed(10)

        nebula_colours = [

            "rgba(70,30,180,0.05)",
            "rgba(0,140,255,0.04)",
            "rgba(0,255,255,0.03)"

        ]

        for colour in nebula_colours:

            x = np.random.normal(
                0,
                2.4,
                1600
            )

            y = np.random.normal(
                0,
                2.4,
                1600
            )

            fig.add_trace(

                go.Scatter(

                    x=x,

                    y=y,

                    mode="markers",

                    marker=dict(

                        size=10,

                        color=colour

                    ),

                    hoverinfo="skip"

                )

            )

    # ==========================================================
    # Procedural Spiral Galaxy
    # ==========================================================

    def add_galaxy(self, fig):

        theta = np.linspace(
            0,
            8 * np.pi,
            2500
        )

        radius = 0.16 * theta

        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        fig.add_trace(

            go.Scatter(

                x=x,

                y=y,

                mode="markers",

                marker=dict(

                    size=1.5,

                    color="rgba(255,255,255,0.10)"

                ),

                hoverinfo="skip"

            )

        )

        # Bright galaxy core

        glow = np.linspace(
            2.5,
            0.3,
            15
        )

        for r in glow:

            fig.add_trace(

                go.Scatter(

                    x=r * np.cos(self.theta),

                    y=r * np.sin(self.theta),

                    fill="toself",

                    fillcolor="rgba(255,255,200,0.015)",

                    line=dict(
                        color="rgba(0,0,0,0)"
                    ),

                    hoverinfo="skip"

                )

            )



    # ==========================================================
    # Event Horizon
    # ==========================================================

    def add_event_horizon(self, fig):

        radius = 1.0 + (self.mass / 100)

        # Outer glow
        for glow_radius in np.linspace(radius + 0.5, radius, 12):

            alpha = 0.015 + (radius + 0.5 - glow_radius) * 0.05

            fig.add_trace(

                go.Scatter(

                    x=glow_radius * np.cos(self.theta),

                    y=glow_radius * np.sin(self.theta),

                    fill="toself",

                    fillcolor=f"rgba(80,180,255,{alpha:.3f})",

                    line=dict(
                        color="rgba(0,0,0,0)"
                    ),

                    hoverinfo="skip",

                    showlegend=False

                )

            )

        # Black hole shadow

        fig.add_trace(

            go.Scatter(

                x=radius * np.cos(self.theta),

                y=radius * np.sin(self.theta),

                fill="toself",

                fillcolor="black",

                line=dict(

                    color="white",

                    width=2

                ),

                hoverinfo="skip",

                showlegend=False

            )

        )


    # ==========================================================
    # Photon Ring
    # ==========================================================

    def add_photon_ring(self, fig):

        radius = 1.45 + self.mass / 300

        glow_layers = [

            (14, 0.03),

            (10, 0.06),

            (6, 0.18),

            (3, 1.0)

        ]

        for width, alpha in glow_layers:

            fig.add_trace(

                go.Scatter(

                    x=radius * np.cos(self.theta),

                    y=radius * np.sin(self.theta),

                    mode="lines",

                    line=dict(

                        color=f"rgba(255,215,0,{alpha})",

                        width=width

                    ),

                    hoverinfo="skip",

                    showlegend=False

                )

            )


    # ==========================================================
    # Accretion Disk
    # ==========================================================

    def add_disk(self, fig):

        disk_radius = 3.3

        flatten = 0.42 + self.spin * 0.45

        # Outer glow

        for width, alpha in [

            (12, 0.05),

            (8, 0.12),

            (5, 1.0)

        ]:

            fig.add_trace(

                go.Scatter(

                    x=disk_radius * np.cos(self.theta),

                    y=flatten * disk_radius * np.sin(self.theta),

                    mode="lines",

                    line=dict(

                        color=f"rgba(0,255,255,{alpha})",

                        width=width

                    ),

                    hoverinfo="skip",

                    showlegend=False

                )

            )


    # ==========================================================
    # Ergosphere
    # ==========================================================

    def add_ergosphere(self, fig):

        radius = 2.0 + self.spin

        fig.add_trace(

            go.Scatter(

                x=radius * np.cos(self.theta),

                y=1.18 * radius * np.sin(self.theta),

                mode="lines",

                line=dict(

                    color="orange",

                    width=3,

                    dash="dash"

                ),

                hoverinfo="skip",

                showlegend=False

            )

        )


    # ==========================================================
    # Electric Field
    # ==========================================================

    def add_electric_field(self, fig):

        total_lines = int(20 + self.charge * 24)

        angles = np.linspace(
            0,
            2 * np.pi,
            total_lines
        )

        for angle in angles:

            start = 1.2

            end = 4.2 + self.charge

            fig.add_trace(

                go.Scatter(

                    x=[

                        start * np.cos(angle),

                        end * np.cos(angle)

                    ],

                    y=[

                        start * np.sin(angle),

                        end * np.sin(angle)

                    ],

                    mode="lines",

                    line=dict(

                        color="#66CCFF",

                        width=2,

                        dash="dot"

                    ),

                    hoverinfo="skip",

                    showlegend=False

                )

            )







    # ==========================================================
    # Orbiting Matter Particles
    # ==========================================================

    def add_particles(self, fig):

        np.random.seed(100)

        angles = np.random.uniform(
            0,
            2*np.pi,
            self.particles
        )

        radius = np.random.uniform(
            2.0,
            5.2,
            self.particles
        )

        colors = np.random.choice(

            [

                "white",

                "#D6ECFF",

                "#FFE082",

                "#90CAF9"

            ],

            self.particles

        )

        sizes = np.random.uniform(
            1.5,
            4,
            self.particles
        )

        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(angles),

                y=radius*np.sin(angles),

                mode="markers",

                marker=dict(

                    color=colors,

                    size=sizes,

                    opacity=0.9

                ),

                hoverinfo="skip",

                showlegend=False

            )

        )


    # ==========================================================
    # Information Labels
    # ==========================================================

    def add_labels(

        self,

        fig,

        disk=False,

        ergosphere=False,

        electric=False

    ):

        fig.add_annotation(

            x=0,

            y=0,

            text="<b>Event Horizon</b>",

            showarrow=False,

            font=dict(

                color="white",

                size=12

            )

        )


        fig.add_annotation(

            x=1.8,

            y=1.5,

            text="Photon Ring",

            showarrow=True,

            arrowhead=2,

            arrowcolor="gold",

            font=dict(

                color="gold",

                size=11

            )

        )


        if disk:

            fig.add_annotation(

                x=3.6,

                y=0,

                text="Accretion Disk",

                showarrow=True,

                arrowhead=2,

                arrowcolor="#00FFFF",

                font=dict(

                    color="#00FFFF",

                    size=11

                )

            )


        if ergosphere:

            fig.add_annotation(

                x=0,

                y=2.6,

                text="Ergosphere",

                showarrow=True,

                arrowhead=2,

                arrowcolor="orange",

                font=dict(

                    color="orange",

                    size=11

                )

            )


        if electric:

            fig.add_annotation(

                x=4.5,

                y=2.8,

                text=f"Electric Field (Q={self.charge:.2f})",

                showarrow=True,

                arrowhead=2,

                arrowcolor="#66CCFF",

                font=dict(

                    color="#66CCFF",

                    size=11

                )

            )


    # ==========================================================
    # Scientific Legend
    # ==========================================================

    def add_legend(

        self,

        fig,

        disk=False,

        ergosphere=False,

        electric=False

    ):

        legend = """

<b>Legend</b>

<br><br>

⚫ Event Horizon

<br>

🟡 Photon Ring

<br>

⭐ Matter Particles

"""

        if disk:

            legend += """

<br>

🔵 Accretion Disk

"""

        if ergosphere:

            legend += """

<br>

🟠 Ergosphere

"""

        if electric:

            legend += """

<br>

⚡ Electric Field

"""

        fig.add_annotation(

            x=5.4,

            y=5.5,

            text=legend,

            showarrow=False,

            align="left",

            font=dict(

                color="white",

                size=11

            ),

            bgcolor="rgba(0,0,0,0.60)",

            bordercolor="#38BDF8",

            borderwidth=1

        )


    # ==========================================================
    # Optional Orbit Animation
    # ==========================================================

    def orbit_frame(

        self,

        angle,

        radius

    ):

        x = radius*np.cos(angle)

        y = radius*np.sin(angle)

        return x, y

            )
