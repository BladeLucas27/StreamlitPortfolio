import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def css():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        [data-testid="stHeader"] {visibility: hidden;}

        .stApp {
            background-color: #4e312f;
            background-size: cover;
        }

        h1, h2, h3, p, .stMarkdown {
            color: #ffddab !important;
        }

        </style>
    """, unsafe_allow_html=True)
#css()

col1, col2 = st.columns([1, 2], gap="large")

project_data = {
    "Project Name": [
        ":material/image: Basic Image Processor",
        ":material/calculate: C# Basic Calculator",
        ":material/self_improvement: CalmCode - Meditation App",
        ":material/quiz: Multiple Choice Quiz Database Creator"
    ],
    "Short Description": [
        "Takes images and applies basic image processing techniques such as grayscale conversion, reverse, and greenscreen subtraction.",
        "Basic operations calculator application built using C# and Windows Forms.",
        "Start of a meditation application that helps users relax and focus through chosen musical genres and related articles.",
        "Stores lists of multiple choice questions, teachers, and students in a database and allows teachers to create quizzes, and students to answer them."
    ],
    "Links": [
        "(https://github.com/BladeLucas27/ImageProcessingAct.git)",
        "(https://github.com/BladeLucas27/CalculatorTutorial-C-Sharp.git)",
        "(https://github.com/BladeLucas27/CalmCode.git)",
        "(https://github.com/BladeLucas27/LA7-GUI-JDBC.git)"
    ]
}

with col1:
    st.markdown('<div class="profile-img">', unsafe_allow_html=True)
    st.image("pfp.png", width=300)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("""
    - Name: Raymond Gerard Tio
    - Age: 21
    - Location: Cebu, Philippines
    - Course: Bachelor of Science in Computer Science
    - Hobbies: Playing Video Games, Discovering Cafés, Watching Anime, and Collecting Amigurumi
    """)

with col2:
    st.title("Hello! This is a brief portfolio all about me!")
    st.markdown("---")

    st.subheader("About Me")
    st.write("""
    Hi! I'm currently a third-year Computer Science student studying at Cebu Institute of Technology - University. 
    As someone who loves problem-solving, I have always been drawn to the world of programming and game development.      
               
    I still think I have a long way to go in terms of learning and improving my skills, but I'm excited about the journey ahead.
    Someday I hope to fulfill my dream of becoming a game developer and creating games that people will love to play, and hopefully enjoy them as much as I did playing games when I was a kid.
    """)

    st.subheader("Sample Projects")
    st.table(project_data, border="horizontal")

    st.subheader("Contact Me")
    st.write("""
    - :material/code_blocks: **GitHub:** [BladeLucas27](https://github.com/BladeLucas27)  
    - :material/mail: **Gmail:** [raymondgtio@gmail.com](mailto:raymondgtio@gmail.com)  
    - :material/chat: **Facebook:** [Raymond Gerard Tio](https://www.facebook.com/raymondgerard.tio)
    """)
st.markdown("---")