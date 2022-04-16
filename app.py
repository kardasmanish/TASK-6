import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import base64

pickle_in = open("classifier_rf.pkl","rb")
classifier = pickle.load(pickle_in)

main_bg = "background.jpg"
main_bg_ext = "jpg"


def welcome():
    return "welcome All"

def fraud_prediction(Product_cd,Transaction_Amount,card1_Amount,card2_Amount,addr1):
    prediction = classifier.predict([[Product_cd,Transaction_Amount,card1_Amount,card2_Amount,addr1]])
    return prediction[0]
def main():
    st.title("TASK 6!")
    st.text("This is an webapp created using streamlit featuring the ML Model")
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    html_temp = """
    <body background='background.png'>
    <div style = "background-color:DarkOrange;padding:10px">
    <h2 style = "color:white;text-align:center;"> Fraud Transaction Detection </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html= True)
    Product_cd = st.selectbox("Product_cd",['w','H','C','S','R'])
    Transaction_Amount = st.text_input(" Transaction Amount ","Enter the amount")
    card1_Amount = st.text_input("Card 1","Enter the amount")
    card2_Amount = st.text_input("Card 2 ","Enter the amount")
    addr1 = st.text_input("Address","Enter the address")
    result = ""
    if st.button("Predict"):
        result = fraud_prediction(Product_cd,Transaction_Amount,card1_Amount,card2_Amount,addr1)
        st.success("The transaction is ".format(result))

if __name__ == "__main__":
    main()
