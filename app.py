import streamlit as st 
from functions.plot import plot_ts 

st.title("Stock History")
st.write("Look the stock values")

ticker = st.sidebar.text.text_input ('Choose the ticket:', value='AAPL')

fig = plot_ts(ticker)

st.plotly_chart(fig)