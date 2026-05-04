import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Land_Use_and_Transportation.png")
col2.markdown("""
    ## 2050 Goal: Land Use and Transportation
    # Integrate land use and transportation planning to provide a reliable and efficient multimodal transportation system
    Integrating land use and transportation planning can assist in providing a reliable, efficient, and multimodal transportation system. To support this goal, the Oahu Metropolitan Planning Organization (OahuMPO) will track the percentage of people living and working in transit-oriented development zones, as well as monitor transit reliability and the performance of both interstate and non-interstate systems.
""")

st.divider()

tab1, tab2 = st.tabs(["Federally Required Performance Measures", "OahuMPO Performance Measures"])

with tab1:
    st.markdown("## Improve transit reliability")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/federally_required/mean_distance_between_major_mechanical_failures.csv",
            title = "Mean Distance Between Major Mechanical Failures",
            title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will monitor the average distance between major mechanical failures, as reported by the City and County of Honolulu Department of Transportation Services, to assist in insuring a safe transit system.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    st.divider()
    st.markdown("## Improve the reliability and efficiency of highway freight networks")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/federally_required/interstate_highway_reliable_person-miles_traveled.csv",
            title = "Interstate Highway Reliable Person-Miles Traveled",
            title_hover = "Reliability assesses the consistency, or dependability, of travel times. To monitor dependability and implement projects and programs that assist in congestion reduction, Oahu Metropolitan Planning Organization (OahuMPO) will track the percentage of persons-miles traveled on the interstate that are [reliable](https://www.fhwa.dot.gov/tpm/).",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/land_use_and_transportation/federally_required/interstate_highway_truck_travel_time_reliability_tttr_index.csv",
            title = "Interstate Highway Truck Travel Time Reliability (TTTR) Index",
            title_hover = "Reliability assesses the consistency, or dependability, of travel times. To monitor dependability and implement projects and programs that assist in congestion reduction, Oahu Metropolitan Planning Organization (OahuMPO) will [track the truck travel time reliability (TTTR)](https://www.federalregister.gov/documents/2017/01/18/2017-00681/national-performance-management-measures-assessing-performance-of-the-national-highway-system) on the interstate system.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/federally_required/non-interstate_national_highway_system_nhs_reliable_person-miles_traveled.csv",
            title = "Non-Interstate National Highway System (NHS) Reliable Person-Miles Traveled",
            title_hover = "Reliability assesses the consistency, or dependability, of travel times. To monitor dependability and implement projects and programs that help reduce congestion, Oahu Metropolitan Planning Organization (OahuMPO) will track the percentage of persons-miles traveled on non-interstate routes that are [reliable](https://www.fhwa.dot.gov/tpm/).",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

with tab2:
    st.markdown("## Improve coordination between land use and transportation")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/ompo/percent_of_population_living_in_transit-oriented_development_zones.csv",
            title = "Percent of population living in transit-oriented development zones",
            title_hover = "Land use has a tremendous impact on transportation policy, as the location of services impact the location of transportation resources (such as bus routes and roads) that are required to reach them. To ensure coordination between land use and transportation Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people living in transit- oriented development zones using Census Population data.",
            is_federal_measure = False,
            source = "State of Hawaii GIS Program - Transit Oriented Development Zones and the OahuMPO Traffic Analysis Zones"
        )
    with col2:
        make_plot(
            path = "./data/land_use_and_transportation/ompo/percent_of_population_living_in_transit-oriented_development_zones.csv",
            title = "Percent of population working in transit-oriented development zones",
            title_hover = "Land use has a tremendous impact on transportation policy, as the location of services impact the location of transportation resources (such as bus routes and roads) that are required to reach them. To ensure coordination between land use and transportation, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people working in transit-oriented development zones using Census Population data.",
            is_federal_measure = False,
            source = "State of Hawaii GIS Program - Transit Oriented Development Zones and the OahuMPO Traffic Analysis Zones"
        )
    col1.write("---");
    col2.write("---");

    st.markdown("## Improve transit reliability")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/ompo/percent_of_transit_trips_completed_on_time.csv",
            title = "Percent of transit trips completed on time",
            title_hover = "Improving transit reliability increases its appeal, encouraging more people to select transit for commuting and everyday destinations. To monitor reliability, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit trips completed on time. Transit trips are considered on time if the transit vehicle is within a range of 2 minutes early to 5 minutes late.",
            is_federal_measure = False,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    col1.write("---");
    col2.write("---");

    st.markdown("## Improve the reliability and efficiency of highway freight networks")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/land_use_and_transportation/ompo/level_of_travel_time_reliability_lottr_miles_that_are_reliable_lottr__15_on_the_national_highway_system_nhs.csv",
            title = "Level of Travel Time Reliability (LOTTR) miles that are reliable (LOTTR < 1.5) on the National Highway System (NHS)",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )
