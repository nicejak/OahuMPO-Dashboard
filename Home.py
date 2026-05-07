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

st.markdown("""
    ## Featured measure
""")

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

st.markdown("""
    ## 2050 Oahu Regional Transportation Plan Goals
    The goals of the 2050 ORTP are shown below. Click on each icon for a detailed description and data, or scroll down for an overview of each goal.
""")

col1, col2 = st.columns(2, vertical_alignment = "center", border = True)
col11, col12 = col1.columns([0.35, 0.65], vertical_alignment = "center")
col11.image("./images/Safety.png")
col12.link_button("Safety", "Safety", width="stretch")
col21, col22 = col2.columns([0.35, 0.65], vertical_alignment = "center")
col21.image("./images/Active_and_Public_Transportation.png")
col22.link_button("Active and Public Transportation", "Active_and_Public_Transportation", width="stretch")

col1, col2 = st.columns(2, vertical_alignment = "center", border = True)
col11, col12 = col1.columns([0.35, 0.65], vertical_alignment = "center")
col11.image("./images/Equity.png")
col12.link_button("Equity", "Equity", width="stretch")
col21, col22 = col2.columns([0.35, 0.65], vertical_alignment = "center")
col21.image("./images/Resilience.png")
col22.link_button("Resilience", "Resilience", width="stretch")

col1, col2 = st.columns(2, vertical_alignment = "center", border = True)
col11, col12 = col1.columns([0.35, 0.65], vertical_alignment = "center")
col11.image("./images/Maintenance.png")
col12.link_button("Maintenance", "Maintenance", width="stretch")
col21, col22 = col2.columns([0.35, 0.65], vertical_alignment = "center")
col21.image("./images/Land_Use_and_Transportation.png")
col22.link_button("Land Use and Transportation", "Land_Use_and_Transportation", width="stretch")

col1, col2 = st.columns(2, vertical_alignment = "center", border = True)
col11, col12 = col1.columns([0.35, 0.65], vertical_alignment = "center")
col11.image("./images/Sustainability.png")
col12.link_button("Sustainability", "Sustainability", width="stretch")
col2.space("xlarge")
