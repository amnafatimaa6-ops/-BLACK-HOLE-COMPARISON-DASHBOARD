import numpy as np
import plotly.graph_objects as go


# ------------------------------------
# Shared layout
# ------------------------------------

def base_layout(fig):

    fig.update_layout(

        template="plotly_dark",

        width=300,
        height=300,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        xaxis=dict(
            visible=False,
            range=[-6,6]
        ),

        yaxis=dict(
            visible=False,
            range=[-6,6],
            scaleanchor="x"
        ),

        showlegend=False

    )

    return fig


# ------------------------------------
# Event horizon
# ------------------------------------

def draw_horizon(fig,radius=1):

    theta=np.linspace(0,2*np.pi,300)

    x=radius*np.cos(theta)
    y=radius*np.sin(theta)

    fig.add_trace(

        go.Scatter(

            x=x,
            y=y,

            mode="lines",

            fill="toself",

            line=dict(width=2),

            name="Event Horizon"

        )

    )


# ------------------------------------
# Accretion disk
# ------------------------------------

def draw_disk(fig,r1=1.5,r2=2.5):

    theta=np.linspace(0,2*np.pi,400)

    x1=r1*np.cos(theta)
    y1=r1*np.sin(theta)

    x2=r2*np.cos(theta[::-1])
    y2=r2*np.sin(theta[::-1])

    fig.add_trace(

        go.Scatter(

            x=np.concatenate([x1,x2]),
            y=np.concatenate([y1,y2]),

            fill="toself",

            mode="lines",

            opacity=0.4,

            line=dict(width=0)

        )

    )


# ------------------------------------
# Electric field
# ------------------------------------

def draw_field(fig):

    angles=np.linspace(0,2*np.pi,18)

    for a in angles:

        fig.add_trace(

            go.Scatter(

                x=[1*np.cos(a),4*np.cos(a)],
                y=[1*np.sin(a),4*np.sin(a)],

                mode="lines",

                line=dict(width=1,dash="dot")

            )

        )


# ------------------------------------
# Schwarzschild
# ------------------------------------

def schwarzschild_sim():

    fig=go.Figure()

    draw_horizon(fig)

    return base_layout(fig)


# ------------------------------------
# Kerr
# ------------------------------------

def kerr_sim():

    fig=go.Figure()

    draw_horizon(fig)

    draw_disk(fig)

    return base_layout(fig)


# ------------------------------------
# Reissner-Nordström
# ------------------------------------

def reissner_sim():

    fig=go.Figure()

    draw_horizon(fig)

    draw_field(fig)

    return base_layout(fig)


# ------------------------------------
# Kerr-Newman
# ------------------------------------

def kerr_newman_sim():

    fig=go.Figure()

    draw_horizon(fig)

    draw_disk(fig)

    draw_field(fig)

    return base_layout(fig)
