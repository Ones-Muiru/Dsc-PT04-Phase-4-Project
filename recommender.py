import streamlit as st
import pickle

with open('./Group_23.ipynb/final_svd_model.pkl','rb') as file:
    model = pickle.load(file)

user_id = st.number_input('User ID')
item_id = st.number_input('Item ID')
hybrid_rating = st.number_input('Item Rating')
    
st.write('Hello world!')