import streamlit as st
import pandas as pd
import json

from animations.schwarzschild import create as schwarzschild
from animations.kerr import create as kerr
from animations.reissner import create as reissner
from animations.kerr_newman import create as kerr_newman


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Black Hole Comparison Dashboard",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# -----------------------------------------------------
# Load Scientific Data
# -----------------------------------------------------

with open("data/blackholes.json", "r") as file:
    blackholes = json.load(file)


# -----------------------------------------------------
# Title
# -----------------------------------------------------

st.title("🌌 Black Hole Comparison Dashboard")

st.markdown("""
Compare the four exact black hole solutions of General Relativity.

Each visualization demonstrates the major physical characteristics of a particular solution.
""")

st.divider()


# -----------------------------------------------------
# Four Columns
# -----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


# =====================================================
# Schwarzschild
# =====================================================

with col1:

    st.subheader("Schwarzschild")

    fig = schwarzschild()

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### About")

    st.write(
        blackholes["Schwarzschild"]["about"]
    )

    st.markdown("### Properties")

    st.markdown(f"""
- **Rotation:** {blackholes["Schwarzschild"]["rotation"]}
- **Charge:** {blackholes["Schwarzschild"]["charge"]}
- **Event Horizon:** {blackholes["Schwarzschild"]["event_horizon"]}
- **Ergosphere:** {blackholes["Schwarzschild"]["ergosphere"]}
- **Singularity:** {blackholes["Schwarzschild"]["singularity"]}
""")


# =====================================================
# Kerr
# =====================================================

with col2:

    st.subheader("Kerr")

    fig = kerr()

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### About")

    st.write(
        blackholes["Kerr"]["about"]
    )

    st.markdown("### Properties")

    st.markdown(f"""
- **Rotation:** {blackholes["Kerr"]["rotation"]}
- **Charge:** {blackholes["Kerr"]["charge"]}
- **Event Horizon:** {blackholes["Kerr"]["event_horizon"]}
- **Ergosphere:** {blackholes["Kerr"]["ergosphere"]}
- **Singularity:** {blackholes["Kerr"]["singularity"]}
""")


# =====================================================
# Reissner–Nordström
# =====================================================

with col3:

    st.subheader("Reissner–Nordström")

    fig = reissner()

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### About")

    st.write(
        blackholes["Reissner-Nordström"]["about"]
    )

    st.markdown("### Properties")

    st.markdown(f"""
- **Rotation:** {blackholes["Reissner-Nordström"]["rotation"]}
- **Charge:** {blackholes["Reissner-Nordström"]["charge"]}
- **Event Horizon:** {blackholes["Reissner-Nordström"]["event_horizon"]}
- **Ergosphere:** {blackholes["Reissner-Nordström"]["ergosphere"]}
- **Singularity:** {blackholes["Reissner-Nordström"]["singularity"]}
""")


# =====================================================
# Kerr-Newman
# =====================================================

with col4:

    st.subheader("Kerr-Newman")

    fig = kerr_newman()

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("### About")

    st.write(
        blackholes["Kerr-Newman"]["about"]
    )

    st.markdown("### Properties")

    st.markdown(f"""
- **Rotation:** {blackholes["Kerr-Newman"]["rotation"]}
- **Charge:** {blackholes["Kerr-Newman"]["charge"]}
- **Event Horizon:** {blackholes["Kerr-Newman"]["event_horizon"]}
- **Ergosphere:** {blackholes["Kerr-Newman"]["ergosphere"]}
- **Singularity:** {blackholes["Kerr-Newman"]["singularity"]}
""")


# -----------------------------------------------------
# Comparison Table
# -----------------------------------------------------

st.divider()

st.header("Scientific Comparison")

comparison = pd.DataFrame({

    "Property": [
        "Rotation",
        "Charge",
        "Event Horizon",
        "Ergosphere",
        "Singularity"
    ],

    "Schwarzschild": [
        "No",
        "No",
        "Yes",
        "No",
        "Point"
    ],

    "Kerr": [
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Ring"
    ],

    "Reissner–Nordström": [
        "No",
        "Yes",
        "Yes",
        "No",
        "Point"
    ],

    "Kerr–Newman": [
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


# -----------------------------------------------------
# Footer
# -----------------------------------------------------

st.divider()

st.caption(
    "Interactive comparison of Schwarzschild, Kerr, Reissner–Nordström, and Kerr–Newman black hole solutions in General Relativity."
)
