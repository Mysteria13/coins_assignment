import streamlit as st

st.title("coin_assignment")
st.write name = st.text_input('Please enter your name')
st.write gold_coins = st.text_input('Please enter your amount of gold coins')
st.write silver_coins = st.text_input('Please enter your amount of silver coins')
st.write bronze_coins = st.text_input('Please enter your amount of bronze coins')
total_coins = gold_coins + silver_coins + bronze_coins
st.write(name,' your total amount of coins are', total_coins)
