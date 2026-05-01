import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Resilience.png")
col2.markdown("""
    ## 2050 Goal: Resilience
    # Adapt Oahu’s transportation network to be resilient to the effects of climate change
    Ensuring our transportation system is resilient to climate change and emergency weather events is crucial for addressing vulnerabilities and safeguarding the maintenance and safety of the network. Central to this effort is monitoring areas at risk from sea level rise and ensuring that these communities have redundant and reliable emergency access.
""")

st.divider()

st.markdown("""
## Address the vulnerability of Oahu’s surface transportation facilities caused by sea level rise
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/resilience/ompo/miles_of_sea_level_rise_potential_flooded_highways_under_32-foot_scenario.csv",
        title = "Miles of sea level rise potential flooded highways under 3.2-foot scenario",
        title_hover = "As climate change accelerates chronic erosion and sea-level rise, we face an increased need to address the vulnerabilities and resilience of our transportation network. To assess the impact of projects on the resiliency of our transportation network, Oahu Metropolitan Planning Organization (OahuMPO) will measure the miles of highways at risk of flooding due to sea level rise. This will be determined by evaluating coastal highways and major roads exposed to chronic flooding within sea level rise exposure zones. The 3.2-feet sea level rise scenario by the year 2100 is the most aggressive projection and will allow agencies to best prepare in the worst-case scenario.",
        is_federal_measure = False,
        source = "State of Hawaii GIS Program - Sea Level Rise (SLR) Potential Flooded Highways",
        is_bar_chart = True,
    )

st.divider()
st.markdown("""
## Provide redundant emergency access, especially in singular access communities
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/resilience/ompo/percent_of_population_lacking_redundant_emergency_vehicular_accessegress.csv",
        title = "Percent of population lacking redundant emergency vehicular access/egress",
        title_hover = "As natural disaster events increase, we face an increased need to address vulnerabilities and resiliency of our transportation network. To evaluate how projects impact the resilience of our transportation network, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of the population that lacks redundant vehicle access. This will be done using a model utilizing the [Transportation Demand Network](https://ops.fhwa.dot.gov/plan4ops/trans_demand.htm) to depict the percentage of the population that would be disconnected if a road network were to become inaccessible in an emergency.",
        is_federal_measure = False,
        source = "OahuMPO Traffic Analysis Zones",
    )
