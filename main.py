import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.image("images/jrasg.jpeg", width=300)

with col2:
    st.title("José A. Rasgado")
    content = """
    Hello! I'm José and I am a Python developer, I graduated in 2021 as a Software Engineer from Anáhuac Mayab University.
    Since then, I've worked in multiple companies using different tools, such as No-Code technologies like Bubble and RPA
    platforms such as Automation Anywhere, which led me to learn Python and create the projects presented in this portfolio.
    """
    st.info(content)