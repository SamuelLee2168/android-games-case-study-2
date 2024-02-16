import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


st.sidebar.subheader('Table of contents')
st.sidebar.write('1. ','<a href=#introduction>Introduction</a>', unsafe_allow_html=True)
st.sidebar.write('1. ','<a href=#the-top-rated-games>The Top Rated Games</a>', unsafe_allow_html=True)
st.sidebar.write('2. ','<a href=#flipping-coins>"Flipping Coins"</a>', unsafe_allow_html=True)
st.sidebar.write('3. ','<a href=#the-top-installed-games>The Top Installed Games</a>', unsafe_allow_html=True)
st.sidebar.write('4. ','<a href=#the-best-categories-of-games>The Best Categories of Games</a>', unsafe_allow_html=True)
st.sidebar.write('5. ','<a href=#the-extreme-difference>The Extreme Difference</a>', unsafe_allow_html=True)
st.sidebar.write('6. ','<a href=#analyzing-the-rating-of-the-games>Analyzing the Rating of the Games</a>', unsafe_allow_html=True)
st.sidebar.write('7. ','<a href=#the-percentage-of-free-games>The Percentage of Free Games</a>', unsafe_allow_html=True)


st.header('Android Games Data Analysis')

st.markdown('August 13th, 2021, by Samuel Lee')

st.subheader('Introduction')

games = pd.read_csv("android-games.csv")
