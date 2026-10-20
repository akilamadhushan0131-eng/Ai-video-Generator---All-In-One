import os
import tempfile

import streamlit as st
from gtts import gTTS

st.set_page_config(
    page_title="AI Video & Voice Generator",
    page_icon="🎬",
    layout="centered",
)

st.title("AI Video & Voice Generator (Sinhala)")
st.write("මෙතැනින් ඔබට අවශ්‍ය පින්තූර, සිංහල හඬ සහ වීඩියෝ සාදාගත හැක.")


# 1. Sinhala Text to Speech
st.header("1. Sinhala Text to Speech")
sinhala_text = st.text_area(
    "සිංහලෙන් යමක් ලියන්න:",
    "සැමෝටම ආයුබෝවන්! මම AI ඇප් එකක්.",
)


def generate_voice_audio(text: str):
    clean_text = text.strip()
    if clean_text == "":
        raise ValueError("දයාකරලා යමක් ලියන්න!")

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        temp_path = temp_audio.name

    try:
        tts = gTTS(text=clean_text, lang="si", slow=False)
        tts.save(temp_path)
        return temp_path
    except Exception as exc:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise RuntimeError(f"හඬ සකස් කිරීමේදී දෝෂයක් ඇති විය: {exc}") from exc


if st.button("Voice එක සකසන්න"):
    try:
        audio_path = generate_voice_audio(sinhala_text)
        st.audio(audio_path, format="audio/mp3")
        st.success("හඬ සාර්ථකව සකස් කරන ලදී!")
    except Exception as exc:
        st.error(str(exc))
    finally:
        if "audio_path" in locals() and os.path.exists(audio_path):
            os.remove(audio_path)


# 2. Text to Image (Placeholder)
st.header("2. Text to Image")
prompt = st.text_input("පින්තූරයක් සඳහා විස්තරයක් ලියන්න (English වලින්):")
if st.button("පින්තූරය සාදන්න"):
    if prompt.strip():
        st.info("පින්තූර උත්පාදන පහසුකම ඉක්මනින් එකතු කරනු ලැබේ!")
    else:
        st.warning("පින්තූරය සඳහා විස්තරයක් ලියන්න.")
