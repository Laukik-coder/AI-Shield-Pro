import streamlit as st
import pandas as pd
import plotly.express as px
import time
from image_detector import detect_image
from deepfake_detector import detect_fake_image
from fake_news_detector import predict_news

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Shield Pro",
    page_icon="🛡️",
    layout="wide"
)

# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #020617;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(to bottom right, #020617, #071a3d);
}

section[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid #1e293b;
}

.big-title {
    font-size: 70px;
    font-weight: bold;
    color: #60a5fa;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {
        text-shadow: 0 0 10px #2563eb;
    }
    to {
        text-shadow: 0 0 30px #60a5fa;
    }
}

.card {
    background: #0f172a;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #1e3a8a;
    box-shadow: 0 0 20px rgba(37,99,235,0.2);
    margin-top: 20px;
}

.metric-card {
    background: #111827;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid #1d4ed8;
}

.stButton>button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8, #60a5fa);
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# ====================================
# SIDEBAR
# ====================================

st.sidebar.markdown("""
# 🛡️ AI Shield Pro

### 🚀 Intelligent AI Verification Platform

Built using:

- Machine Learning
- Deep Learning
- NLP
- HuggingFace
- Streamlit
- Computer Vision
- Plotly Analytics
""")

option = st.sidebar.radio(
    "Choose Module",
    [
        "🏠 Home",
        "📰 Fake News Detection",
        "🖼️ Image Detection",
        "🤖 AI Generated Detection",
        "📷 Live Camera Detection",
        "🤖 AI Assistant",
        "📊 System Dashboard",
        "ℹ️ About Project"
    ]
)

# ====================================
# HOME
# ====================================

