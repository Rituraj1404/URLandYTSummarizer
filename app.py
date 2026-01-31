import streamlit as st
import validators
import os
import tempfile

import whisper
import yt_dlp

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import UnstructuredURLLoader

def truncate_to_token_limit(text: str, max_tokens: int = 4500) -> str:
    """
    Rough token-safe truncation.
    1 token ≈ 4 characters (safe approximation)
    """
    max_chars = max_tokens * 4
    return text[:max_chars]



# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Website & YouTube Summarizer",
    page_icon="🦜"
)

st.title("🦜 Website & YouTube Summarizer")
st.subheader("Put your Website or Youtube URL here :")


# ---------------- SIDEBAR ----------------
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password")


url = st.text_input(
    "Paste Website or YouTube URL",
    label_visibility="collapsed"
)

summary_language = st.selectbox(
    "Summary language",
    ["English", "Hindi", "French", "Spanish"],
    index=0
)

# ---------------- YOUTUBE → WHISPER ----------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")   


def youtube_to_text(video_url: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(tmpdir, "%(id)s.%(ext)s"),
            "quiet": True,
            "user_agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        audio_file = None
        for file in os.listdir(tmpdir):
            if file.startswith(info["id"]):
                audio_file = os.path.join(tmpdir, file)
                break

        if not audio_file:
            raise RuntimeError("Audio download failed. No audio file found.")

        model = load_whisper_model()
        result = model.transcribe(audio_file)

        return result["text"]




# ---------------- BUTTON ----------------
if st.button("Summarize"):

    # -------- VALIDATION --------
    if not groq_api_key or not url:
        st.error("Please provide Groq API key and a URL.")
        st.stop()

    if not groq_api_key.startswith("gsk_"):
        st.error("Invalid Groq API key.")
        st.stop()

    if not validators.url(url):
        st.error("Please enter a valid URL.")
        st.stop()

    try:
        with st.spinner("Loading and summarizing..."):

            # -------- LOAD CONTENT --------
            if "youtube.com" in url or "youtu.be" in url:
                st.info("Detected YouTube video → using Whisper transcription")
                full_text = youtube_to_text(url)

            else:
                st.info("Detected website → extracting page text")
                loader = UnstructuredURLLoader(
                    urls=[url],
                    mode="elements",
                    headers={"User-Agent": "Mozilla/5.0"}
                )

                docs = loader.load()

                full_text = "\n\n".join(
                    d.page_content for d in docs if d.page_content.strip()
                )

            if not full_text.strip():
                st.error("No readable content found.")
                st.stop()

            # -------- STUFF (TOKEN SAFE) --------
            original_length = len(full_text)

            full_text = truncate_to_token_limit(
            full_text,
            max_tokens=4200
             )

            truncated_length = len(full_text)
            
            # Show warning only if truncation is extreme
            if truncated_length < 0.4 * original_length:
                 st.info(
            "⚠️ The content is extremely large. "
             "Only the most relevant portion was summarized."
                )




            # -------- LLM (PRODUCTION MODEL) --------
            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                groq_api_key=groq_api_key,
                temperature=0
            )

            prompt = ChatPromptTemplate.from_template(
                """
                 Summarize the following content clearly and concisely.
                  Write the summary in {language}.
                 Focus on the main ideas and key points.

                       Content:
                    {text}
                   """
                 )

            chain = prompt | llm | StrOutputParser()

            summary = chain.invoke({
            "text": full_text,
             "language": summary_language
                })


            st.success(summary)
            
            st.download_button(
               label="⬇️ Download summary (.txt)",
               data=summary,
               file_name="summary.txt",
               mime="text/plain"
                 )
            st.info("You can download or copy the summary for later use.")



    except Exception as e:
        st.exception(e)
