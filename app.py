import streamlit as st
from PIL import Image

# Set the title of the app
st.title("Sushil Kokare's Portfolio")

# Add a header
st.header("Welcome to my Portfolio!")

# Add a subheader
st.subheader("About Me")

# Add some text about yourself
st.write("""
Hello! My name is **Sushil Kokare**. I am passionate about Data Science and related fields. 
I enjoy working on data-driven projects and am constantly looking to improve my skills and learn new techniques.
""")

# Add an image
image = Image.open("photo.png")  # Replace with your image path
st.image(image, caption='Sushil Kokare', use_column_width=False,width=500)

# Add a section for skills
st.header("Skills")
st.write("""
- Programming Languages: Python, R
- Data Analysis: Pandas, NumPy, Scikit-Learn
- Data Visualization: Matplotlib, Seaborn, Plotly
- Machine Learning: Scikit-Learn, TensorFlow, Keras
- Others: SQL, Excel
""")

# Add a section for projects
st.header("Projects")
st.write("""
### Project 1: Data Analysis on Sales Data
- Description: Performed exploratory data analysis on sales data to identify trends and patterns.
- Technologies: Python, Pandas, Matplotlib

### Project 2: Machine Learning Model for Predicting House Prices
- Description: Built and trained a machine learning model to predict house prices based on various features.
- Technologies: Python, Scikit-Learn, Pandas

### Project 3: Interactive Dashboard for Visualizing Company Performance
- Description: Created an interactive dashboard using Streamlit to visualize the performance of different departments within a company.
- Technologies: Python, Streamlit, Plotly
""")

# Add a section for contact information
st.header("Contact Me")
st.write("""
- Email: sushil.kokare@example.com
- LinkedIn: [Sushil Kokare](https://www.linkedin.com/in/sushil-kokare/)
- GitHub: [SushilKokare](https://github.com/SushilKokare)
""")

# Add an expander for more detailed information
with st.expander("More about me"):
    st.write("""
    I have a strong foundation in mathematics and statistics, which has helped me excel in data science. 
    I am also a quick learner and thrive in collaborative environments. 
    When I am not working, I enjoy reading books, hiking, and exploring new technologies.
    """)

# Add a sidebar with additional information
st.sidebar.title("About Me")
st.sidebar.info("""
    I am a data enthusiast who loves working with data and uncovering insights from it.
    In my free time, I contribute to open-source projects and write blogs about data science.
""")

