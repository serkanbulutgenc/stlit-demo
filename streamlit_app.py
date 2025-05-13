import streamlit as st


def main():
    st.header("st.selectbox")

    option = st.selectbox(
        "What is your favorite color?",
        ("Blue", "Red", "Green"),
        index=None,
        placeholder="Choose an option",
    )

    st.write("Your favorie color is ", option)


if __name__ == "__main__":
    main()
