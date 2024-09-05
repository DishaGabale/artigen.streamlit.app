import streamlit as st
welcome = "## ✨Welcome!✨"
summary = "## Read the summary of our model!!"
preinfo = """
Unique, fast, detailed article generator which helps you to write wonderful articles.
"""


contactInfo = """
## For any Queries:-
### You could connect with me on [LinkedIn](https://www.linkedin.com/in/disha-gabale-9682ba238/) or could mail me [here](mailto:gabaledisha@gmail.com)
"""



def sidebar_conf():
    sidebar = st.sidebar
    sidebar.title("ArtiGen - A article generator")
    sidebar.divider()
    sidebar.markdown(welcome)
    sidebar.markdown(summary)
    sidebar.caption(preinfo)
    sidebar.markdown("* To simply generate a article")
    sidebar.markdown("* To generate articles about certain latest government policy updates ")
    sidebar.divider()
    sidebar.markdown(contactInfo)
    sidebar.markdown("# Made with ❤️ by Disha")

if __name__ == "__main__":
    sidebar_conf()
