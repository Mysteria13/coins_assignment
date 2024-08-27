import streamlit as st

st.title("coin_assignment")
name = st.text_input('Please enter your name')
gold_coins = st.text_input('Please enter your amount of gold coins')
silver_coins = st.text_input('Please enter your amount of silver coins')
bronze_coins = st.text_input('Please enter your amount of bronze coins')
total_coins,int = gold_coins + silver_coins + bronze_coins
st.write(name,' your total amount of coins are', total_coins)
