import streamlit as st
import pandas as pd
import numpy as np
from colorutils import Color
import plotly.graph_objects as go
import plotly.express as px
from numpy.random import default_rng as rng

def make_chart_table(path, is_bar_chart, xlim, ylim):
    df = pd.read_csv(path, na_values = "-")
    if is_bar_chart:
        fig = go.Figure([
            go.Bar(
                x = df.iloc[:,0],
                y = df.iloc[:,1],
                width = [0.1] * df.shape[0]
            )
        ])
        fig.update_xaxes(tickvals = df.iloc[:,0])
    else:
        if df.shape[0] > 1:
            fig = go.Figure()
            for i in range(1,df.shape[1]):
                original_name = df.columns[i]
                nice_name = original_name.title()
                if "(Target)" not in nice_name:
                    # find the headers that are not targets
                    # plot the original data
                    fig.add_trace(
                        go.Scatter(
                            x = df.iloc[:,0],
                            y = df.iloc[:,i],
                            name = nice_name,
                            line=dict(color = px.colors.qualitative.Plotly[i-1]),
                        )
                    )
                    # plot the target data
                    try:
                        fig.add_trace(
                            go.Scatter(
                                x = df.iloc[:,0],
                                y = df[original_name + " (Target)"],
                                name = nice_name + " (Target)",
                                line = dict(color = (Color(hex = px.colors.qualitative.Plotly[i-1]) - Color((50,35,35))).hex, dash = 'dash'),
                                # mode = 'lines'
                            )
                        )
                    except KeyError:
                        print("No target found for " + path)
            fig.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            ))
            fig.update_traces(hoverinfo='name+x+y', mode='lines+markers')

        elif df.shape[0] == 1:
            labels = ["Percent that is", "Percent that isn't"]
            values = [df.iloc[0,1], 100-df.iloc[0,1]]
            colors = [px.colors.qualitative.Plotly[0],px.colors.qualitative.Plotly[1]]
            fig = go.Figure(data=[go.Pie(labels = labels, values=values)])
            fig.update_traces(
                hoverinfo='label+percent',
                textinfo='value',
                textfont_size=20,
                marker=dict(colors = colors, line = dict(color='#000000', width=1))
            )
            fig.update_layout(showlegend=False)
    fig.update_xaxes(range = xlim)
    fig.update_yaxes(range = ylim)

    tab_chart, tab_table = st.tabs(["Chart", "Table"])

    with tab_chart:
        st.plotly_chart(fig, config = {"scrollZoom": False})
    with tab_table:
        st.dataframe(df)

def make_plot(path, title, title_hover, is_federal_measure, source, is_bar_chart = False, ymin = None, ymax = None, xmin = None, xmax = None):
    # First, download the data
    df = pd.read_csv(path, na_values = "-")

    # Write down a title and help according to input
    st.markdown(
        "### " + title,
        help = title_hover
    )

    # If is_federal_measure = True, then add a tag
    if is_federal_measure:
        st.markdown(":small[Federally Required Performance Measure]")

    # Put down the plot using the path
    make_chart_table(path, is_bar_chart, [xmin, xmax], [ymin, ymax])

    # Put down the source
    st.markdown(":small[Data source: " + source + "]")
