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
    .name {
        color: #ff9900; /* Change name color to orange */
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

# Header Section with a brief introduction
st.markdown('<div class="header"><h1 class="name">Swara Kamalkumar Joshi</h1><p>Master of Science in Information Systems at Northeastern University | Research Enthusiast | Bachelor of Technology in Information and Communication Technology at PDEU | Passionate about Innovation and Technology</p></div>', unsafe_allow_html=True)

# Navigation Buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Home"):
        st.session_state.page = "home"
with col2:
    if st.button("Education"):
        st.session_state.page = "education"
with col3:
    if st.button("Experience"):
        st.session_state.page = "experience"
with col4:
    if st.button("Projects & Research"):
        st.session_state.page = "projects"

# Initialize session state if not set
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Display content based on button click
if st.session_state.page == "home":
    st.subheader("👋 About Me")
    st.write("""
    I am a passionate Information Systems professional currently pursuing my Master's at Northeastern University, with a strong focus on emerging technologies and data-driven innovations. My goal is to leverage my academic experience and hands-on projects to contribute to advancements in the IT industry.

    Beyond academics, I have been actively involved in personal growth and leadership roles. I served as the President of Camaraderie (Dance Crew) at PDEU and the Marketing Head of the GeeksforGeeks Student Chapter, enhancing my communication, project management, and leadership skills. I am also passionate about sports and fitness, actively participating in volleyball and staying engaged in fitness activities.

    Since moving to the USA, I have been fully immersing myself in the culture, expanding my network, and exploring the tech ecosystem. My role as an ITS Customer Experience Technician at Northeastern University has allowed me to blend my technical background with customer-facing responsibilities, improving the user experience while staying up-to-date with the latest tech trends.

    Outside of academics and work, I enjoy traveling, exploring new places, and trying out diverse cuisines. I also participate in recreational activities like hiking and attend tech meetups to stay connected with the local tech community.
    """)
elif st.session_state.page == "education":
    st.subheader("🎓 Education")
    st.write("""
    - **Master of Science in Information Systems** – Northeastern University, Boston, MA  
      Coursework: Application Engineering and Development, Data Science Engineering Methods and Tools, Program Structures and Algorithms, Advances in Data Science/Architecture

    - **Bachelor of Technology in Information and Communication Technology** – Pandit Deendayal Energy University, Gujarat, India  
      CPI: 3.41/4.0  
      Aug 2020 - May 2024  
      Coursework: Computer Programming with C, Fundamentals of Python Programming, Data Structures and Algorithm, Object Oriented Concepts and Programming, SQL for Beginners, Database Management System, Computer Organization and Design, Introduction to Data Mining, Information Security, Theory of Automata and Computation, AI Systems, Machine Learning, Cloud Architecture and Services, Internet of Things, Big Data Analytics and Computing, Deep Reinforcement Learning, Software Engineering and Project Management
    """)
    st.subheader("💻 Skills")
    st.write("""
    #### Technical Skills
    | Category | Skills |
    |----------|--------|
    | **Languages** | Python, C++, Java, Solidity, C, Kotlin, SQL, JavaScript, HTML, CSS, R, MATLAB, C# |
    | **AI & ML** | Deep Learning, LLMs, OpenAI, Groq, LangChain, RAG, NLP, Computer Vision, A/B Testing, Rasa, Llama, Tavily, Web Scraping, Hugging Face |
    | **Data Science & Analytics** | Data Visualization, Data Modeling, Quantitative & Predictive Analytics, Statistical Modeling, Power BI, Tableau, Data Wrangling, Big Data, Data Pipelines & ETL, Time Series Analysis, Tensorflow, Pytorch, Mathematics |
    | **Cloud & DevOps** | AWS, Azure, GCP, Docker, Kubernetes, Hadoop, Spark, MLOps, SAS, Big Data, Git, Lightning |
    | **Software Development** |  Flask, Streamlit, React, Node.js, Next.js, Angular, MongoDB, PostgreSQL, MySQL, RESTful APIs, CI/CD |
    | **Soft Skills** | Problem-Solving, Time Management, Critical Thinking, Attention to Detail, Communication, Adaptability, Teamwork |
    """)
    st.subheader("🏅 Certifications")
    st.write("""
    - IIT Kharagpur certified python course  
    - PH526x: Using Python for Research - HarvardX  
    - 30 Days of Google Cloud - Create and Manage Cloud Resources; Google Cloud Essentials; Google Cloud Fundamentals; Core Infrastructure; Perform Foundational Infrastructure Tasks; Google Cloud Big Data and Machine Learning Fundamentals  
    - Programming with SQL - Oracle
    """)
elif st.session_state.page == "experience":
    st.subheader("🧠 Experience")
    st.write("""
    - **ITS Customer Experience Technician** – Northeastern University, Boston, MA  
      Dec 2024 - Present  
      - Assisted library patrons by resolving IT service queries, ensuring seamless access to technology resources and support while addressing customer needs and enhancing customer relationship management

    - **Research Intern** – Gujarat Council of Science and Technology, India  
      Jun 2023 - Aug 2023  
      - Researched and analyzed authentication protocols, identifying areas for improvement and proposing new techniques such as keystroke analysis and secure one-way method which led to increased security and reduction in time and space complexity  
      - Developed a structural framework integrating blockchain technology into Kerberos systems, resulting in a \(40 \%\) increase in efficiency. Created smart contracts on Ethereum Remix IDE using Solidity and Web3.js to streamline operations

    - **Data Science Intern** – The Sparks Foundation, Remote, India  
      Sept 2022 - Oct 2022  
      - Performed data cleaning and preprocessing on large datasets, training machine learning models for currency exchange rate prediction, achieving a \(15 \%\) improvement in forecasting accuracy by optimizing feature selection and model performance.
    """)
elif st.session_state.page == "projects":
    st.subheader("🚀 Projects and Publications")
    st.write("""
    - **AI Agent Chatbot**  
      - Built an end-to-end AI app integrating Groq and Tavily with Llama models, optimizing response accuracy and automation.
      - Developed an agentic AI chatbot that personalizes AI models (e.g., Llama, GPT-4) for specific tasks (e.g., health bot, email generator), integrating Groq, Tavily, and Llama models to enhance response accuracy and automation.Built a full-stack, end-to-end web application, reducing processing latency by 50% and improving user engagement with customizable features, including web search enablement.
      [GitHub](https://github.com/Swara-Joshi/Agentic-Chatbot)

    - **AI-Powered Newsletter Subscription System**  
      - Developed a full-stack web application leveraging web scraping with Selenium and Beautiful Soup to scrape finance and tech news. 
      - Incorporated OpenAI model for advanced content summarization and sentiment analysis, automating personalized email delivery to over 1000 subscribers, increasing engagement by 30%.
      [GitHub](https://github.com/Swara-Joshi/AI-Powered-Newsletter)
             
    - **Segmentation of Palmprint Region From Diversified Hand Videos** 
      – IEEE CONECCT 2024  
      -Implemented a novel algorithm utilizing the Segment Anything Model using deep learning framework to accurately segment palmprint regions from diverse hand video datasets with annotations from a proprietary hand video dataset, containing videos of 30 individuals  
      - Applied advanced image processing techniques including thresholding, contour detection, and ROI extraction to enhance palmprint recognition efficiency by \(35 \%\), contributing to the development of robust biometric authentication systems  
      [Citation](https://ieeexplore.ieee.org/document/10677138)

    - **Cancer Detection with machine learning approach** 
      – Presented at the 2nd International Conference on Advancements in Smart Computing and Information Security: Reviewed 50+ research studies on ML techniques for detecting breast, lung, skin, and prostate cancers, with model accuracies ranging from \(82 \%\) to \(97 \%\).
      - Highlighted research gaps and societal impact, showing a potential \(25 \%\) reduction in diagnostic errors through ML models, while analyzing algorithm complexities like CNN \(\left(O\left(n^{2}\right)\right)\) and random forests \((O(n \log n)\) )  
      [Citation](https://ieeexplore.ieee.org/abstract/document/10461904)

    - **A consolidated study of traditional data to Big Data**
      – Accepted in 3rd Asian Conference on Innovation in Technology (IJANA)
      - Highlighted the transition from RDBMS to NoSQL databases, focusing on MongoDB's efficiency in handling large-scale data, with observed improvements in query performance by up to \(40 \%\) due to its schema-less architecture  
      [Citation](https://www.researchgate.net/publication/378198693_A_consolidated_study_on_transformation_of_Traditional_Data_to_Big_Data)

    - **Energy theft detection in smart grid using deep learning algorithm**
       - Developed a precise deep learning model capable of accurately distinguishing between normal energy consumption and potential theft, leading to the implementation of an alert system for immediate action upon detection. Built a hardware setup showcasing the functionality of the deep learning model for energy theft detection, providing a tangible demonstration of its effectiveness to stakeholders
    """)
    st.subheader("📜 Patents")
    st.write("""
    - **Contact-less Authentication with Blockchain Integration**  
      Developed an end-to-end system combining face detection, QR code scanner & blockchain, achieving a \(40 \%\) reduction in authentication time and a \(30 \%\) increase in security through dynamic access control and immutable log maintenance.  
      **Patent Number:** 202321075151
    """)

# Contact Section with Links
st.subheader("📞 Contact Me")
st.write("""
Feel free to reach out via email at [joshi.swar@northeastern.edu](mailto:joshi.swar@northeastern.edu).  
Connect with me on [LinkedIn](https://www.linkedin.com/in/swara-joshi) or [ResearchGate](https://www.researchgate.net/profile/Swara-Joshi-3?ev=hdr_xprf).  
Check out my projects on [GitHub](https://github.com/Swara-Joshi).
""")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Made with 💻 by Swara Joshi | Powered by Streamlit")

# Optional: Add background image
background_image_url = "https://path_to_your_image.jpg"  # Replace with your image URL or path
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: cover;
    }}
    </style>
""", unsafe_allow_html=True)
