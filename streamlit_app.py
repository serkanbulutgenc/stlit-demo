import streamlit as st
import pandas as pd


def main():
    st.title("st.file_uploader")

    st.subheader("Input Csv")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("DataFrame")
        st.write(df)
        st.subheader("Descriptive statistics")
        st.write(df.describe())
    else:
        st.info("Upload a CSV file")


if __name__ == "__main__":
    main()
