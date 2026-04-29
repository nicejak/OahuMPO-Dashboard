import streamlit as st
from numpy.random import default_rng as rng

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns(2, vertical_alignment = "center")
col2.image("./images/Home_Header.png")
col1.markdown("""
# Welcome to the Oahu Regional Transportation Dashboard
Find out how we are tracking our path towards regional transportation goals
""")

st.divider()

st.markdown("# Explore performance measures that matter to you")

col1, col2 = st.columns(2, vertical_alignment = "center", border = True)

col1.markdown("""
    Over the coming months, community members will have opportunities to actively participate in shaping the vision and direction of the [Oahu Regional Transportation Plan 2050 (ORTP2050)](https://engage.oahumpo.org/oahu-regional-transportation-plan-ortp-2050)
""")

col2.markdown("[Have questions? Let's hear them](mailto:oahumpo@oahumpo.org)")

st.markdown("# Featured measure")
st.markdown("blah blah something")
