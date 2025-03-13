import streamlit as st
from streamlit.components.v1 import html

# Set the page config for a clean header and title
st.set_page_config(page_title="Swara Joshi's Portfolio", page_icon=":wave:", layout="wide")

# Custom CSS to make the layout look cleaner
st.markdown("""
    <style>
    .main {
        background-color: #f1f5f8;
        color: #333;
    }
    .header {
        background-color: #1f2a44;
        color: white;
        padding: 20px;
    }
    .section-title {
        color: #1f2a44;
        font-weight: bold;
    }
    .subsection {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .icon {
        font-size: 30px;
        color: #1f2a44;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section with a profile picture and a brief introduction
st.markdown('<div class="header"><h1>Swara Joshi</h1><p>Graduate Student | Data Scientist | Research Enthusiast</p></div>', unsafe_allow_html=True)
# st.image("your_photo.jpg", use_column_width=True)  # Replace with your image path

# About Me Section with Icons
st.subheader("👋 About Me")
st.write("""
I am a passionate graduate student at Northeastern University, Boston, with a keen interest in Data Science and Research. 
I have experience in software development, machine learning, blockchain, and cloud technologies. 
My ultimate goal is to contribute to innovative projects that push the boundaries of technology.
""")

# Education Section with Icons
st.subheader("🎓 Education")
st.write("""
- **Master of Science in Information Systems** – Northeastern University, Boston  
- **Bachelor of Technology in Information and Communication Technology** – Pandit Deendayal Energy University, India (2020 - 2024)
""")

st.subheader("🏅 Certifications")
st.write("""
- IIT Kharagpur certified Python course
- PH526x: Using Python for Research – HarvardX
- Google Cloud Essentials, Google Cloud Big Data and ML Fundamentals
- Programming with SQL – Oracle
""")

# Skills Section with Icons and Visual Display
st.subheader("💻 Skills")
skills = [
    'Python', 'Java', 'SQL', 'Machine Learning', 'Blockchain', 'Deep Learning', 
    'Google Cloud', 'Git', 'C++', 'Solidity', 'C', 'Kotlin', 'JavaScript', 
    'HTML', 'CSS', 'R', 'MATLAB', 'C#', 'Data Visualization', 'Data Modeling', 
    'Quantitative & Predictive Analytics', 'Statistical Modeling', 'Power BI', 
    'Tableau', 'Data Wrangling', 'Big Data', 'Data Pipelines & ETL', 'Time Series Analysis', 
    'Tensorflow', 'Pytorch', 'AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes', 
    'Hadoop', 'Spark', 'MLOps', 'SAS', 'Git', 'Lightning'
]
st.write("I am proficient in the following skills:")
for skill in skills:
    st.markdown(f"- {skill}")

# Research Projects Section with Collapsible Elements
st.subheader("🧠 Research & Experience")
with st.expander("Research Projects"):
    st.write("""
    - **Segmentation of Palmprint Region From Diversified Hand Videos** – IEEE CONECCT 2024  
      Implemented a novel algorithm for palmprint recognition, improving authentication efficiency by 35%.

    - **Cancer Detection with Machine Learning** – International Conference on Smart Computing and Information Security  
      Studied machine learning techniques for early cancer detection and analyzed their societal impact.

    - **A Consolidated Study of Traditional Data to Big Data** – Asian Conference on Innovation in Technology  
      Highlighted the transition from RDBMS to NoSQL databases, focusing on MongoDB's efficiency.
    """)

with st.expander("Work Experience"):
    st.write("""
    - **ITS Customer Experience Technician** – Northeastern University  
      Assisted library patrons by resolving IT service queries and enhancing customer relationship management.

    - **Research Intern** – Gujarat Council of Science and Technology  
      Researched authentication protocols, proposed new techniques, and developed a blockchain-based Kerberos system.
    """)

# Projects Section with Collapsible Elements
st.subheader("🚀 Projects")
with st.expander("Blockchain-based Authentication System"):
    st.write("""
    Integrated Kerberos with blockchain to create a contactless authentication system with dynamic policies.
    """)

with st.expander("AI Agent Chatbot"):
    st.write("""
    Built an end-to-end AI app integrating Groq and Tavily with Llama models, optimizing response accuracy and automation.
    """)

with st.expander("Contact-less Authentication with Blockchain Integration"):
    st.write("""
    Developed an end-to-end system combining face detection, QR code scanner & blockchain, achieving a 40% reduction in authentication time and a 30% increase in security.
    """)

# Contact Section with Links
st.subheader("📞 Contact Me")
st.write("""
Feel free to reach out via email at [joshi.swar@northeastern.edu](mailto:joshi.swar@northeastern.edu).  
Connect with me on [LinkedIn](https://www.linkedin.com/in/swara-joshi).
""")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Made with 💻 by Swara Joshi | Powered by Streamlit")

# Optional: Add background image
background_image_url = "C:/Users/Swara/Desktop/profile.jpg"  # Replace with your image URL or path
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: cover;
    }}
    </style>
""", unsafe_allow_html=True)
