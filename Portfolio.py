import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

# Sidebar
st.sidebar.title("Noâm Detournay")
st.sidebar.text(
    "Data Scientist | ML Engineer"
)

st.sidebar.markdown("[GitHub](https://github.com/NoamDetournay)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/noam-detournay)")

# Main Title
st.title("My Portfolio")

# Studies Section
st.header("My Studies")
st.write("""
- **Master 1 in Data Science** - *Efrei Paris* (Expected 2026)
  - Key courses: Machine Learning, Data Analysis, Big Data, Python Programming, Statistics
""")

# Projects Section
st.header("My Projects")
st.write("""
### 1. Predictive France Housing Price 
- Built a predictive model for housing prices using the land value dataset from France.
- Applied data preprocessing, feature engineering, and linear regression to predict housing prices.
- Tools used: Python, Scikit-learn, Pandas, Matplotlib.

### 2. NLP - Patent classification explained
- Developed a patent classification model using Natural Language Processing (NLP) techniques.
- Tools used: PyTorch, TensorFlow, Python, Streamlit.

""")

# Professional Experiences Section
st.header("My Professional Experiences")


# Footer
st.write("""
*This portfolio was built using [Streamlit](https://streamlit.io/), a Python library for building interactive web applications.*
""")
