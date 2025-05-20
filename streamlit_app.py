import streamlit as st


def main():
    st.title("st.form")

    st.header("1. Example of usin `with` notation")
    st.subheader("Coffee machine")

    with st.form("my_form"):
        st.subheader("**Order your coffee**")

        coffee_bean_val = st.selectbox("Coffee bean", ["Arabica", "Robusta"])
        coffee_roast_val = st.selectbox("Coffee roast", ["light", "Medium", "Dark"])
        brewing_val = st.selectbox(
            "Brewing method",
            ["Aeropress", "Drip", "French press", "Moka pot", "Siphon"],
        )
        serving_type_val = st.selectbox("Serving format", ["Hot", "Iced", "Frappe"])
        own_cup = st.checkbox("Bring own cup")

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.markdown(f"""
            You have ordered:
            - Coffee bean `{coffee_bean_val}`
            - Coffee roast `{coffee_roast_val}`
            - Brewing: ̀`{brewing_val}`
            - Serving type: `{serving_type_val}`
            - Bring own cup : `{own_cup}`

        """)
        else:
            st.write("Place your order")

    st.header("2. Example of object notation")

    form = st.form("my_form_2")
    selected_val = form.slider("Select a value")
    form.form_submit_button("Submit")

    st.write("Selected value :", selected_val)


if __name__ == "__main__":
    main()
