import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm

from black_scholes import BlackScholes


st.title('Options Pricing Models')
st.write('Creator: Arnav Khurma')

with st.sidebar:
    # Default values set for each input
    underlying_price = st.number_input(
        "Current Underlying Asset Price", 
        min_value=0.0, 
        max_value=None, 
        value=100.0,  # Default value set to 100.0
        step=1.0, 
        format=None, 
        key=None, 
        help=None, 
        on_change=None, 
        args=None, 
        kwargs=None, 
        placeholder="Underlying Price", 
        disabled=False, 
        label_visibility="visible"
    )

    strike_price = st.number_input(
        "Option Strike Price", 
        min_value=0.0, 
        max_value=None, 
        value=95.0,  # Default value set to 95.0
        step=1.0, 
        format=None, 
        key=None, 
        help=None, 
        on_change=None, 
        args=None, 
        kwargs=None, 
        placeholder="None", 
        disabled=False, 
        label_visibility="visible"
    )

    time_to_maturity = st.number_input(
        "Time to Maturity (Years)", 
        min_value=0.0, 
        max_value=None, 
        value=1.0,  # Default value set to 1.0 (1 year)
        step=0.1, 
        format=None, 
        key=None, 
        help=None, 
        on_change=None, 
        args=None, 
        kwargs=None, 
        placeholder="None", 
        disabled=False, 
        label_visibility="visible"
    )

    risk_free_rate = st.number_input(
        "Risk-Free Return Rate", 
        min_value=0.0, 
        max_value=None, 
        value=0.05,  # Default value set to 0.05 (5%)
        step=0.01, 
        format=None, 
        key=None, 
        help=None, 
        on_change=None, 
        args=None, 
        kwargs=None, 
        placeholder="None", 
        disabled=False, 
        label_visibility="visible"
    )

    sigma = st.number_input(
        "Volatility (σ)", 
        min_value=0.0, 
        max_value=None, 
        value=0.2,  # Default value set to 0.2 (20%)
        step=0.01, 
        format=None, 
        key=None, 
        help=None, 
        on_change=None, 
        args=None, 
        kwargs=None, 
        placeholder="None", 
        disabled=False, 
        label_visibility="visible"
    )


# Create an instance of BlackScholes
option = BlackScholes(underlying_price, strike_price, time_to_maturity, risk_free_rate, sigma)

# Print statistics
option.printStats()

# Calculate and print the call and put option prices individually if needed
call_price = option.calculate_call_price()
put_price = option.calculate_put_price()

st.write(f"Call Price: {call_price}")
st.write(f"Put Price: {put_price}")
