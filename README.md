# PDF Processing & Search API

This project extracts text from PDFs, cleans it using OCR, creates embeddings, and provides a search API with ranking.

---

## Features

- OCR-based PDF text extraction using **EasyOCR**
- Text cleaning and noise removal
- Vector embeddings with **Sentence Transformers** (`distiluse-base-multilingual-cased-v2`)
- FAISS vector store for similarity search
- Optional ranking with **Cross-Encoder**
- FastAPI-based search API

---

## Quick Start with Docker

### 1. Build the Docker Image

```bash
docker build -t pdf_app .
```

### 2. Run the Docker Container

```bash
docker run -p 8000:8000 -v /path/to/pdfs:/app/pdfs pdf_app
```

- Replace `/path/to/pdfs` with the folder containing your PDF files.
- The API will be available at: `http://localhost:8000`

---

## Running Without Docker

If you want to run the project locally:

### 1. Install Python Dependencies

Make sure you have **Python 3.11+** installed.

```bash
# Create a virtual environment
python -m venv env

# Activate it
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt
```


### 2. Run the FastAPI App

```bash
uvicorn app:app --reload

```

- The API will be available at: `http://127.0.0.1:8000/docs#/default/search_search_post`
- `/search` endpoint accepts POST requests with JSON:

```json
{
  "query": "Your search text",
  "top_k": 5
}
```

---

## Example Request (Python)

```python
import requests

url = "http://localhost:8000/search"
data = {"query": "machine learning", "top_k": 3}

response = requests.post(url, json=data)
print(response.json())
```

---

## Notes

- Recommended to use a GPU for faster OCR and embedding generation.
- Make sure PDFs are clean and legible for best results.
- For Docker, PDFs are mounted using a volume (`-v`) t
