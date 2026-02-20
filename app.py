import streamlit as st
from openai import OpenAI

# OpenAI client intializing

client = OpenAI(api_key="ENTER_YOUR_OPENAI_APIKEY")

# Fn 1: Product recommendations fetch

def get_products(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a product recommendation assistant."},
            {"role": "user", "content": f"List 5 {user_input} with brand, model, and key specifications."}
        ]
    )
    return response.choices[0].message.content

# Fn 2: Fetching price trends 

def get_price_analysis(product_name):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Give price trends of {product_name} from 2023 to 2026 with approximate values in INR (₹). Mention prices clearly in Indian Rupees."}
        ]
    )
    return response.choices[0].message.content

#UI of the system

st.title("AI Product Recommendation System")

user_input = st.text_input("Enter product (AC, fridge, geyser):")

if st.button("Search"):
    result = get_products(user_input)
    st.write(result)

selected_product = st.text_input("Select a product from above:")

if st.button("Get Price Insights"):
    price = get_price_analysis(selected_product)
    st.write(price)

st.markdown("---")
st.markdown("Made by Kritik with ❤️")