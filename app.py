import streamlit as st
import pandas as pd
import numpy as np
import json

from animations.schwarzschild import create as schwarzschild
from animations.kerr import create as kerr
from animations.reissner import create as reissner
from animations.kerr_newman import create as kerr_newman


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