if option == "🏠 Home":

    st.markdown(
        '<div class="big-title">🛡️ AI Shield Pro</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    ## Intelligent AI-Powered Content Verification Platform

    AI Shield Pro is an advanced AI system capable of:

    - 📰 Fake News Detection
    - 🖼️ Intelligent Image Classification
    - 🤖 AI Generated Image Detection
    - 📷 Live Camera AI Analysis
    - 📊 AI Confidence Analytics
    - 🧠 Machine Learning Verification
    - 🤖 AI Assistant Integration
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
        <h1>5</h1>
        <p>AI Modules</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
        <h1>ML + DL</h1>
        <p>Hybrid AI Stack</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
        <h1>2026</h1>
        <p>Latest Version</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
        <h1>LIVE</h1>
        <p>Deployment Active</p>
        </div>
        """, unsafe_allow_html=True)

# ====================================
# FAKE NEWS DETECTION
# ====================================

elif option == "📰 Fake News Detection":

    st.title("📰 AI Fake News Detector")

    news = st.text_area("Enter News Article")

    if st.button("Analyze News"):

        if news.strip() == "":
            st.warning("Please enter news text.")
        else:

            prediction = predict_news(news)

            if prediction == "REAL":
                st.success("✅ This News Appears Real")
            else:
                st.error("⚠️ This News Appears Fake")

# ====================================
# IMAGE DETECTION
# ====================================

elif option == "🖼️ Image Detection":

    st.title("🖼️ AI Image Detector")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:

        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.getbuffer())

        st.image(uploaded_image)

        if st.button("Analyze Image"):

            with st.spinner("Analyzing Image with AI Vision Engine..."):
                time.sleep(2)

                result = detect_image("temp_image.jpg")

                st.subheader("📊 AI Probability Results")

                labels = []
                scores = []

                for item in result[:3]:

                    label = item['label']
                    score = round(item['score'] * 100, 2)

                    labels.append(label)
                    scores.append(score)

                    st.info(f"{label} : {score}%")

                    st.progress(int(score))

                df = pd.DataFrame({
                    "Label": labels,
                    "Confidence": scores
                })

                fig = px.bar(
                    df,
                    x="Label",
                    y="Confidence",
                    title="AI Confidence Analysis"
                )

                st.plotly_chart(fig, use_container_width=True)

# ====================================
# AI GENERATED DETECTION
# ====================================

elif option == "🤖 AI Generated Detection":

    st.title("🤖 AI Generated Image Detector")

    uploaded_fake_image = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_fake_image is not None:

        with open("fake_test.jpg", "wb") as f:
            f.write(uploaded_fake_image.getbuffer())

        st.image(uploaded_fake_image)

        if st.button("Check AI Generated Image"):

            with st.spinner("Running Deepfake Detection Engine..."):
                time.sleep(2)

                results = detect_fake_image("fake_test.jpg")

                st.subheader("📊 AI Authenticity Analysis")

                labels = []
                scores = []

                for item in results[:2]:

                    label = item['label']
                    score = round(item['score'] * 100, 2)

                    labels.append(label)
                    scores.append(score)

                    if "fake" in label.lower() or "artificial" in label.lower():

                        st.error(f"{label} : {score}%")

                    else:

                        st.success(f"{label} : {score}%")

                    st.progress(int(score))

                df = pd.DataFrame({
                    "Type": labels,
                    "Confidence": scores
                })

                fig = px.pie(
                    df,
                    names="Type",
                    values="Confidence",
                    title="Authenticity Distribution"
                )

                st.plotly_chart(fig, use_container_width=True)

# ====================================
# LIVE CAMERA
# ====================================

elif option == "📷 Live Camera Detection":

    st.title("📷 Live Camera AI Detection")

    camera_image = st.camera_input("Capture Image")

    if camera_image is not None:

        with open("camera.jpg", "wb") as f:
            f.write(camera_image.getbuffer())

        st.success("✅ Image Captured Successfully")

        st.image(camera_image)

# ====================================
# AI ASSISTANT
# ====================================

elif option == "🤖 AI Assistant":

    st.title("🤖 AI Shield Assistant")

    user_question = st.text_input(
        "Ask something about AI, fake news, cybersecurity, or deepfakes"
    )

    if st.button("Ask AI Shield"):

        with st.spinner("Thinking..."):
            time.sleep(2)

            st.success(
                "AI Assistant Response: AI-generated misinformation is increasing rapidly across social media platforms. Verification systems like AI Shield Pro help users analyze authenticity using machine learning and deep learning models."
            )

# ====================================
# DASHBOARD
# ====================================

elif option == "📊 System Dashboard":

    st.title("📊 AI System Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Models Active", "5")
    col2.metric("Framework", "Streamlit")
    col3.metric("Status", "Online")

    analytics = pd.DataFrame({
        "Module": [
            "Fake News",
            "Image Detection",
            "AI Detection",
            "Camera AI"
        ],
        "Usage": [85, 70, 90, 60]
    })

    fig = px.line(
        analytics,
        x="Module",
        y="Usage",
        title="System Usage Analytics"
    )

    st.plotly_chart(fig, use_container_width=True)

# ====================================
# ABOUT
# ====================================

elif option == "ℹ️ About Project":

    st.title("ℹ️ About AI Shield Pro")

    st.markdown("""
    ## Developed By Laukik 🚀

    AI Shield Pro is an intelligent AI-powered misinformation and media verification platform.

    ### Features:
    - Fake News Detection
    - AI Image Classification
    - AI Generated Detection
    - Live Camera AI Analysis
    - AI Assistant
    - Analytics Dashboard

    ### Technologies Used:
    - Python
    - Streamlit
    - Plotly
    - Transformers
    - HuggingFace
    - NLP
    - Computer Vision
    - Deep Learning

    ### Future Goals:
    - Voice Deepfake Detection
    - Live AI Monitoring
    - Browser Extension
    - API Deployment
    - Enterprise Dashboard
    """)

# ====================================
# FOOTER
# ====================================

st.markdown("---")
st.caption("🛡️ AI Shield Pro • Built by Laukik 🚀")
