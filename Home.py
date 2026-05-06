import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns(2, vertical_alignment = "center")
col2.image("./images/Home_Header.png")
col1.markdown("""
# Welcome to the Oahu Regional Transportation Dashboard
Track progress toward the adopted goals and performance measures of the ORTP 2050 through clear, data-driven reporting aligned with federal planning requirements.
""")

st.divider()

st.markdown("## Explore performance measures that matter to you")

col1, col2 = st.columns(2, vertical_alignment = "center", border = False)

col1.markdown("""
    This dashboard monitors system performance and trends to inform future ORTP updates, TIP programming, and performance-based investment decisions.
""")

col2.link_button(":incoming_envelope: Have questions? Let's hear them", "mailto:oahumpo@oahumpo.org")

st.divider()

col1, col2 = st.columns(2, vertical_alignment = "center", border = False)

with col1:
    make_plot(
        path = "./data/safety/ompo/percent_of_crashes_involving_impaired_driving.csv",
        title = "Percent of crashes involving impaired driving",
        title_hover = "Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety. To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes involving impaired driving using data provided by the State of Hawaii Department of Transportation.",
        is_federal_measure = False,
        source = "State of Hawaii Department of Transportation"
    )

col2.markdown("""
    ### About this Measure

    Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety.


    To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes involving impaired driving using data provided by the State of Hawaii Department of Transportation.

    **Goal: Reduce serious injuries and traffic deaths to zero**
""")
col2.link_button("Learn More", "Safety")
