import streamlit as st
import pandas as pd
import json
import numpy as np

from animations.schwarzschild import create as schwarzschild
from animations.kerr import create as kerr
from animations.reissner import create as reissner
from animations.kerr_newman import create as kerr_newman


# ==========================================
# Page Setup
# ==========================================

st.set_page_config(
    page_title="Black Hole Comparison Dashboard",
    page_icon="🌌",
    layout="wide"
)


# ==========================================
# Load Data
# ==========================================

with open("data/blackholes.json") as file:
    blackholes = json.load(file)


# ==========================================
# Sidebar Controls
# ==========================================

st.sidebar.title("⚙️ Simulation Controls")


mass = st.sidebar.slider(
    "Mass (Solar Masses)",
    1.0,
    100.0,
    10.0
)


spin = st.sidebar.slider(
    "Spin Parameter (a)",
    0.0,
    0.99,
    0.7
)


charge = st.sidebar.slider(
    "Charge (Q)",
    0.0,
    1.0,
    0.2
)


particles = st.sidebar.slider(
    "Particle Count",
    50,
    500,
    250
)


speed = st.sidebar.slider(
    "Animation Speed",
    1,
    10,
    5
)



# ==========================================
# Title
# ==========================================

st.title(
    "🌌 Black Hole Comparison Dashboard"
)


st.markdown(
"""
Compare the four exact black hole solutions
of Einstein's General Relativity.

Each simulation represents the physical properties
of a different black hole solution.
"""
)


st.divider()



# ==========================================
# Black Hole Simulations
# ==========================================


col1, col2, col3, col4 = st.columns(4)



# ------------------------------------------
# Schwarzschild
# ------------------------------------------

with col1:

    st.subheader("Schwarzschild")


    st.plotly_chart(
        schwarzschild(),
        use_container_width=True
    )


    st.write(
        blackholes["Schwarzschild"]["about"]
    )


    st.markdown(
    f"""
    **Rotation:** {blackholes["Schwarzschild"]["rotation"]}

    **Charge:** {blackholes["Schwarzschild"]["charge"]}

    **Event Horizon:** {blackholes["Schwarzschild"]["event_horizon"]}

    **Ergosphere:** {blackholes["Schwarzschild"]["ergosphere"]}

    **Singularity:** {blackholes["Schwarzschild"]["singularity"]}
    """
    )



# ------------------------------------------
# Kerr
# ------------------------------------------

with col2:

    st.subheader("Kerr")


    st.plotly_chart(
        kerr(),
        use_container_width=True
    )


    st.write(
        blackholes["Kerr"]["about"]
    )


    st.markdown(
    f"""
    **Rotation:** {blackholes["Kerr"]["rotation"]}

    **Charge:** {blackholes["Kerr"]["charge"]}

    **Event Horizon:** {blackholes["Kerr"]["event_horizon"]}

    **Ergosphere:** {blackholes["Kerr"]["ergosphere"]}

    **Singularity:** {blackholes["Kerr"]["singularity"]}
    """
    )



# ------------------------------------------
# Reissner Nordstrom
# ------------------------------------------

with col3:

    st.subheader("Reissner–Nordström")


    st.plotly_chart(
        reissner(),
        use_container_width=True
    )


    st.write(
        blackholes["Reissner-Nordström"]["about"]
    )


    st.markdown(
    f"""
    **Rotation:** {blackholes["Reissner-Nordström"]["rotation"]}

    **Charge:** {blackholes["Reissner-Nordström"]["charge"]}

    **Event Horizon:** {blackholes["Reissner-Nordström"]["event_horizon"]}

    **Ergosphere:** {blackholes["Reissner-Nordström"]["ergosphere"]}

    **Singularity:** {blackholes["Reissner-Nordström"]["singularity"]}
    """
    )



# ------------------------------------------
# Kerr Newman
# ------------------------------------------

with col4:

    st.subheader("Kerr-Newman")


    st.plotly_chart(
        kerr_newman(),
        use_container_width=True
    )


    st.write(
        blackholes["Kerr-Newman"]["about"]
    )


    st.markdown(
    f"""
    **Rotation:** {blackholes["Kerr-Newman"]["rotation"]}

    **Charge:** {blackholes["Kerr-Newman"]["charge"]}

    **Event Horizon:** {blackholes["Kerr-Newman"]["event_horizon"]}

    **Ergosphere:** {blackholes["Kerr-Newman"]["ergosphere"]}

    **Singularity:** {blackholes["Kerr-Newman"]["singularity"]}
    """
    )



# ==========================================
# Comparison Table
# ==========================================

st.divider()

st.header("📊 Scientific Comparison")


comparison = pd.DataFrame({

"Property":
[
"Rotation",
"Charge",
"Event Horizon",
"Ergosphere",
"Singularity"
],

"Schwarzschild":
[
"No",
"No",
"Yes",
"No",
"Point"
],

"Kerr":
[
"Yes",
"No",
"Yes",
"Yes",
"Ring"
],

"Reissner–Nordström":
[
"No",
"Yes",
"Yes",
"No",
"Point"
],

"Kerr–Newman":
[
"Yes",
"Yes",
"Yes",
"Yes",
"Ring"
]

})


st.dataframe(
comparison,
use_container_width=True,
hide_index=True
)



# ==========================================
# GR Equations
# ==========================================

st.divider()

st.header("📐 General Relativity Equations")



with st.expander("Schwarzschild Metric"):

    st.latex(
r"""
ds^2 =
-\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
+
\left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2
+r^2d\Omega^2
"""
)



with st.expander("Kerr Metric"):

    st.latex(
r"""
\Delta=r^2-2Mr+a^2
"""
)



with st.expander("Reissner–Nordström Metric"):

    st.latex(
r"""
f(r)=1-\frac{2GM}{rc^2}
+\frac{Q^2}{r^2}
"""
)



with st.expander("Kerr-Newman Metric"):

    st.latex(
r"""
\Delta=r^2-2Mr+a^2+Q^2
"""
)



# ==========================================
# Physics Calculator
# ==========================================

st.divider()

st.header("🧮 Black Hole Calculator")


G = 6.67430e-11

c = 299792458

solar_mass = 1.98847e30


M = mass * solar_mass


Rs = (2*G*M)/(c**2)


photon_radius = 1.5*Rs


hbar = 1.054571817e-34

kB = 1.380649e-23


temperature = (
    hbar*c**3
)/(8*np.pi*G*M*kB)



a,b,c1 = st.columns(3)


with a:

    st.metric(
        "Event Horizon Radius",
        f"{Rs/1000:.2f} km"
    )


with b:

    st.metric(
        "Photon Sphere",
        f"{photon_radius/1000:.2f} km"
    )


with c1:

    st.metric(
        "Hawking Temperature",
        f"{temperature:.3e} K"
    )



st.divider()


st.caption(
"Interactive computational visualization of exact black hole solutions in General Relativity."
)
