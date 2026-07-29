import streamlit as st
import pandas as pd
import json

from simulator import (
    schwarzschild_sim,
    kerr_sim,
    reissner_sim,
    kerr_newman_sim
)

st.set_page_config(
    page_title="Black Hole Comparison",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🌌 Black Hole Comparison Dashboard")
st.markdown(
"""
Compare the four exact black hole solutions of General Relativity.

Each panel below contains a live simulation together with its physical properties.
"""
)

# -----------------------------
# Load data
# -----------------------------

with open("blackholes.json","r") as f:
    data = json.load(f)

# -----------------------------
# Four simulations
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.subheader("Schwarzschild")

    st.plotly_chart(
        schwarzschild_sim(),
        use_container_width=True
    )

    st.json(data["Schwarzschild"])

with col2:

    st.subheader("Kerr")

    st.plotly_chart(
        kerr_sim(),
        use_container_width=True
    )

    st.json(data["Kerr"])

with col3:

    st.subheader("Reissner-Nordström")

    st.plotly_chart(
        reissner_sim(),
        use_container_width=True
    )

    st.json(data["Reissner-Nordström"])

with col4:

    st.subheader("Kerr-Newman")

    st.plotly_chart(
        kerr_newman_sim(),
        use_container_width=True
    )

    st.json(data["Kerr-Newman"])

st.divider()

st.header("Scientific Comparison")

comparison = pd.DataFrame({

"Property":[
"Rotation",
"Charge",
"Event Horizon",
"Ergosphere",
"Singularity"
],

"Schwarzschild":[
"No",
"No",
"Yes",
"No",
"Point"
],

"Kerr":[
"Yes",
"No",
"Yes",
"Yes",
"Ring"
],

"Reissner-Nordström":[
"No",
"Yes",
"Yes",
"No",
"Point"
],

"Kerr-Newman":[
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
