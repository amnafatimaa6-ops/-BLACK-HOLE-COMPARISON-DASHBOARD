import streamlit as st
import pandas as pd
import numpy as np
import json

from animations.schwarzschild import create as schwarzschild
from animations.kerr import create as kerr
from animations.reissner import create as reissner
from animations.kerr_newman import create as kerr_newman
import plotly.graph_objects as go


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(

    page_title="Black Hole Comparison Dashboard",

    page_icon="🌌",

    layout="wide",

    initial_sidebar_state="expanded"

)


# ==========================================================
# NASA Theme
# ==========================================================

st.markdown("""

<style>

/* Main App */

.stApp{

background:#020617;

color:white;

}


/* Sidebar */

[data-testid="stSidebar"]{

background:#07111f;

border-right:1px solid #1E3A8A;

}


/* Titles */

h1{

text-align:center;

font-size:42px;

font-weight:700;

background:linear-gradient(
90deg,
#38BDF8,
#FFD700,
#38BDF8
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}


h2{

color:#FFD700;

}


h3{

color:#7DD3FC;

}


/* Cards */

div[data-testid="stVerticalBlock"]{

border-radius:14px;

}


/* Metric Cards */

div[data-testid="metric-container"]{

background:#07192f;

padding:15px;

border-radius:12px;

border:1px solid #38BDF8;

box-shadow:0 0 12px rgba(56,189,248,0.15);

}


/* DataFrame */

[data-testid="stDataFrame"]{

border-radius:12px;

}


/* Expander */

.streamlit-expanderHeader{

font-size:18px;

font-weight:600;

color:#FFD700;

}


/* Buttons */

.stButton>button{

background:#0f172a;

color:white;

border:1px solid #38BDF8;

border-radius:8px;

}


.stButton>button:hover{

background:#38BDF8;

color:black;

}


/* Divider */

hr{

border:1px solid #1E3A8A;

}

</style>

""", unsafe_allow_html=True)



# ==========================================================
# Load Black Hole Data
# ==========================================================

with open("data/blackholes.json","r") as f:

    blackholes=json.load(f)



# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("⚙️ Simulation Controls")

st.sidebar.markdown("---")

mass=st.sidebar.slider(

"Mass (Solar Masses)",

1.0,

100.0,

10.0

)


spin=st.sidebar.slider(

"Spin Parameter (a)",

0.0,

0.99,

0.70

)


charge=st.sidebar.slider(

"Charge (Q)",

0.0,

1.0,

0.20

)


particles=st.sidebar.slider(

"Particle Count",

50,

500,

250

)


speed=st.sidebar.slider(

"Animation Speed",

1,

10,

5

)


st.sidebar.markdown("---")

st.sidebar.info("""

### Controls

⭐ **Mass**

Changes event horizon radius.

🌀 **Spin**

Changes frame dragging and ergosphere.

⚡ **Charge**

Controls electric field strength.

✨ **Particles**

Changes surrounding matter density.

🎬 **Animation**

Reserved for future orbital animation.

""")


# ==========================================================
# Title
# ==========================================================

st.title("🌌 Black Hole Comparison Dashboard")

st.markdown(
"""
### Interactive comparison of the four exact black hole solutions of General Relativity.

This dashboard combines **interactive scientific visualizations**, **physics calculations**,
and **comparative properties** of the Schwarzschild, Kerr,
Reissner–Nordström and Kerr–Newman solutions.

Move the sliders in the sidebar to explore how **mass**, **spin**,
**electric charge**, and **particle density** influence each simulation.
"""
)

st.divider()


# ==========================================================
# Top Row
# ==========================================================

col1, col2 = st.columns(2)


# ==========================================================
# Schwarzschild
# ==========================================================

with col1:

    st.subheader("⚫ Schwarzschild Black Hole")

    st.plotly_chart(

        schwarzschild(

            mass=mass,

            particles=particles,

            speed=speed

        ),

        use_container_width=True

    )

    st.info(

        blackholes["Schwarzschild"]["about"]

    )

    st.markdown("""

### Properties

- Rotation: **No**
- Charge: **No**
- Event Horizon: **Yes**
- Ergosphere: **No**
- Singularity: **Point**

""")



# ==========================================================
# Kerr
# ==========================================================

