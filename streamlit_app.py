import streamlit as st
from datetime import datetime, time


def main():
    st.header("st.slider")
    # Example 1
    st.subheader("Slider")

    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I'am ", age, "years old.")

    # Example 2
    st.subheader("Range slieder")

    values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
    st.write("values", values)

    # Example 3
    st.subheader("Range time slider")
    appointment = st.slider(
        "Schedule your appoinmtment:", value=(time(11, 30), time(12, 45))
    )
    st.write("You scheduled for:", appointment)

    # Example 4
    st.subheader("Datetime slider")
    start_time = st.slider(
        "When dou you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/Dd/YY - hh:mm",
    )
    st.write("Start time", start_time)


if __name__ == "__main__":
    main()
