import streamlit as st
import numpy as np
import pandas as pd
from time import perf_counter


@st.cache_data(show_spinner=True)
def load_data_a():
    print("cache data")
    df = pd.DataFrame(np.random.randn(2000000, 5), columns=[*"abcde"])
    return df


def load_data_b():
    print("not caching data")
    df = pd.DataFrame(np.random.randn(2000000, 5), columns=[*"abcde"])
    return df


def main():
    a0 = perf_counter()

    st.title("st.cache")

    st.subheader("Using st.cache")

    st.write(load_data_a())
    a1 = perf_counter()
    st.info(a1 - a0)

    a0 = perf_counter()

    st.subheader("Not Using st.cache")

    st.write(load_data_b())
    a1 = perf_counter()
    st.info(a1 - a0)


if __name__ == "__main__":
    main()
