import streamlit as st


def main():
    st.title("st.experimental_get_query_params")

    with st.expander("about the app"):
        st.write(
            "`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser."
        )

    st.header("1. Instructions")
    st.markdown("""
    In the above URL bar of your internet browser, append the folowing:
                `?firstname=Jack&surname=Beanstalk`
                after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`

""")

    st.header("2. Contents of st.experimantal_get_query_params")
    st.write(st.query_params)

    st.header("3. Retrieving and dispalying information from the URL")
    firstname = st.query_params["firstname"]
    lastname = st.query_params["lastname"]

    st.write(f"Hello **{firstname} {lastname}** how are you?")


if __name__ == "__main__":
    main()
