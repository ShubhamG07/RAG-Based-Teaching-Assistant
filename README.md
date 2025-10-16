# 🎓 RAG-Based Teaching Assistant

> **“Ask your course — and it tells you exactly *where* to learn what you need.”**  

This project is a **Retrieval-Augmented Generation (RAG)** powered **Teaching Assistant** that can:
- 🧠 **Understand your course playlist**
- 🎧 **Transcribe & translate** every lecture using **Groq API**
- 🧩 **Generate embeddings** for semantic understanding
- 🔍 **Find the exact timestamp & video** where a specific topic is taught!

Perfect for learners who want to **instantly locate concepts** in long video-based courses.

---

## 🚀 Features

✅ Add an entire **playlist** of videos  
✅ Automatically **convert videos → audios** using FFmpeg  
✅ **Split long audios** into 10-minute chunks for efficient processing  
✅ **Translate + Transcribe** using **Groq API** (JSON output)  
✅ **Generate embeddings** using **Jina AI API** (or Ollama’s `bge-m3` locally)  
✅ **Store all embeddings** in a pandas DataFrame (`embeddings.joblib`)  
✅ **Ask natural questions** like:  
> “Where is binary search explained?”  
and get a precise response like:  
> “Binary Search is taught in *Video 2* at **08:43**.”

---
## ⚙️ Step-by-Step Usage

**Step 1: Collect Course Videos**
- Place all your course videos in the Videos/ folder.

**Step 2: Convert Videos to MP3**
- Run
```bash
 python video_to_mp3.py
```
This will use FFmpeg to convert all videos into audio files and store them in Audios/.

**Step 3: Split Long Audios (if >10 min)**
- Run:
```bash
 python breaking_audio_in_10min_parts.py
```
This script breaks large audio files into 10-minute chunks to optimize transcription.

**Step 4: Translate & Transcribe**
- Run
```bash
 python mp3_to_json.py
```
This uses the Groq API to:

- Transcribe each audio chunk

- Translate non-English segments

- Save results as .json files in the Json/ folder

**Step 5: Generate Embeddings**
- Run
```bash
 python preprocessing_json_embeddings.py
```
This script:

- Converts all transcript chunks into embeddings using Jina API (or Ollama locally)

- Stores them in a pandas DataFrame

- Saves the DataFrame as embeddings.joblib

**Step 6: Process User Queries**
- Run
```bash
 python processing_user_query.py
```
This:

- Takes the user’s question

- Converts it into an embedding

- Finds the closest matches using cosine similarity

- Returns the video name + timestamp where the answer is taught

**Step 7: Get the Final AI Response**
- Finally, with the help of the Groq API, you’ll get a formatted, natural-language answer like:

> “The concept of gradient descent is explained in Lecture 4 (Deep Learning Basics) at 12:17.”
 
---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | 🐍 Python |
| Embeddings | 🧬 Jina API / Ollama (BGE-M3) |
| Transcription / Translation | ⚡ Groq API |
| Data Handling | 🐼 Pandas, NumPy |
| ML / Similarity | 🎯 Scikit-Learn (Cosine Similarity) |
| Audio Processing | 🎵 FFmpeg, Pydub |
| Model Storage | 💾 Joblib |
| Networking | 🌐 Requests, Subprocess |

---

## 🧩 Workflow Overview

```mermaid
graph TD
A[Video Folder] -->|Convert| B[Audio Files]
B -->|Split 10-min Chunks| C[Audio Parts]
C -->|Groq API| D[Translated + Transcribed JSONs]
D -->|Jina Embeddings| E[Embeddings DataFrame]
E -->|Save| F[embeddings.joblib]
F -->|Query with Groq + Cosine Similarity| G[Precise Time + Video Result]
