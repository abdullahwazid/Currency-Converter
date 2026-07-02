import json
import streamlit as st 

st.title("Currency Converter")

#importing currencies from json folder
with open("currencies.json", "r", encoding="utf-8") as file : 
    currencies = json.load(file)

from_currency = st.selectbox(
    "From",
    currencies,
    key = "from_currency",
    format_func=lambda currency : 
        f'{currency["flag"]} {currency["code"]} - {currency["name"]}'
)

to_currency = st.selectbox(
    "To",
    currencies,
    key = "from_currency",
    format_func=lambda currency : 
        f'{currency["flag"]} {currency["code"]} - {currency["name"]}'
)

from_amount = st.number_input(
    f'{from_currency["code"]}',
    min_value = 0.00,
    value = 1.0,
    step = 0.10,
)


