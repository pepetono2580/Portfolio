import streamlit as st

st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/jrasg.jpeg", width=300)

with col2:
    st.title("José A. Rasgado")
    content = """
    Hello! I'm José and I am a Python developer, I graduated in 2021 as a Software Engineer from Anáhuac Mayab University.
    Since then, I've worked in multiple companies using different tools, such as No-Code technologies for building dynamic 
    websites and web-apps with Bubble, and RPA platforms such as Automation Anywhere, which led me to learn Python and 
    create the projects presented in this portfolio.
    """
    st.info(content)

content2 = """Below you can find me some of the apps I have built in Python. Feel free to contact me"""
st.write(content2)