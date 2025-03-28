# streamlit_app.py new 

import streamlit as st
import random as random

#Headers/Initial text 
st.title("Higher or Lower Guessing Game")
st.write("Guess if a number is higher or lower then the next!")

choices = ["Higher", "Lower"]

#Initializing variables 
if "userScore" and "compScore" and "tiedNum" not in st.session_state:
    st.session_state["userScore"] = 0
    st.session_state["compScore"] = 0
    st.session_state["tiedNum"] = 0

#Determine if player was correct 
def winnerIs(userChoice, compChoice1, compChoice2): 
    if userChoice == "Higher" and randomNum1 < randomNum2: 
        st.write("🎉 The next number was higher! You win! 🎉")
        st.session_state["userScore"] += 1
    elif userChoice == "Lower" and randomNum2 < randomNum1: 
        st.write("🎉 The next number was lower! You win! 🎉")
        st.session_state["userScore"] += 1
    elif randomNum1 == randomNum2: 
        st.write("The numbers were the same!")
        st.session_state["tiedNum"] += 1
    else: 
        st.write("😢 Sorry, you lost! 😢")
        st.session_state["compScore"] += 1

#Generate random numbers 
randomNum1 = random.randint(1, 20)
randomNum2 = random.randint(1, 20)

st.write("Do you think the next number is higher or lower then " + str(randomNum1) + "?")
userChoice = st.radio("Select higher or lower: ", choices, key=None)

#Play button 
if st.button("Play"):
    st.write("The next number was " + str(randomNum2))
    winnerIs(userChoice, randomNum1, randomNum2)
    st.write("✅ Times won: " + str(st.session_state["userScore"]))
    st.write("❌ Times lost: " + str(st.session_state["compScore"]))
    st.write("🟰 Times numbers were the same: " + str(st.session_state["tiedNum"]))