import streamlit as st
from writer import write_article
from sidebar import sidebar_conf

# basic configuration
st.set_page_config(
    page_title="ArtiGen",
    page_icon="./assests/favicon.png",
    layout="centered",
    initial_sidebar_state="expanded",
)

# sidebar configuration
sidebar_conf()
st.image("./assests/logoX.png")

# take input from user
topic = st.text_input("Write the topic of the Article", max_chars=60)
generate_article = st.button("Generate Article")

# check if topic is given and button is pressed
if topic and generate_article:
    # extract fields from topic
    extract_topic = topic.split("--")
    if len(extract_topic) == 3:
        inputs = {
            "topic": extract_topic[0],
            "user": extract_topic[1],
            "words": extract_topic[2],
        }
    elif len(extract_topic) == 2:
        inputs = {
            "topic": extract_topic[0],
            "user": extract_topic[1],
            "words": 500,
        }
    elif len(extract_topic) == 1:
        inputs = {
            "topic": extract_topic[0],
            "user": "general public",
            "words": 500,
        }
    
    # Display loading GIF while generating the article
    loading_placeholder = st.empty()
    loading_url = "https://i.imgur.com/Sna5jn6.gif"
    loading_html = f'<div style="display: flex; justify-content: center; align-items: center;"><img src="{loading_url}" alt="Loading" width="300px" height="300px"></div>'
    loading_placeholder.markdown(loading_html, unsafe_allow_html=True)

    # Write article
    article = write_article(inputs, st.secrets["email"], st.secrets["password"])

    if article:
        loading_placeholder.empty()
        st.markdown("# ----------- Generated Article -----------")
        st.markdown(article, unsafe_allow_html=True)
    else:
        loading_placeholder.empty()
        st.error("Failed to generate the article.")
