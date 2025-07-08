▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=z5Emuv6UMdc&ab_channel=Jatin)  
---

````markdown
# 🧠 Website & YouTube Video Summarizer using LangChain + Groq

> A powerful and easy-to-use Streamlit app that summarizes **YouTube videos** and **web articles** using LLMs from **Groq**, powered by **LangChain**.

---

## 📌 Why I Built This

I come from a humble background, currently pursuing my **MCA**, and learning every day through practice.  
Building this tool was not just a portfolio exercise — it was born from the **need to consume faster, understand deeper, and summarize better**.

In a world where we’re overloaded with content, this app helps users instantly extract the **core insights** from:

- 🎥 YouTube lectures and podcasts
- 🌐 Blog articles, research links, or documentation

I hope this makes someone's life easier — and helps me land a meaningful role in AI, LLM Engineering, or Machine Learning.

---

## 🔍 What It Does

- ✂️ Summarizes any **YouTube video** by extracting transcript
- 📄 Summarizes text from **any public website**
- ⚡ Built with Groq’s blazing fast **LLaMA3-70B**
- 🧠 Uses **LangChain summarize chain + PromptTemplate**
- 🎛️ Neat UI using Streamlit + `.env` protected API

---

## 📺 Sample Use-Cases

- Quickly grasp 1-hour lectures from YouTube in seconds
- Summarize technical blogs or news articles
- Understand long content without reading every word

---

## 🧪 Example Prompt

> Summarize this YouTube video:  
> `https://www.youtube.com/watch?v=VIDEO_ID`  

> Summarize this blog:  
> `https://huggingface.co/blog/llm-evaluation`

---

## 📁 Folder Structure

```bash
.
├── app.py             # Main app
├── .env               # Contains GROQ_API_KEY
├── test.py            # Optional helper/test file
├── venv/              # Created with uv
├── requirements.txt   # All dependencies
└── README.md
````

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Project

```bash
git clone https://github.com/jatinydav557/website-yt-summarizer-langchain.git
cd website-yt-summarizer-langchain
```

### 2️⃣ Create Environment & Install

```bash
uv venv venv
source venv/bin/activate  # or use `venv\Scripts\activate` on Windows
uv pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Open in browser: `http://localhost:8501`

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-community
langchain-groq
youtube-transcript-api
unstructured
validators==0.28.1
python-dotenv
```

---

## 💬 Behind the Code

This project uses:

* `UnstructuredURLLoader` to fetch website text
* `YouTubeTranscriptAPI` to get video transcripts
* `LangChain load_summarize_chain` to summarize with prompt tuning
* `Groq LLaMA3` for powerful generation (faster than OpenAI!)

---

## 👨‍💻 About Me

I’m a self-driven **final-year MCA student** with a passion for building tools that **solve real problems**.
Despite financial constraints, I’m constantly pushing boundaries through practice, hands-on projects, and AI research.

📌 Looking for roles in:

* 🧠 LLM / AI Development
* 📊 Data Science / ML
* ⚙️ Backend / Python / MLOps
* 📫 [Reach out on LinkedIn](https://www.linkedin.com/in/yourusername)

🙏 If this project inspires you or helps you, feel free to ⭐ it!

---

## ✨ Future Plans

* Add file upload + video embedding
* Expand to multilingual summarization
* Deploy to Hugging Face Spaces or GCP

---

> Thank you for checking out my work.
> If you’re a recruiter or collaborator, I’d love to connect and grow further — this project means a lot to me 💙

```

---

Let me know if you'd like a **dark-themed banner** for this project too, or want to add a **YouTube video demo** or **LinkedIn badge**.

You're building **real, useful things** — that's what gets people jobs. Keep going.
```
