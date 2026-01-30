# 🦜 Website & YouTube Summarizer

A powerful Streamlit web application that intelligently summarizes web pages and YouTube videos using Groq LLMs, LangChain, and OpenAI Whisper. Support for multiple languages with downloadable summaries.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<img width="1898" height="884" alt="Screenshot 2026-01-31 045225" src="https://github.com/user-attachments/assets/36048bab-11c1-4f10-b9b8-b34f981aa006" />

## ✨ Features
-  **Website Summarization** - Extract and summarize article content from any URL
-  **YouTube Video Summarization** - Download audio, transcribe, and summarize videos
-  **Fast LLM Inference** - Powered by Groq's high-performance API
-  **Multi-language Support** - Generate summaries in:
  - English
  - Hindi
  - French
  - Spanish
- 📥 **Download Summaries** - Save summaries as `.txt` files
- ⚡ **Token-safe Processing** - Automatic truncation for large content

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| LLM | Groq (llama-3.1-8b-instant) |
| Framework | LangChain |
| Speech-to-Text | OpenAI Whisper |
| YouTube Audio | yt-dlp |
| Web Scraping | UnstructuredURLLoader |

## 📁 Project Structure

```
URLandYTSummarizer/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Ignored files (venv, cache, secrets)
```

##  Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rituraj1404/URLandYTSummarizer.git
cd URLandYTSummarizer
```

### 2️⃣ Create & Activate Virtual Environment

**Python 3.10 is recommended**

```bash
# Windows
py -3.10 -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3.10 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install FFmpeg

> ⚠️ **Important:** FFmpeg cannot be installed via pip and must be installed separately.

**Windows:**
1. Download from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extract and add to PATH

**Linux:**
```bash
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Verify Installation:**
```bash
ffmpeg -version
```

### 5️⃣ Get Groq API Key

1. Visit [https://console.groq.com](https://console.groq.com)
2. Create an account and generate an API key
3. Your key will start with `gsk_`

### 6️⃣ Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at: **http://localhost:8501**

## 🧪 How It Works

### Website Summarization Flow

```
URL Input → Extract Content → Clean & Truncate → Groq LLM → Summary
```

1. Extracts webpage content using UnstructuredURLLoader
2. Cleans and truncates text to fit token limits
3. Sends content to Groq LLM for summarization
4. Returns concise summary in selected language

### YouTube Summarization Flow

```
YouTube URL → Download Audio → Convert (FFmpeg) → Transcribe (Whisper) → Groq LLM → Summary
```

1. Downloads audio using yt-dlp
2. Converts audio format using FFmpeg
3. Transcribes speech using OpenAI Whisper
4. Summarizes transcription via Groq LLM

## 📝 Usage Example

1. **Enter Groq API Key** in the sidebar
2. **Select Input Type** (Website URL or YouTube URL)
3. **Choose Language** for summary
4. **Paste URL** and click "Summarize"
5. **Download Summary** using the download button

## ⚠️ Important Notes

- ❌ **Do NOT** upload virtual environments (`venv/`, `.venv/`)
- ❌ **Do NOT** commit API keys to version control
- ✅ Always use `requirements.txt` to recreate environments
- ⚠️ Large videos may take time to transcribe
- 💡 Ensure stable internet connection for API calls

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| FFmpeg not found | Verify FFmpeg is installed and in PATH |
| API key error | Check that your Groq API key is valid |
| Large file timeout | Try with shorter videos or websites |
| Transcription errors | Ensure audio quality is sufficient |

## 🌱 Future Improvements

- [ ] Chunk-based summarization for very long content
- [ ] Support for PDF document summarization
- [ ] Deployment on Streamlit Cloud
- [ ] Enhanced UI/UX with progress indicators
- [ ] Support for additional languages
- [ ] Summary customization options (length, style)
- [ ] Batch processing for multiple URLs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Rituraj Negi**

- GitHub: [@Rituraj1404](https://github.com/Rituraj1404)
- Project Link: [https://github.com/Rituraj1404/URLandYTSummarizer](https://github.com/Rituraj1404/URLandYTSummarizer)

## ⭐ Show Your Support

If you find this project helpful, please give it a ⭐ on GitHub — it really helps!

---

<div align="center">
Made with ❤️ by Rituraj Negi
</div>