with col2:

    st.subheader("🌀 Kerr Black Hole")

    st.plotly_chart(

        kerr(

            mass=mass,

            spin=spin,

            particles=particles,

            speed=speed

        ),

        use_container_width=True

    )

    st.info(

        blackholes["Kerr"]["about"]

    )

    st.markdown("""

### Properties

- Rotation: **Yes**
- Charge: **No**
- Event Horizon: **Yes**
- Ergosphere: **Yes**
- Singularity: **Ring**

""")


# ==========================================================
# Bottom Row
# ==========================================================

st.divider()

col3, col4 = st.columns(2)


# ==========================================================
# Reissner–Nordström
# ==========================================================

with col3:

    st.subheader("⚡ Reissner–Nordström Black Hole")

    st.plotly_chart(

        reissner(

            mass=mass,

            charge=charge,

            particles=particles,

            speed=speed

        ),

        use_container_width=True

    )

    st.info(

        blackholes["Reissner-Nordström"]["about"]

    )

    st.markdown("""

### Properties

- Rotation: **No**
- Charge: **Yes**
- Event Horizon: **Yes**
- Ergosphere: **No**
- Singularity: **Point**

""")

    st.success("""

**Physical Interpretation**

The Reissner–Nordström solution describes a **non-rotating electrically charged**
black hole. The electric field modifies spacetime and changes the horizon
structure compared with the Schwarzschild solution.

""")


# ==========================================================
# Kerr–Newman
# ==========================================================

with col4:

    st.subheader("🌌 Kerr–Newman Black Hole")

    st.plotly_chart(

        kerr_newman(

            mass=mass,

            spin=spin,

            charge=charge,

            particles=particles,

            speed=speed

        ),

        use_container_width=True

    )

    st.info(

        blackholes["Kerr-Newman"]["about"]

    )

    st.markdown("""

### Properties

- Rotation: **Yes**
- Charge: **Yes**
- Event Horizon: **Yes**
- Ergosphere: **Yes**
- Singularity: **Ring**

""")

    st.success("""

**Physical Interpretation**

The Kerr–Newman solution is the **most general stationary black hole**
predicted by General Relativity, possessing **mass, angular momentum,
and electric charge** simultaneously.

""")



# ==========================================================
# Quick Scientific Summary
# ==========================================================

st.divider()

st.subheader("🔬 Scientific Summary")

summary1, summary2, summary3, summary4 = st.columns(4)

with summary1:
    st.metric(
        "Mass",
        f"{mass:.2f} M☉"
    )

with summary2:
    st.metric(
        "Spin",
        f"{spin:.2f}"
    )

with summary3:
    st.metric(
        "Charge",
        f"{charge:.2f}"
    )

with summary4:
    st.metric(
        "Particles",
        particles
    )


# ==========================================================
# Bottom Row
# ==========================================================

st.divider()

col3, col4 = st.columns(2)





# ==========================================================
# General Relativity Equations
# ==========================================================

st.divider()

st.header("📐 General Relativity Equations")

st.markdown("""
These four exact solutions of Einstein's Field Equations describe different
types of black holes depending on their physical properties such as
**mass**, **rotation**, and **electric charge**.
""")

eq1, eq2 = st.columns(2)

with eq1:

    with st.expander("⚫ Schwarzschild Metric", expanded=False):

        st.latex(r"""
ds^2=
-\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
+\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2
+r^2(d\theta^2+\sin^2\theta\,d\phi^2)
""")

        st.markdown("""
The **Schwarzschild solution (1916)** is the simplest exact solution of
Einstein's General Relativity.

It describes a **non-rotating, electrically neutral black hole** whose
geometry depends only on its mass.

This solution predicts:

- Event Horizon
- Photon Sphere
- Point Singularity
- Gravitational Time Dilation
""")

    with st.expander("⚡ Reissner–Nordström Metric", expanded=False):

        st.latex(r"""
ds^2=
-\left(
1-\frac{2GM}{rc^2}
+\frac{Q^2}{r^2}
\right)dt^2
+
\left(
1-\frac{2GM}{rc^2}
+\frac{Q^2}{r^2}
\right)^{-1}dr^2
+r^2d\Omega^2
""")

        st.markdown("""
This solution extends Schwarzschild by introducing **electric charge**.

Although mathematically important, astrophysical black holes are expected
to carry almost **no net charge** because surrounding plasma rapidly
neutralises them.
""")

