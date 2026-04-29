import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Safety_Header.png")
col2.markdown("""
    ## 2050 Goal: Safety
    # Reduce serious injuries and traffic deaths to zero
    Prioritizing safety to achieve vision zero requires a focus on key metrics that highlight the risks on our roads. Oahu Metropolitan Planning Organization (OahuMPO) is focused on prioritizing safety in the planning, design, and selection of projects; reducing dangerous driving behaviors, and implementing safety plans for transit. Central to this effort includes monitoring fatalities and serious injuries, both motorized and non-motorized, crashes involving dangerous driving behaviors, and safety incidents on transit.
""")

st.divider()

tab1, tab2 = st.tabs(["Federally Required Performance Measures", "OahuMPO Performance Measures"])

with tab1:
    st.markdown("""
    ## Prioritize safety in the planning, design, and selection of projects
    """)

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/safety/federally_required/number_of_fatalities.csv",
            title = "Number of fatalities",
            title_hover = "To determine ways to decrease traffic fatalities and serious injuries, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the number of fatalities on Oahu's roadways through data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/safety/federally_required/number_of_serious_injuries.csv",
            title = "Number of serious injuries",
            title_hover = "To determine ways to decrease traffic fatalities and serious injuries, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the number of serious injuries on Oahu's roadways through data provided by the State of Hawaii Department of Transportation. The State of Hawaii Department of Transportation provides specific injury types identified as serious injuries in the [Hawaii Strategic Highway Safety Plan](https://hidot.hawaii.gov/highways/files/2024/11/241113-Final-SHSP-with-Appendices-508-Compliant_reduced.pdf).",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )
    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/safety/federally_required/rate_of_fatalities.csv",
            title = "Rate of fatalities",
            title_hover = "To determine ways to decrease traffic fatalities and serious injuries, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the rate of fatalities on Oahu's roadways through data provided by the State of Hawaii Department of Transportation. The rate of fatalities per 100 million vehicle miles traveled will be calculated by dividing the number of fatalities on Oahu's roadways by Vehicle Miles Traveled.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/safety/federally_required/rate_of_serious_injuries.csv",
            title = "Rate of serious injuries",
            title_hover = "To determine ways to decrease traffic fatalities and serious injuries, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the rate of serious injuries on Oahu's roadways through data provided by the State of Hawaii Department of Transportation. The rate of serious injuries per 100 million vehicle miles traveled will be calculated by dividing the number of fatalities on Oahu's roadways by Vehicle Miles Traveled. The State of Hawaii Department of Transportation provides specific injury types identified as serious injuries in the [Hawaii Strategic Highway Safety Plan](https://hidot.hawaii.gov/highways/files/2024/11/241113-Final-SHSP-with-Appendices-508-Compliant_reduced.pdf).",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/safety/federally_required/number_of_non-motorized_fatalities_and_non-motorized_serious_injuries.csv",
            title = "Number of non-motorized fatalities and non-motorized serious injuries",
            title_hover = "To determine ways to decrease traffic fatalities and serious injuries for [vulnerable road users](https://hidot.hawaii.gov/highways/files/2023/11/Final_VRUSA_2023.pdf), Oahu Metropolitan Planning Organization (OahuMPO) will monitor the number of non-motorized fatalities on Oahu's roadways through data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    st.divider()
    st.markdown("## Implement safety plans for transit")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/safety/federally_required/transit_total_number_of_fatalities.csv",
            title = "Total number of fatalities on transit",
            title_hover = "To support the implementation of transit safety plans, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the number of fatalities by transit mode, as provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    with col2:
        make_plot(
            path = "./data/safety/federally_required/transit_fatality_rate_per_100000_vehicle-revenue_miles.csv",
            title = "Fatality rate per 100,000 vehicle-revenue miles on transit",
            title_hover = "To assist in the development and implementation of transit safety plans, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the rate of fatalities by transit mode per 100,000 vehicle revenue miles. This data is provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/safety/federally_required/transit_total_number_of_injuries.csv",
            title = "Total number of injuries on transit",
            title_hover = "To assist in the development and implementation of transit safety plans, Oahu Metropolitan Planning Organization (OahuMPO) will monitor number of injuries by transit mode. This data is provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    with col2:
        make_plot(
            path = "./data/safety/federally_required/transit_injury_rate_per_100000_vehicle-revenue_miles.csv",
            title = "Injury rate per 100,000 vehicle-revenue miles on transit",
            title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will monitor the rate of injuries by transit mode per 100,000 vehicle revenue miles, as provided by the City and County of Honolulu Department of Transportation Services, to assist in in the development and implementation of transit safety plans.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/safety/federally_required/transit_total_number_of_safety_events.csv",
            title = "Total number of safety events on transit",
            title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will monitor the number of safety events by transit mode, as provided by the City and County of Honolulu Department of Transportation Services, to assist in the development and implementation of transit safety plans.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    with col2:
        make_plot(
            path = "./data/safety/federally_required/transit_rate_of_safety_events_per_100000_vehicle-revenue_miles.csv",
            title = "Rate of safety events per 100,000 vehicle-revenue miles on transit",
            title_hover = "Oahu Metropolitan Planning Organization (OahuMPO) will monitor the rate of safety events by transit mode per 100,000 vehicle revenue miles, as provided by the City and County of Honolulu Department of Transportation Services, to assist in the development and implementation of transit safety plans.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

with tab2:
    st.markdown("## Reduce dangerous driving behaviors such as speeding, impaired, distracted, and reckless driving")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/safety/ompo/percent_of_crashes_involving_impaired_driving.csv",
            title = "Percent of crashes involving impaired driving",
            title_hover = "Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety. To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes involving impaired driving using data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/safety/ompo/percent_of_crashes_involving_distracted_driving.csv",
            title = "Percent of crashes involving distracted driving",
            title_hover = "Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety. To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes that involve distracted driving. This will be sourced from data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )
    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/safety/ompo/percent_of_crashes_involving_reckless_driving.csv",
            title = "Percent of crashes involving reckless driving",
            title_hover = "Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety. To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes involving [reckless driving](https://www.capitol.hawaii.gov/hrscurrent/Vol05_Ch0261-0319/HRS0291/HRS_0291-0002.htm) using data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/safety/ompo/percent_of_crashes_involving_speed.csv",
            title = "Percent of crashes involving speed",
            title_hover = "Focusing on reducing dangerous driving behaviors causing the highest number and proportion of crashes allows a targeted and efficient approach to improving overall safety. To target appropriate policies and programs to address dangerous driving behaviors, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of crashes involving speeding driving using data provided by the State of Hawaii Department of Transportation.",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )
