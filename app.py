import streamlit as st

st.title("🎨 Guess Rudra's Favorite Color")

fav_color = "blue"

guess = st.text_input("What is Rudra's favorite color?")

if st.button("Submit Guess"):
    if guess.lower() == fav_color.lower():
        st.success("🎉 You guessed correctly, Guru!")
    else:
        st.error("❌ Nope! Try again — তুমি একটা গাধা, গুরু! 🐴😄")
