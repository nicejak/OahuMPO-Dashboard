import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Sustainability.png")
col2.markdown("""
    ## 2050 Goal: Sustainability
    # Achieve state and county commitments to the environment, health, and culture in the development, maintenance, and operation of the transportation system
    Ensuring sustainability in transportation is crucial with the landmark Navahine vs State of Hawaii Department of Transportation decision, which requires the State of Hawaii Department of Transportation to reduce greenhouse gas emissions. To support this effort, the Oahu Metropolitan Planning Organization (OahuMPO) will prioritize reducing greenhouse gas emissions from surface transportation and expanding sidewalks and bike facilities. Additionally, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit vehicles that are zero-emission, track the number of registered vehicles that are electric, assess the percent of tailpipe carbon emissions, and measure the growth in miles of bikeways and walkways.
""")

st.divider()

st.markdown("""
## Reduce greenhouse gas emissions from surface transportation
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/sustainability/ompo/percent_of_city_transit_fleet_that_is_zero-emission_vehicles.csv",
        title = "Percent of City Transit Fleet that is Zero-emission Vehicles",
        title_hover = "The landmark Navahine vs. State of Hawaii Department of Transportation requires the implementation of actions to bring transportation sector emissions to Zero by 2045. To assist in achieving this goal, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit vehicles that are electric versus its entire fleet of transit vehicles. The data will be provided by the City and County of Honolulu Department of Transportation Services.",
        is_federal_measure = False,
        source = "City and County of Honolulu - Department of Transportation Services",
    )

with col2:
    make_plot(
        path = "./data/sustainability/ompo/percent_change_in_tailpipe_carbon_dioxide_co2_emissions_on_the_national_highway_system_nhs_compared_to_the_reference_year_of_calendar_year_2022.csv",
        title = "Percent Change in Tailpipe Carbon Dioxide (CO2) emissions on the National Highway System (NHS) compared to the reference year of calendar year 2022",
        title_hover = "The landmark Navahine vs. State of Hawaii Department of Transportation requires the implementation of actions to bring transportation sector emissions to Zero by 2045. To assist in achieving this goal, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percent change in tailpipe carbon dioxide (CO2) emissions on the National Highway System (NHS) compared to the reference of calendar year 2022.",
        is_federal_measure = False,
        source = "State of Hawaii Department of Transportation and the United States Department of Energy",
    )

col1.write("---");
col2.write("---");

with col1:
    make_plot(
        path = "./data/sustainability/ompo/percent_of_registered_vehicles_that_are_electric.csv",
        title = "Percent of Registered Vehicles that are Electric",
        title_hover = "The landmark Navahine vs. State of Hawaii Department of Transportation requires the implementation of actions to bring transportation sector emissions to Zero by 2045. To support this goal, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of registered passenger and freight vehicles that are electric. This data is publicly accessible through the State of Hawaii Department of Business, Economic Development, and Tourism.",
        is_federal_measure = False,
        source = "State of Hawaii Department of Business, Economic Development & Tourism - Research and Economic Analysis",
    )


st.divider()
st.markdown("""
## Support active living by increasing mileage of sidewalks and bike facilities
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/sustainability/ompo/miles_of_bikeways_bike_lanes_protected_bike_lanes_and_shared_use_paths.csv",
        title = "Miles of Bikeways (bike lanes, protected bike lanes, and shared use paths)",
        title_hover = "The landmark Navahine vs. State of Hawaii Department of Transportation requires the implementation of actions to bring transportation sector emissions to Zero by 2045. To support this goal, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of registered passenger and freight vehicles that are electric. This data is publicly accessible through the State of Hawaii Department of Business, Economic Development, and Tourism.",
        is_federal_measure = False,
        source = "State of Hawaii Department of Transportation and City and County of Honolulu Department of Transportation Services",
    )

with col2:
    make_plot(
        path = "./data/sustainability/ompo/miles_of_walkways.csv",
        title = "Miles of Walkways​",
        title_hover = "A crucial component of reducing greenhouse gas emissions, as outlined in the Navahine vs State of Hawaii Department of Transportation decision, is the expansion of the active transportation network. To monitor this, Oahu Metropolitan Planning Organization (OahuMPO) will track the mileage of walkways using data provided by the City and County of Honolulu Department of Transportation Services and State of Hawaii Department of Transportation. [Walkways](https://hidot.hawaii.gov/highways/files/2013/07/Pedest-Tbox-Hawaii-Pedestrian-Toolbox-Low-Res.pdf) are defined by as raised or at-grade improved paths designed exclusively for pedestrian use. This includes sidewalks, which are portions of a street between curb lines, or the lateral lines of a roadway, and the adjacent property lines, specifically intended for pedestrian movement.",
        is_federal_measure = False,
        source = "State of Hawaii Department of Transportation and City and County of Honolulu Department of Transportation Services",
    )
