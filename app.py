import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="AI Video & Voice Generator", page_icon="🎬", layout="centered")

st.title("AI Video & Voice Generator (Sinhala)")
st.write("මෙතැනින් ඔබට අවශ්‍ය පින්තූර, සිංහල හඬ සහ වීඩියෝ සාදාගත හැක.")

# 1. Sinhala Text to Speech
st.header("1. Sinhala Text to Speech")
sinhala_text = st.text_area("සිංහලෙන් යමක් ලියන්න:", "සැමෝටම ආයුබෝවන්! මම AI ඇප් එකක්.")

if st.button("Voice එක සකසන්න"):
    if sinhala_text.strip() != "":
        tts = gTTS(text=sinhala_text, lang='si')
        audio_file = "output.mp3"
        tts.save(audio_file)
        st.audio(audio_file, format="audio/mp3")
        st.success("හඬ සාර්ථකව සකස් කරන ලදී!")
    else:
        st.warning("দয়া කරලා යමක් ලියන්න!")

# 2. Text to Image (Placeholder)
st.header("2. Text to Image")
prompt = st.text_input("පින්තූරයක් සඳහා විස්තරයක් ලියන්න (English වලින්):")
if st.button("පින්තූරය සාදන්න"):
    st.info("පින්තූර උත්පාදන පහසුකම ඉක්මනින් එකතු කරනු ලැබේ!")
  
