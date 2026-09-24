import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

# Page Config
st.set_page_config(page_title="ComicCraft - AI Comic Creator", layout="wide")
st.title("🎨 ComicCraft: AI Comic Story & Scene Generator")

# Sidebar for API Key
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if not api_key:
    st.info("👈 Please enter your Gemini API Key in the sidebar to start.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# App UI
st.subheader("1. Enter Your Comic Concept")
topic = st.text_input("Story Idea / Theme", placeholder="A superhero cat saving the city from a giant robot")

col1, col2 = st.columns(2)
with col1:
    num_panels = st.slider("Number of Panels", min_value=2, max_value=6, value=4)
with col2:
    art_style = st.selectbox("Art Style", ["Manga", "Marvel Comic Style", "Cartoon", "Pixel Art", "Watercolor"])

if st.button("Generate Comic Script & Prompts"):
    if not topic:
        st.warning("Please enter a story idea!")
    else:
        with st.spinner("Writing your comic script..."):
            prompt = f"""
            Create a {num_panels}-panel comic story script based on the theme: '{topic}'.
            For each panel, provide:
            1. Panel Title
            2. Scene Description
            3. Character Dialogue / Caption
            4. Image Generation Prompt (style: {art_style})
            """
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            st.success("Comic Script Generated!")
            st.markdown(response.text)
