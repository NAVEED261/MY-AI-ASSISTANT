

# prompt: MAKE CURRENCY CONVERTER APP , FIRST IS SOURCE WHICH IS PKR AND 2NS IS TARGET WHICH IS  USD, EUR, GBP, YEN ,JPY, INR, SAR , DINAR, DIRHEM AND IN LAST OPTION IS TOTEL CALCULATIONS , THEN LIVE ON STREAMLIT



import streamlit as st
from forex_python.converter import CurrencyRates

def currency_converter(amount, source_currency, target_currency):
  c = CurrencyRates()
  try:
    rate = c.get_rate(source_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount
  except Exception as e:
    st.error(f"Error converting currency: {e}")
    return None

st.title("Currency Converter")

amount = st.number_input("Enter amount in PKR:", min_value=0.0)
source_currency = "PKR"

target_currency = st.selectbox("Select target currency:",
                                ["USD", "EUR", "GBP", "JPY", "INR", "SAR", "KWD", "AED"])

if st.button("Convert"):
  converted_amount = currency_converter(amount, source_currency, target_currency)
  if converted_amount is not None:
    st.success(f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}")

if st.button("Total Calculations"):
  # Add logic to display all conversions (optional)
  st.write("Total Calculations feature will be added soon!")
