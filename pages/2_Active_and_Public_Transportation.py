import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Active_and_Public_Transportation_Header.png")
col2.markdown("""
    ## 2050 Goal: Active and public transportation
    # Enhance the transportation network to increase active and public transportation
    Increasing active and public transportation can have significant implications for public health and the environment. Oahu Metropolitan Planning Organization (OahuMPO) is focused on increasing the number of people who walk, bike and utilize transit while also reducing the percentage of people driving alone. Key to this effort includes monitoring pedestrian and bicyclist counts, transit ridership, and the percentage of people who drive alone.
""")

st.divider()

st.markdown("""
## Prioritize safety in the planning, design, and selection of projects
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_walk_to_work.csv",
        title = "Percent of people who walk to work",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who walk and bike to work, using data from the United States Census Bureau American Community Survey.",
        is_federal_measure = False,
        source = "United States Census Bureau, American Community Survey - Commuting Characteristics by Sex",
    )

with col2:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_bike_to_work.csv",
        title = "Percent of people who bike to work",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who walk and bike to work, using data from the United States Census Bureau American Community Survey.",
        is_federal_measure = False,
        source = "United States Census Bureau, American Community Survey - Commuting Characteristics by Sex"
    )
col1.write("---");
col2.write("---");
with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_teens_that_walk_bike_or_wheelchair_to_school.csv",
        title = "Percent of teens that walk, bike, or wheelchair to school",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of teens in grades 9 through 12 that walk, bike, or wheelchair to school, using data from Hawaii Health Matters.",
        is_federal_measure = False,
        source = "Hawaii Health Matters"
    )

with col2:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/monthly_average_bike_counts.csv",
        title = "Monthly average bike counts",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. To evaluate the number of people who bike, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the monthly average bike counts using data provided by the City and County Department of Transportation Active Transportation Project. This program was partially funded by Oahu Metropolitan Planning Organization (OahuMPO).",
        is_federal_measure = False,
        source = "City and County of Honolulu - Department of Tranpsortation Services"
    )
col1.write("---");
col2.write("---");
with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/monthly_average_pedestrian_counts.csv",
        title = "Monthly average pedestrian counts",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. To evaluate the number of people who walk, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the monthly average pedestrian counts using data provided by the City and County Department of Transportation Active Transportation Project. This program was partially funded by Oahu Metropolitan Planning Organization (OahuMPO).",
        is_federal_measure = False,
        source = "City and County of Honolulu - Department of Tranpsortation Services"
    )

with col2:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/monthly_average_scooter_counts.csv",
        title = "Monthly average scooter counts",
        title_hover = "The United States Department of Transportation notes that increasing active transportation has important implications on improving physical and mental health, reducing congestion, improving transportation and community resilience, and spurring economic growth. To evaluate the number of people who scooter, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the monthly average scooter counts using data provided by the City and County Department of Transportation Active Transportation Project. This program was partially funded by Oahu Metropolitan Planning Organization (OahuMPO).",
        is_federal_measure = False,
        source = "City and County of Honolulu - Department of Tranpsortation Services"
    )

st.divider()
st.markdown("""
## Increase the number of people who utilize transit
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/transit_ridership_per_capita.csv",
        title = "Transit ridership per capita",
        title_hover = "According to the American Public Transportation Association, public transit provides a multitude of benefits including safer ways to travel, cost savings for consumers, as well as reduction in gasoline consumption and carbon emissions. To support projects and programs that increase the number of people who utilize transit, Oahu Metropolitan Planning Organization (OahuMPO) will monitor per capita transit ridership, as provided by the City and County of Honolulu Department of Transportation Services.",
        is_federal_measure = False,
        source = "City and County of Honolulu - Department of Tranpsortation Services"
    )

with col2:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_live_within_a_10-minute_walk_to_a_rail_station.csv",
        title = "Percent of people who live within a 10-minute walk to a rail station",
        title_hover = "According to the American Public Transportation Association, public transit provides a multitude of benefits including safer ways to travel, cost savings for consumers, as well as reduction in gasoline consumption and carbon emissions. To support projects and programs that increase the number of people who utilize transit, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who live within a 10-minute walk of a rail station using data from the United States Census Bureau.",
        is_federal_measure = False,
        source = "State of Hawaii GIS Program - Rail Station Locations and OahuMPO Traffic Analysis Zones"
    )
col1.write("---");
col2.write("---");
with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_work_within_a_10-minute_walk_to_a_rail_station.csv",
        title = "Percent of people who work within a 10-minute walk to a rail station",
        title_hover = "According to the American Public Transportation Association, public transit provides a multitude of benefits including safer ways to travel, cost savings for consumers, as well as reduction in gasoline consumption and carbon emissions. To support projects and programs that increase the number of people who utilize transit, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who work within a 10-minute walk of a rail station using data from the United States Census Bureau.",
        is_federal_measure = False,
        source = "State of Hawaii GIS Program - Rail Station Locations and OahuMPO Traffic Analysis Zones"
    )

with col2:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_live_within_a_5-minute_walk_to_a_bus_stop.csv",
        title = "Percent of people who live within a 5-minute walk to a bus stop",
        title_hover = "According to the American Public Transportation Association, public transit provides a multitude of benefits including safer ways to travel, cost savings for consumers, as well as reduction in gasoline consumption and carbon emissions. To support projects and programs that increase the number of people who utilize transit, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who live within a 5-minute walk of a bus stop using data from the United States Census Bureau.",
        is_federal_measure = False,
        source = "State of Hawaii GIS Program - Rail Station Locations and OahuMPO Traffic Analysis Zones"
    )
col1.write("---");
col2.write("---");
with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_who_work_within_a_5-minute_walk_to_a_bus_stop.csv",
        title = "Percent of people who work within a 5-minute walk to a bus stop",
        title_hover = "According to the American Public Transportation Association, public transit provides a multitude of benefits including safer ways to travel, cost savings for consumers, as well as reduction in gasoline consumption and carbon emissions. To support projects and programs that increase the number of people who utilize transit, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people who work within a 5-minute walk of a bus stop using data from the United States Census Bureau.",
        is_federal_measure = False,
        source = "State of Hawaii GIS Program - Rail Station Locations and OahuMPO Traffic Analysis Zones"
    )

st.divider()
st.markdown("""
## Reduce the percentage of people driving alone
""")

col1, col2 = st.columns(2, border = True)

with col1:
    make_plot(
        path = "./data/active_and_public_transportation/ompo/percent_of_people_driving_alone_to_work.csv",
        title = "Percent of people driving alone to work",
        title_hover = "Driving alone to work has significant implications on consumer health and the environment, yet it is still the most common way Americans commute to work. Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of people driving to work, using data obtained through the United States Census Bureau American Community Survey.",
        is_federal_measure = False,
        source = "United States Census Bureau, American Community Survey - Commuting Characteristics by Sex"
    )
