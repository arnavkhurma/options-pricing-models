import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes

st.set_page_config(
    page_title="Option Pricing Models",
    page_icon="📈",
    layout="wide")

st.title('Options Pricing Models')

with st.sidebar:
    st.title("📊 Options Pricing Models")
    st.write("`Developed by:`")
    linkedin_url = "https://www.linkedin.com/in/arnav-khurma/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" height="20" style="vertical-align: middle; margin-right: 10px;">`Arnav Khurma`</a>', unsafe_allow_html=True)
    st.markdown("---")
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

    time_to_maturity = st.slider('Time to Maturity (Days)', min_value=1.0, max_value=1000.0, value=365.0, step=1.0) / 365

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

    sigma = st.slider('Volatility (σ)', min_value=0.0, max_value=1.0, value=0.2, step=0.01)

    st.markdown("---")
    st.write("Heatmap Parameters")
    spot_min = st.number_input('Minimum Spot Price', min_value=0.01, value=underlying_price*0.8, step=0.01)
    spot_max = st.number_input('Maximum Spot Price', min_value=0.01, value=underlying_price*1.2, step=0.01)
    vol_min = st.slider('Minimum Volatility for Heatmap', min_value=0.01, max_value=1.0, value=sigma*0.5, step=0.01)
    vol_max = st.slider('Maximum Volatility for Heatmap', min_value=0.01, max_value=1.0, value=sigma*1.5, step=0.01)

input_data = {
    "Current Underlying Asset Price": [underlying_price],
    "Strike Price": [strike_price],
    "Time to Maturity (Days)": [time_to_maturity * 365],
    "Risk-Free Rate": [risk_free_rate],
    "Volatility (σ)": [sigma],
}
input_df = pd.DataFrame(input_data)
st.table(input_df)


# Create an instance of BlackScholes
option = BlackScholes(underlying_price, strike_price, time_to_maturity, risk_free_rate, sigma)

# Print statistics
# option.printStats()

# Calculate and print the call and put option prices individually if needed
call_price = option.calculate_call_price()
put_price = option.calculate_put_price()

st.write(f"Call Price: {round(call_price, 2)}")
st.write(f"Put Price: {round(put_price, 2)}")
st.write(f"Call Delta: {round(option.delta('C'), 4)}")
st.write(f"Put Delta: {round(option.delta('P'), 4)}")
st.write(f"Gamma: {round(option.gamma(), 4)}")
st.write(f"Vega: {round(option.vega(), 4)}")
st.write(f"Call Rho: {round(option.rho('C'), 4)}")
st.write(f"Put Rho: {round(option.rho('P'), 4)}")
st.write(f"Call Theta: {round(option.theta('C'), 4)}")
st.write(f"Put Theta: {round(option.theta('P'), 4)}")
