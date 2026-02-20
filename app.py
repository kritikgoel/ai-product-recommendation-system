import streamlit as st
from openai import OpenAI

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    password = st.text_input("Enter Password", type="password")

    if password:
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state.password_correct = True
        else:
            st.error("Incorrect password")

    return st.session_state.password_correct

if not check_password():
    st.stop()

#OPENAI CLIENT CONFIG
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#FUNCTION TO GET PRODUCTS

def get_products(user_input):
    prompt = f"""
    List 5 {user_input} available in India.

    For each product, provide:
    - Brand
    - Model
    - Price in INR
    - Energy Rating
    - Key Features

    Format properly.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

#FUNCTION FOR PREDICTING PRICES

def get_price_analysis(product_name):
    prompt = f"""
    Give price trends of {product_name} in India.

    Include:
    - 2023 price range (INR)
    - 2024 price range (INR)
    - 2025 price range (INR)
    - 2026 predicted price range (INR)

    Keep it realistic and structured.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

#UI OF THE PROGRAM

st.title("AI Product Recommendation System")

user_input = st.text_input("Enter product (AC, fridge, geyser):")

if st.button("Search"):

    if user_input.strip() == "":
        st.warning("Please enter a product")
    else:
        result = get_products(user_input)

        st.subheader("Available Products")
        st.write(result)

selected_product = st.text_input("Select a product from above:")

if st.button("Get Price Insights"):

    if selected_product.strip() == "":
        st.warning("Please enter a product name")
    else:
        price_data = get_price_analysis(selected_product)

        st.subheader("📊 Price Trends (2023–2026)")
        st.write(price_data)

st.markdown("---")
st.markdown("Made by Kritik with ❤️")
