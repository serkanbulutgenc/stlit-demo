import streamlit as st


def main():
    st.title("st.secrets")

    st.write(st.secrets["message"])


if __name__ == "__main__":
    main()
