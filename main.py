import random
import streamlit as st

if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)

st.title("Number Guessing Game")
st.write("Guess a number between 1 and 100")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Check guess"):
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write("🎉 Congratulations! You've guessed the number!")
        st.session_state.number_to_guess = random.randint(1, 100)
