import streamlit as st


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs / 2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg * 2.2046


def main():
    st.title("st.session_state")

    st.header("Input")

    col1, spacer, col2 = st.columns([2, 1, 1])

    with col1:
        pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)

    with col2:
        kilogram = st.number_input("Kilograms", key="kg", on_change=kg_to_lbs)

    st.header("Output")
    st.write("st.session_state object: ", st.session_state)


if __name__ == "__main__":
    main()
