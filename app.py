import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document
from urllib.parse import urlparse, parse_qs

# Helper to extract YouTube video ID
def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1]
    query = parse_qs(urlparse(url).query)
    return query.get("v", [None])[0]

# Create Document from YouTube transcript
def load_youtube_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL.")
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([t["text"] for t in transcript])
    return [Document(page_content=full_text)]

# Streamlit UI
st.set_page_config(page_title="LangChain: Summarize Text From Youtube or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YouTube or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

# Initialize LLM
if groq_api_key:
    llm = ChatGroq(model="llama3-70b-8192", groq_api_key=groq_api_key)
else:
    llm = None

prompt_template = """
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Button logic
if st.button("Summarize the Content from YT or Website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It may be a YouTube video or website")
    elif llm is None:
        st.error("Groq API Key is missing or invalid.")
    else:
        try:
            with st.spinner("Loading and summarizing..."):
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    docs = load_youtube_transcript(generic_url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )
                    docs = loader.load()

                if not docs:
                    st.error("No transcript or text could be loaded from the provided URL.")
                else:
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.run(docs)
                    st.success("Summary:")
                    st.write(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")