with eq2:

    with st.expander("🌀 Kerr Metric", expanded=False):

        st.latex(r"""
\Delta=r^2-2Mr+a^2
""")

        st.latex(r"""
\Sigma=r^2+a^2\cos^2\theta
""")

        st.markdown("""
The **Kerr solution (1963)** describes rotating black holes.

Rotation twists spacetime itself through **frame dragging**, producing an
**ergosphere**, where no object can remain stationary relative to distant
observers.
""")

    with st.expander("🌌 Kerr–Newman Metric", expanded=False):

        st.latex(r"""
\Delta=r^2-2Mr+a^2+Q^2
""")

        st.latex(r"""
\Sigma=r^2+a^2\cos^2\theta
""")

        st.markdown("""
The **Kerr–Newman solution** is the most general stationary black hole
solution in General Relativity.

It simultaneously possesses:

- Mass
- Angular Momentum
- Electric Charge

All other stationary black hole solutions can be regarded as special cases
of the Kerr–Newman geometry.
""")



# ==========================================================
# Advanced Black Hole Physics Calculator
# ==========================================================

st.divider()

st.header("🧮 Advanced Black Hole Physics")

# Physical Constants
G = 6.67430e-11
c = 299792458
M_sun = 1.98847e30
h = 6.62607015e-34
hbar = h / (2 * np.pi)
kB = 1.380649e-23

M = mass * M_sun

# Schwarzschild Radius
Rs = (2 * G * M) / c**2

# Event Horizon
event_horizon = Rs

# Photon Sphere
photon_sphere = 1.5 * Rs

# ISCO
isco = 3 * Rs

# Escape Velocity
escape_velocity = c

# Surface Gravity
surface_gravity = c**4 / (4 * G * M)

# Hawking Temperature
hawking_temperature = (
    hbar * c**3
) / (
    8 * np.pi * G * M * kB
)

# Light Crossing Time
light_crossing = Rs / c

# Gravitational Redshift
redshift = (
    1 / np.sqrt(1 - Rs / (2 * Rs))
) - 1

# Horizon Area
horizon_area = 4 * np.pi * Rs**2

# Average Density
average_density = (
    M /
    ((4/3) * np.pi * Rs**3)
)

# Bekenstein-Hawking Entropy
entropy = (
    kB * horizon_area
) / (
    4 * 2.612e-70
)

row1 = st.columns(4)

with row1[0]:
    st.metric(
        "Event Horizon",
        f"{event_horizon/1000:.2f} km"
    )

with row1[1]:
    st.metric(
        "Photon Sphere",
        f"{photon_sphere/1000:.2f} km"
    )

with row1[2]:
    st.metric(
        "ISCO Radius",
        f"{isco/1000:.2f} km"
    )

with row1[3]:
    st.metric(
        "Escape Velocity",
        f"{escape_velocity/1000:.0f} km/s"
    )

row2 = st.columns(4)

with row2[0]:
    st.metric(
        "Surface Gravity",
        f"{surface_gravity:.3e} m/s²"
    )

with row2[1]:
    st.metric(
        "Hawking Temperature",
        f"{hawking_temperature:.3e} K"
    )

with row2[2]:
    st.metric(
        "Light Crossing Time",
        f"{light_crossing*1000:.3f} ms"
    )

with row2[3]:
    st.metric(
        "Gravitational Redshift",
        f"{redshift:.3f}"
    )

row3 = st.columns(3)

with row3[0]:
    st.metric(
        "Horizon Area",
        f"{horizon_area:.3e} m²"
    )

with row3[1]:
    st.metric(
        "Average Density",
        f"{average_density:.3e} kg/m³"
    )

with row3[2]:
    st.metric(
        "Entropy",
        f"{entropy:.3e} J/K"
    )


# ==========================================================
# Understanding Black Holes
# ==========================================================

st.divider()

st.header("🔭 Understanding Black Holes")

st.markdown("""
Black holes are among the most fascinating predictions of **Einstein's General Relativity**.
Although invisible, they can be studied through their effects on nearby matter, light,
and spacetime itself.

Expand the sections below to explore the key physical concepts.
""")

# ----------------------------------------------------------

