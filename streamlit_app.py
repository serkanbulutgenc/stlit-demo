import streamlit as st


def main():
    st.header("st.multiselect")

    options = st.multiselect(
        "What are your favorite colors",
        ["Greean", "Yellow", "Red", "Blue"],
    )

    st.write("You selected ", options)


if __name__ == "__main__":
    main()
