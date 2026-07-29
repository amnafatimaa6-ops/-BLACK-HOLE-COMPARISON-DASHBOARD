import numpy as np
import plotly.graph_objects as go


class BlackHoleRenderer:

    def __init__(self):

        self.theta = np.linspace(0, 2*np.pi, 500)

    # -------------------------------------------------------
    # Layout
    # -------------------------------------------------------

    def create_figure(self, title=""):

        fig = go.Figure()

        fig.update_layout(

            template="plotly_dark",

           paper_bgcolor="#010409",
           plot_bgcolor="#010409",

            width=350,
            height=350,

            margin=dict(
                l=5,
                r=5,
                t=35,
                b=5
            ),

            title=title,

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

        return fig

    # -------------------------------------------------------
    # Star Field
    # -------------------------------------------------------

    def add_starfield(self, fig, n=120):

        np.random.seed(42)

        x = np.random.uniform(-6, 6, n)
        y = np.random.uniform(-6, 6, n)

        sizes = np.random.uniform(1, 3, n)

        fig.add_trace(

            go.Scatter(

                x=x,
                y=y,

                mode="markers",

                marker=dict(

                    color="white",

                    size=sizes,

                    opacity=.8

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Event Horizon
    # -------------------------------------------------------

    def add_event_horizon(self, fig):

        x = np.cos(self.theta)
        y = np.sin(self.theta)

        fig.add_trace(

            go.Scatter(

                x=x,

                y=y,

                fill="toself",

                mode="lines",

                fillcolor="black",

                line=dict(

                    color="white",

                    width=2

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Photon Ring
    # -------------------------------------------------------

    def add_photon_ring(self, fig):

        r = 1.35

        fig.add_trace(

            go.Scatter(

                x=r*np.cos(self.theta),

                y=r*np.sin(self.theta),

                mode="lines",

                line=dict(

                    color="gold",

                    width=3

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Accretion Disk
    # -------------------------------------------------------

    def add_disk(self, fig):

        a = 3.2
        b = .8

        fig.add_trace(

            go.Scatter(

                x=a*np.cos(self.theta),

                y=b*np.sin(self.theta),

                mode="lines",

                line=dict(

                    color="cyan",

                    width=5

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Ergosphere
    # -------------------------------------------------------

    def add_ergosphere(self, fig):

        fig.add_trace(

            go.Scatter(

                x=1.8*np.cos(self.theta),

                y=1.45*np.sin(self.theta),

                mode="lines",

                line=dict(

                    color="orange",

                    dash="dash",

                    width=2

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Electric Field
    # -------------------------------------------------------

    def add_electric_field(self, fig):

        angles = np.linspace(0, 2*np.pi, 18)

        for a in angles:

            fig.add_trace(

                go.Scatter(

                    x=[1*np.cos(a), 4.3*np.cos(a)],

                    y=[1*np.sin(a), 4.3*np.sin(a)],

                    mode="lines",

                    line=dict(

                        color="deepskyblue",

                        dash="dot"

                    ),

                    hoverinfo="skip"

                )

            )

    # -------------------------------------------------------
    # Orbiting Matter
    # -------------------------------------------------------

    def add_particles(self, fig, number=180):

        angles = np.random.uniform(0, 2*np.pi, number)

        radius = np.random.uniform(2.2, 4.8, number)

        fig.add_trace(

            go.Scatter(

                x=radius*np.cos(angles),

                y=radius*np.sin(angles),

                mode="markers",

                marker=dict(

                    size=3,

                    color="white"

                ),

                hoverinfo="skip"

            )

        )

    # -------------------------------------------------------
    # Legend
    # -------------------------------------------------------

    def add_legend(

            self,

            fig,

            ergosphere=False,

            electric=False,

            disk=False

    ):

        text = (
            "<b>Legend</b><br>"
            "⚫ Event Horizon<br>"
            "🟡 Photon Ring<br>"
            "⚪ Orbiting Matter<br>"
        )

        if disk:
            text += "🔵 Accretion Disk<br>"

        if ergosphere:
            text += "🟠 Ergosphere<br>"

        if electric:
            text += "⚡ Electric Field"

        fig.add_annotation(

            x=5.8,

            y=5.7,

            xref="x",

            yref="y",

            align="left",

            showarrow=False,

            bgcolor="rgba(0,0,0,.65)",

            bordercolor="white",

            borderwidth=1,

            font=dict(

                size=10,

                color="white"

            ),

            text=text

        )

        return fig