with st.expander("⚫ Event Horizon"):

    st.markdown("""

### What is it?

The **event horizon** is the boundary surrounding a black hole beyond which
nothing—not even light—can escape.

### Key Facts

- Defines the visible size of a black hole.
- Escape velocity equals the speed of light.
- It is **not a physical surface**.
- Crossing the event horizon does not necessarily produce any local physical sensation.

""")

# ----------------------------------------------------------

with st.expander("🟡 Photon Sphere"):

    st.markdown("""

### What is it?

The **photon sphere** is the region where light can orbit the black hole.

### Key Facts

- Located at approximately **1.5 Schwarzschild radii** for a non-rotating black hole.
- Photon orbits are unstable.
- Responsible for the bright photon ring observed by the Event Horizon Telescope.

""")

# ----------------------------------------------------------

with st.expander("🌀 Frame Dragging"):

    st.markdown("""

### What is it?

Rotating black holes twist the surrounding spacetime.

This phenomenon is known as **frame dragging** or the **Lense–Thirring effect**.

### Consequences

- Produces an ergosphere.
- Changes nearby particle orbits.
- Extracting rotational energy is theoretically possible through the Penrose Process.

""")

# ----------------------------------------------------------

with st.expander("⚡ Electric Charge"):

    st.markdown("""

### Charged Black Holes

The Reissner–Nordström and Kerr–Newman solutions include electric charge.

### In Reality

Astronomers expect real black holes to possess **very little net charge**
because surrounding plasma quickly neutralises them.

Charged solutions remain extremely important for theoretical physics.

""")

# ----------------------------------------------------------

with st.expander("⭐ Singularity"):

    st.markdown("""

### Point Singularity

Schwarzschild and Reissner–Nordström black holes contain a
theoretical point singularity.

### Ring Singularity

Kerr and Kerr–Newman black holes contain a rotating ring singularity.

Modern theories of **quantum gravity** are expected to modify
these classical predictions.

""")

# ----------------------------------------------------------

with st.expander("🌡️ Hawking Radiation"):

    st.markdown("""

In 1974, Stephen Hawking showed that quantum effects allow
black holes to emit thermal radiation.

This causes black holes to lose mass extremely slowly.

Large astrophysical black holes evaporate so slowly that
their lifetimes greatly exceed the current age of the Universe.

""")

# ----------------------------------------------------------

with st.expander("📡 Gravitational Waves"):

    st.markdown("""

When black holes merge they generate ripples in spacetime
known as **gravitational waves**.

These waves were first directly detected by **LIGO** in 2015,
providing one of the greatest confirmations of General Relativity.

""")

# ----------------------------------------------------------

with st.expander("🛰️ Famous Black Holes"):

    st.table({

        "Object":[
            "Sagittarius A*",
            "M87*",
            "Cygnus X-1",
            "GW150914"
        ],

        "Type":[
            "Supermassive",
            "Supermassive",
            "Stellar",
            "Merger Event"
        ],

        "Approximate Mass":[
            "4.3 Million M☉",
            "6.5 Billion M☉",
            "21 M☉",
            "66 M☉ (final)"
        ]

    })


# ==========================================================
# Interactive Physics Explorer
# ==========================================================

st.divider()

st.header("📊 Black Hole Physics Explorer")

st.markdown("""
Explore how important black hole properties vary with mass.

The **red marker** indicates the current mass selected from the sidebar.
""")

masses = np.linspace(1, 100, 250)

M_values = masses * M_sun

Rs_values = (2 * G * M_values) / c**2

hawking_values = (
    hbar * c**3
) / (
    8 * np.pi * G * M_values * kB
)

gravity_values = c**4 / (4 * G * M_values)

density_values = (
    M_values /
    ((4 / 3) * np.pi * Rs_values**3)
)

crossing_values = Rs_values / c

tabs = st.tabs([
    "Event Horizon",
    "Temperature",
    "Gravity",
    "Density",
    "Crossing Time"
])


with tabs[0]:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=masses,
            y=Rs_values / 1000,
            name="Event Horizon Radius",
            line=dict(width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[mass],
            y=[Rs / 1000],
            mode="markers",
            marker=dict(
                size=12,
                color="red"
            ),
            name="Current"
        )
    )

    fig.update_layout(

        template="plotly_dark",

        title="Event Horizon Radius vs Mass",

        xaxis_title="Mass (Solar Masses)",

        yaxis_title="Radius (km)",

        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="graph_event_horizon"
    )






