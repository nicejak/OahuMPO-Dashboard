import streamlit as st
from make_plot import make_plot, make_chart_table

st.set_page_config(layout="wide")
st.logo("./images/logo-ompo-02.svg")

col1, col2 = st.columns([0.35, 0.65], vertical_alignment = "center")
col1.image("./images/Maintenance.png")
col2.markdown("""
    ## 2050 Goal: Maintenance
    # Maintaining transportation facilities prevents the need for future repairs. To help preserve our network, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of roadways, bridges, transit vehicles, and facilities that are in good condition, along with those that are in need of improvements.
""")

st.divider()

tab1, tab2 = st.tabs(["Federally Required Performance Measures", "OahuMPO Performance Measures"])

with tab1:
    st.markdown("""
    ## Ensure roadways and bridges are in good condition
    """)

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/maintenance/federally_required/interstate_pavement_percent_in_good_condition.csv",
            title = "Interstate Pavement Percent in Good Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percent of interstate pavement lane miles in good condition as provided by the State of Hawaii Department of Transportation. The Federal Highways Administration (FHWA) measures condition using pavement condition metrics including the international roughness index (IRI), cracking percent, rutting, faulting, and present serviceability rating (PSR). There are [specific thresholds](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) indicated by the FHWA to indicate if the metric receives a good or poor. If three or more metrics meet the criteria for good, the pavement section is considered to be in good condition.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/maintenance/federally_required/interstate_pavement_percent_in_poor_condition.csv",
            title = "Interstate Pavement Percent in Poor Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percent of interstate pavement lane miles in good condition as provided by the State of Hawaii Department of Transportation. The Federal Highways Administration (FHWA) measures condition using pavement condition metrics including the international roughness index (IRI), cracking percent, rutting, faulting, and present serviceability rating (PSR). There are [specific thresholds](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) indicated by the FHWA to indicate if the metric receives a good or poor. If three or more metrics meet the criteria for poor, the pavement section is considered to be in poor condition.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/maintenance/federally_required/national_highway_system_nhs_non-interstate_percent_in_good_condition.csv",
            title = "National Highway System (NHS) Non-Interstate Percent in Good Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percent of interstate pavement lane miles in good condition as provided by the State of Hawaii Department of Transportation. The Federal Highways Administration (FHWA) measures condition using pavement condition metrics including the international roughness index (IRI), cracking percent, rutting, faulting, and present serviceability rating (PSR). There are [specific thresholds](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) indicated by the FHWA to indicate if the metric receives a good or poor. If three or more metrics meet the criteria for good, the pavement section is considered to be in good condition.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    with col2:
        make_plot(
            path = "./data/maintenance/federally_required/national_highway_system_nhs_non-interstate_percent_in_poor_condition.csv",
            title = "National Highway System (NHS) Non-Interstate Percent in Poor Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of interstate pavement lane miles in good condition as provided by the State of Hawaii Department of Transportation. The Federal Highways Administration (FHWA) measures condition using pavement condition metrics, including the international roughness index (IRI), cracking percent, rutting, faulting, and present serviceability rating (PSR). There are [specific thresholds](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) indicated by the FHWA to indicate if the metric receives a good or poor. If three or more metrics meet the criteria for poor, the pavement section is considered to be in poor condition..",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/maintenance/federally_required/national_highway_system_nhs_bridges_percent_in_good_condition.csv",
            title = "National Highway System (NHS) Bridges Percent in Good Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of NHS bridges in good condition as provided by the State of Hawaii Department of Transportation. The [Federal Highways Administration (FHWA)](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) measures conditions based on the following criteria: deck, superstructure, structure, and culverts. A bridge is in good condition when each of the criteria obtains a “good condition” rating.",
            is_federal_measure = True,
            source = "State of Hawaii Department of Transportation"
        )
    with col2:
        make_plot(
            path = "./data/maintenance/federally_required/national_highway_system_nhs_bridges_percent_in_poor_condition.csv",
            title = "National Highway System (NHS) Bridges Percent in Poor Condition",
            title_hover = "To maintain compliance with federally required performance measures, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of NHS bridges in good condition as provided by the State of Hawaii Department of Transportation. The [Federal Highways Administration (FHWA)](https://www.ecfr.gov/current/title-23/chapter-I/subchapter-E/part-490) measures conditions based on the following criteria: deck, superstructure, structure, and culverts. A bridge is in poor condition when each of the criteria obtains a “poor condition” rating.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    st.divider()
    st.markdown("## Ensure transit vehicles and facilities are in good condition")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/maintenance/federally_required/percent_of_revenue_vehicles_exceeding_the_useful_life_benchmark_ulb.csv",
            title = "Percent of revenue vehicles exceeding the useful life benchmark (ULB)",
            title_hover = "The [Federal Transit Agency (FTA)](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-VI/part-625) has a set default Useful Life Benchmark (ULB) for specific vehicle classes, and a vehicle needs to reach specific benchmarks on the FTA Transit Economic Requirements Model (TERM) scale to be compliant. To ensure compliance, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit revenue vehicles that have met or exceeded their useful life benchmark, as provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    with col2:
        make_plot(
            path = "./data/maintenance/federally_required/percent_of_non-revenue_vehicles_exceeding_the_useful_life_benchmark_ulb.csv",
            title = "Percent of non-revenue vehicles exceeding the useful life benchmark (ULB)",
            title_hover = "The [Federal Transit Agency (FTA)](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-VI/part-625) has a set default Useful Life Benchmark (ULB) for specific vehicle classes, and a vehicle needs to reach specific benchmarks on the FTA Transit Economic Requirements Model (TERM) scale to be compliant. To ensure compliance, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit non-revenue, support-service, and maintenance vehicles that have met or exceeded their useful life benchmark, as provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

    col1.write("---");
    col2.write("---");

    with col1:
        make_plot(
            path = "./data/maintenance/federally_required/percentage_of_assets_with_condition_rating_below_30_on_fta_transit_economic_requirements_model_term_scale.csv",
            title = "Percentage of assets with condition rating below 3.0 on FTA Transit Economic Requirements Model (TERM) scale",
            title_hover = "The [Federal Transit Agency (FTA)](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-VI/part-625) has a set default Useful Life Benchmark (ULB) for specific vehicle classes, and a vehicle needs to reach specific benchmarks on the FTA Transit Economic Requirements Model (TERM) scale to be compliant. To ensure compliance, Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit facilities rated below condition 3 on the TERM scale, as provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = True,
            source = "City and County of Honolulu - Department of Transportation Services"
        )

with tab2:
    st.markdown("## Ensure transit vehicles and facilities are in good condition")

    col1, col2 = st.columns(2, border = True)

    with col1:
        make_plot(
            path = "./data/maintenance/ompo/percent_of_transit_inspections_completed_on_time.csv",
            title = "Percent of (transit) inspections completed on time",
            title_hover = "The National Transit Asset Management (TAM) system, established by [49 CFR 625](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-VI/part-625), monitors and manages the State of Good Repair (SGR) of public transportation capital assets to enhance safety, reduce maintenance costs, increase reliability, and improve performance. Although it is not a federally required performance measure, the Oahu Metropolitan Planning Organization (OahuMPO) will monitor the percentage of transit inspections completed on time, as provided by the City and County of Honolulu Department of Transportation Services.",
            is_federal_measure = False,
            source = "State of Hawaii Department of Transportation"
        )
