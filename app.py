import streamlit as st
import pickle

f = open('model.pickle', 'rb')
model = pickle.load(f)

st.subheader('Revenue Predict')
temperator = st.number_input('Input Temperature')


if st.button('Predict'):
  revenue = model.predict([[temperator]])
  st.text('Revenue Predict')
  st.info(revenue.flatten()[0])
