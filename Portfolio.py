import streamlit as st
from PIL import Image

# Page Configurations
st.set_page_config(
    page_title="Noâm Detournay Portfolio",
    page_icon="👋",
    layout="wide",
)

# Sidebar
st.sidebar.title("Noâm Detournay")
st.sidebar.image("profile_picture.jpg", use_column_width=True)  
st.sidebar.markdown("""
**Data Scientist | ML Engineer**  
I'm passionate about harnessing the power of data and AI to solve real-world problems.
""")
st.sidebar.markdown("[GitHub](https://github.com/NoamDetournay)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/noam-detournay)")
st.sidebar.markdown("[Contact Me](mailto:noam.detournay@orange.fr)")

# Main Title
st.title("Welcome to My Portfolio 👋")
st.subheader("Hi, I'm Noâm Detournay, a Data Scientist with a passion for AI and Machine Learning.")
st.write("Feel free to explore my projects and experiences below.")

st.markdown("---")

# Studies Section
st.header("📚 My Studies")
st.write("""
- **Master 1 in Data Science** - *Efrei Paris* (Expected 2026)
  - Key courses: Machine Learning, Data Analysis, Big Data, Python Programming, Statistics
- **Semester Abroad in California** (29/08/2023 – 09/12/2023) - *University of California, Irvine (UCI)*
  - Immersed in American culture and education system. Courses taken: Java, Web Development, Networks, UML, Operating Systems, and Computer Architecture (all taught in English).
""")
st.markdown("---")
st.header("💼 My Professional Experience")
st.write("""
- **Customer Service and Sales - Darty** (CDD, 2 Months: 05/06/2023 - 25/08/2023)
  - Assisted customers and managed sales tasks at the Villabé 91 location.
- **Commercial Internship - Darty** (Internship, 1 Month: 02/01/2023 - 28/01/2023)
  - Handled customer service and sales as part of a commercial internship at Villabé 91.
- **Packaging Line Worker - COOPER** (Internship, 1 Month: 04/07/2022 - 29/07/2022)
  - Worked as a packaging line agent at Coopération Pharmaceutique Française in Melun 77.
""")

st.markdown("---")
st.header("🛠️ Skills")
st.write("""
- **Programming**: Python, R, SQL
- **Libraries**: TensorFlow, PyTorch, Scikit-learn, Pandas, Numpy
- **Tools**: Git, Docker, Streamlit
""")

st.markdown("---")
# Add a call-to-action for more projects

st.header("💻 My Projects")
st.markdown("[See projects on my GitHub](https://github.com/NoamDetournay)")


col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Predictive France Housing Price")
    st.write("""
    - Built a predictive model for housing prices using the land value dataset from France.
    - Applied data preprocessing, feature engineering, and linear regression to predict housing prices.
    - **Tools**: Python, Scikit-learn, Pandas, Matplotlib.
    """)

with col2:
    st.subheader("2. NLP - Patent Classification")
    st.write("""
    - Developed a patent classification model using Natural Language Processing (NLP) techniques.
    - **Tools**: PyTorch, TensorFlow, Python, Streamlit.
    """)
