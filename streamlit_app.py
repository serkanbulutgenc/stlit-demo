import streamlit as st
import pandas as pd
import time


def main():
    st.title("st.progress")

    with st.expander("About this app"):
        st.write(
            "You can now display the progress of your calculations in a Streamlit app with the `st.progress`"
        )

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    st.balloons()


if __name__ == "__main__":
    main()
