import streamlit as st


def main():
    st.header("st.checkbox")

    st.write("What would you like to order?")

    icecream = st.checkbox("Ice cream", key="icecream")
    coffee = st.checkbox("Coffee")
    cola = st.checkbox("Cola")

    if icecream:
        st.write("Great! Here's come more")
    if coffee:
        st.write("Okay, here's some coffee")
    if cola:
        st.write("Here you go")


if __name__ == "__main__":
    main()
