import streamlit as st
import numpy as np
import pandas as pd


def main():
    st.header("Lİne Chart")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.line_chart(chart_data, x_label="X label", y_label="Y label")


if __name__ == "__main__":
    main()
