import json
import requests
import streamlit as st 

st.title("Currency Converter")

#importing currencies from json folder
with open("currencies.json", "r", encoding="utf-8") as file : 
    currencies = json.load(file)

#defining function for swap
def swap_currencies() : 
    st.session_state.from_currency, st.session_state.to_currency = (
            st.session_state.to_currency,
            st.session_state.from_currency,
        )

#adding colummns for from swap and to currency
col1, col2, col3 = st.columns([4,1,4])

with col1 : 
    from_currency = st.selectbox(
    "From",
    currencies,
    key = "from_currency",
    format_func=lambda currency : 
        f'{currency["flag"]} {currency["code"]} - {currency["name"]}'
)

with col2 : 
    st.write(" ") #spacing
    st.write(" ")
    st.button("🔄", on_click=swap_currencies)

with col3 : 
    to_currency = st.selectbox(
    "To",
    currencies,
    key = "to_currency",
    format_func=lambda currency : 
        f'{currency["flag"]} {currency["code"]} - {currency["name"]}'
)

from_amount = st.number_input(
    f'{from_currency["code"]}',
    min_value = 0.00,
    value = 1.0,
    step = 0.10,
)

#api & conversion
if st.button("Convert") : 
    url = f"https://open.er-api.com/v6/latest/{from_currency['code']}"
    response = requests.get(url)
    data = response.json()

    rate = data["rates"][to_currency["code"]]
    converted_amount = from_amount * rate
    
    st.success(
        f"{from_amount:.2f} {from_currency['code']} = "
        f"{converted_amount:.6f} {to_currency['code']}"
    )
