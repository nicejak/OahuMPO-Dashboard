import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Equity.png")
col2.markdown("""
    ## 2050 Goal: Equity
    # Provide an equitable and affordable transportation system
    Making transportation affordable ensures equity. Oahu Metropolitan Planning Organization (OahuMPO) is focused on prioritizing bike, pedestrian, and transit projects in traditionally underserved areas, as well as communities facing challenges in housing and transportation costs.
""")

st.divider()

st.markdown("""
## Invest in Title VI and Environmental Justice Areas
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/equity/ompo/per_capita_project_expenditures_spent_on_transit_or_active_transportation_in_title_vienvironmental_justice_areas.csv",
        title = "Per capita project expenditures spent on transit or active transportation in Title VI/Environmental Justice Areas",
        title_hover = "Bridging gaps in traditionally underrepresented and underfunded communities, identified as Title VI and Environmental Justice (T6/EJ) Communities, helps to create a more equitable transportation system. To help rectify these gaps, Oahu Metropolitan Planning Organization (OahuMPO) will monitor per capita project expenditures spent on transit or active transportation projects in T6/EJ communities.",
        is_federal_measure = False,
        source = "OahuMPO Oahu Regional Transportation Plan Expenditures",
        is_bar_chart = True,
    )

st.divider()
st.markdown("""
## Provide transit access to assist in reducing household transportation costs
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/equity/ompo/share_of_housing_and_transportation_costs_as_a_percentage_of_income_county.csv",
        title = "Share of housing and transportation costs as a percentage of income​ (County)",
        title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will measure affordability by evaluating the share of housing and transportation costs as a percentage of income on a countywide scale. This data comes from the Housing and Transportation Index, produced by the Center for Neighborhood Technology, which provides a variety of affordability metrics on housing and transportation. Oahu Metropolitan Planning Organization (OahuMPO) will specifically be using Housing + Transportation Costs as a percentage of income index, which demonstrates the proportion of household income spent on housing and transportation.",
        is_federal_measure = False,
        source = "Center for Neighborhood Technology (CNT) - Housing Transportation Index",
    )

with col2:
    make_plot(
        path = "./data/equity/ompo/percent_of_households_living_in_areas_lacking_housing_and_transportation_affordability.csv",
        title = "Percent of households living in areas lacking housing and transportation affordability",
        title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will measure affordability by assessing the share of households living in areas that lack both transportation and housing affordability. This data comes from United for ALICE, led by the United Way. The ALICE (Asset Limited, Income Constrained, Employed) indicator represents households that earn more than the Federal Poverty Level, but still struggle to afford necessities in their community. Oahu Metropolitan Planning Organization (OahuMPO) will use the percentage of households below ALICE thresholds by zip code to determine the percentage of households living in areas lacking housing and transportation affordability.",
        is_federal_measure = False,
        source = "United for ALICE",
    )
