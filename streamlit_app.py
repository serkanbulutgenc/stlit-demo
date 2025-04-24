import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


def main():
    st.header("st.write")
    # Example 1
    st.write("Hello, *World!* :sunglasses:")

    # Example 2
    st.write(1234)

    # Example 3
    df = pd.DataFrame({"first_col": [1, 2, 3, 4], "second_col": [10, 20, 30, 40]})
    st.write(df)

    # Example 4
    st.write("Below is a Dataframe:", df, "Above is a dataframe.")

    # Example 5
    df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
    c = (
        alt.Chart(df2)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )
    st.write(c)


if __name__ == "__main__":
    main()
