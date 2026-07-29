import streamlit as st
import pandas as pd
import json

# Import the four black hole simulations
from animations.schwarzschild import create as schwarzschild
from animations.kerr import create as kerr
from animations.reissner import create as reissner
from animations.kerr_newman import create as kerr_newman


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Black Hole Comparison Dashboard",
    page_icon="🌌",
    layout="wide"
)

# ---------------------------------------------------
# Load JSON Data
# ---------------------------------------------------

with open("data/blackholes.json", "r") as f:
    blackholes = json.load(f)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🌌 Black Hole Comparison Dashboard")

st.markdown("""
Compare the four exact black hole solutions of General Relativity.

Each panel below shows a visualization together with its physical properties.
""")

st.divider()

# ---------------------------------------------------
# Four Columns
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

# ===================================================
# Schwarzschild
# ===================================================

with col1:

    st.subheader("Schwarzschild")

    st.plotly_chart(
        schwarzschild(),
        use_container_width=True
    )

    st.markdown("### About")
    st.write(blackholes["Schwarzschild"]["about"])

    st.markdown("### Properties")

    st.write(f"**Rotation:** {blackholes['Schwarzschild']['rotation']}")
    st.write(f"**Charge:** {blackholes['Schwarzschild']['charge']}")
    st.write(f"**Event Horizon:** {blackholes['Schwarzschild']['event_horizon']}")
    st.write(f"**Ergosphere:** {blackholes['Schwarzschild']['ergosphere']}")
    st.write(f"**Singularity:** {blackholes['Schwarzschild']['singularity']}")

# ===================================================
# Kerr
# ===================================================

with col2:

    st.subheader("Kerr")

    st.plotly_chart(
        kerr(),
        use_container_width=True
    )

    st.markdown("### About")
    st.write(blackholes["Kerr"]["about"])

    st.markdown("### Properties")

    st.write(f"**Rotation:** {blackholes['Kerr']['rotation']}")
    st.write(f"**Charge:** {blackholes['Kerr']['charge']}")
    st.write(f"**Event Horizon:** {blackholes['Kerr']['event_horizon']}")
    st.write(f"**Ergosphere:** {blackholes['Kerr']['ergosphere']}")
    st.write(f"**Singularity:** {blackholes['Kerr']['singularity']}")

# ===================================================
# Reissner-Nordström
# ===================================================

with col3:

    st.subheader("Reissner–Nordström")

    st.plotly_chart(
        reissner(),
        use_container_width=True
    )

    st.markdown("### About")
    st.write(blackholes["Reissner-Nordström"]["about"])

    st.markdown("### Properties")

    st.write(f"**Rotation:** {blackholes['Reissner-Nordström']['rotation']}")
    st.write(f"**Charge:** {blackholes['Reissner-Nordström']['charge']}")
    st.write(f"**Event Horizon:** {blackholes['Reissner-Nordström']['event_horizon']}")
    st.write(f"**Ergosphere:** {blackholes['Reissner-Nordström']['ergosphere']}")
    st.write(f"**Singularity:** {blackholes['Reissner-Nordström']['singularity']}")

# ===================================================
# Kerr-Newman
# ===================================================

with col4:

    st.subheader("Kerr-Newman")

    st.plotly_chart(
        kerr_newman(),
        use_container_width=True
    )

    st.markdown("### About")
    st.write(blackholes["Kerr-Newman"]["about"])

    st.markdown("### Properties")

    st.write(f"**Rotation:** {blackholes['Kerr-Newman']['rotation']}")
    st.write(f"**Charge:** {blackholes['Kerr-Newman']['charge']}")
    st.write(f"**Event Horizon:** {blackholes['Kerr-Newman']['event_horizon']}")
    st.write(f"**Ergosphere:** {blackholes['Kerr-Newman']['ergosphere']}")
    st.write(f"**Singularity:** {blackholes['Kerr-Newman']['singularity']}")

# ---------------------------------------------------
# Comparison Table
# ---------------------------------------------------

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

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.caption(
    "Interactive comparison of Schwarzschild, Kerr, Reissner–Nordström and Kerr–Newman black holes."
)
