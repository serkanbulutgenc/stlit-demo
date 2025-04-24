import streamlit as st


@st.cache_data
def req():
    return {"users": ["foo", "bar"]}


if "counter" not in st.session_state:
    st.session_state["counter"] = 0


def increment_counter():
    st.session_state["counter"] += 1


def main():
    st.write("""
    # Heading 
             
    Hello world
""")
    files = st.file_uploader(
        "Upload", type=["jpeg", "jpg", "bmp"], accept_multiple_files=True
    )
    res = st.button("Label", "k")
    if res:
        st.write(files)


if __name__ == "__main__":
    main()
