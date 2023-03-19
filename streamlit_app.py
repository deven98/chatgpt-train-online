from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write('# Fine-tune an OpenAI model online')

api_key = st.text_input('OpenAPI Secret Key')

model_name = st.text_input('Model name')

option = st.selectbox(
    'Select model type',
    ('davinci', 'curie', 'babbage', 'ada'))

