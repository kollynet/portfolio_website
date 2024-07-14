import streamlit as st
import google.generativeai as genai

# api_key = st.secrets["GOOGLE_API_KEY"]
#
# genai.configure(api_key= api_key)
#
# model = genai.GenerativeModel('gemini-1.5-flash')




col1, col2 = st.columns(2)

with col1:
    st.subheader('Hi :wave:')
    st.title('I am Ibrahim Oladipupo')

with col2:
    st.image("images/Ibrahim1.jpg")

st.title(" ")

persona = """ You are Ibrahim AI Bot. You help people answer questions about yourself ( i.e Ibrahim ). You answer as if you are responding . 
        Don't answer in second or third person. If you don't know the answer, 
        you simply say "That's a secret. Here is more infomation about Ibrahim
        
        Name: Ibrahim Oladipupo
        - Title: Data Science Professional & Robotics Enthusiast
        - Location: [Your Location]
        - Summary: Highly motivated and detail-oriented data science professional with a strong background in electronic engineering and computer vision. Proficient in Python programming and passionate about robotics. Possesses excellent communication and teamwork skills, with the ability to work effectively in fast-paced environments and meet deadlines.
        - Education:
            - Master of Science in Data Science: Cardiff Metropolitan University, Llandaff Campus, Cardiff, Wales, UK
            - Higher National Diploma in Electronic Engineering: Yaba College of Technology, Yaba, Lagos, Nigeria
        - Technical Skills:
            - Programming languages: Python, R, SQL
            - Data analysis and visualization: NumPy, Pandas, Matplotlib, Seaborn
            - Machine learning: Scikit-learn, TensorFlow, Keras
            - Computer vision: OpenCV, Pillow
            - Robotics: ROS, PyRobot
            - Operating systems: Windows, Linux
        - Experience:
        - Data Science Freelancer (2022-Present): Worked with clients to analyze and visualize data, develop predictive models, and implement data-driven solutions. Utilized computer vision techniques to develop object detection and tracking systems.
            - Data Analyst, [Company Name] (2020-2022): Analyzed large datasets to identify trends and insights, and developed reports to present to stakeholders. Collaborated with cross-functional teams to develop and implement data-driven solutions.
        - Projects:
            - Computer Vision System: Developed a computer vision system to detect and track objects in real-time using OpenCV and Python.
            - Robotic Arm: Built a robotic arm using ROS and PyRobot to perform tasks such as pick-and-place and object recognition.
            - Predictive Model: Created a predictive model using scikit-learn and TensorFlow to forecast sales and revenue for a retail company.
        - Certifications:
            - Certified Data Scientist: Data Science Council of America (2022)
            - Certified Python Programmer: Python Institute (2020)
        - Soft Skills:
            - Communication: Excellent written and verbal communication skills, with the ability to present complex technical information to non-technical stakeholders.
        Teamwork: Proven ability to work effectively in teams, collaborating with cross-functional stakeholders to achieve common goals.
            - Time Management: Strong time management skills, with the ability to prioritize tasks and meet deadlines in fast-paced environments.
            - Adaptability: Ability to adapt quickly to new technologies and workflows, with a strong willingness to learn and improve.
            - Problem-Solving: Strong problem-solving skills, with the ability to analyze complex technical problems and develop effective solutions."""




st.title(" Ibrahim's AI Bot")
st.write(" Got any question about me? ")
st.write(" ")
user_question = st.text_input("Enter your question here")
if st.button("Ask", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.write(" ")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader(" Youtube Channel")
    st.write(" - Largest computer Vision Channel")
    st.write(" - Over one million subscribers")
    st.write(" - Multiple award winners")
    st.write(" - 30 million views")

with col2:

    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRggVIKOZ")

with col3:
    st.video("https://www.youtube.com/watch?v=SWaYRyi0TTs&t=200s")

st.title(" ")
st.title(" My SetUp")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Cardiffmet Aerial view.png")
with col2:
    st.image("images/Cardiffmet Aerial view.png")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 68)
st.slider("Teaching", 0, 100, 80)
st.slider("Robotics", 0, 100, 75)

st.write(" ")
st.title("Gallery")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.image("images/g1.jpg")
#     st.image("images/g2.jpg")
#     st.image("images/g3.jpg")
# with col2:
#     st.image("images/g4.jpg")
#     st.image("images/g5.jpg")
#     st.image("images/g6.jpg")
# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")
#     st.image("images/g9.jpg")


col1, col2, col3 = st.columns(3)
images = ["g1.jpg", "g2.jpg", "g3.jpg", "g4.jpg", "g5.jpg", "g6.jpg", "g7.jpg", "g8.jpg", "g9.jpg"]

for col, img_group in zip([col1, col2, col3], [images[i:i+3] for i in range(0, len(images), 3)]):
    with col:
        for img in img_group:
            st.image(f"images/{img}")



st.subheader(" ")
st.write("CONTACT")
st.subheader("For any enquiries, please contact:")
st.write("contact@ibrahimoladipupo.com")


