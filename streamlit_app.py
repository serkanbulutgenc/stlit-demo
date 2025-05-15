import streamlit as st
import pandas as pd


def main():
    st.set_page_config(layout="wide")

    st.title("How to layout your Streamlit app")

    with st.expander("About this app"):
        st.write(
            "This app shows the various ways on how you can layout your streamlit app"
        )
        st.image(
            "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
            width=250,
        )

    st.sidebar.header("Input")
    username = st.sidebar.text_input("What is your name?")
    user_emoji = st.sidebar.selectbox(
        "Choose an emoji", ["", "😄", "😆", "😊", "😍", "😴", "😕", "😱"]
    )
    user_food = st.sidebar.selectbox(
        "What is your favorite food?",
        ["", "Tom Yum Kung", "Burrito", "Lasagna", "Hamburger", "Pizza"],
    )

    st.header("Output")

    col1, col2, col3 = st.columns(3)

    with col1:
        if username != "":
            st.write(f" Hello {username}")
        else:
            st.write("Please enter your **name**")

    with col2:
        if user_emoji != "":
            st.write(f"{user_emoji} is your favorite **emoji**!")
        else:
            st.write("👈 Please choose an **emoji**!")

    with col3:
        if user_food != "":
            st.write(f"🍴 **{user_food}** is your favorite **food**!")
        else:
            st.write("👈 Please choose your favorite **food**!")


if __name__ == "__main__":
    main()
