import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import zipfile
import os
from colorutils import Color
import plotly.graph_objects as go
import plotly.express as px
from numpy.random import default_rng as rng
from make_plot import make_plot, make_chart_table

df = pd.read_csv("./data/equity/ompo/per_capita_project_expenditures_spent_on_transit_or_active_transportation_in_title_vienvironmental_justice_areas.csv", na_values = "-")

print(df.shape[0])
