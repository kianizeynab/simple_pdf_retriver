import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from ocr_cleaner import get_cleaned_ocr_text
import easyocr

ocr_reader = easyocr.Reader(['en', 'es'])

def extract_text_from_pdf(pdf_path):
    print(f"********************** {pdf_path} ")
    reader = PdfReader(pdf_path)
    texts = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text or text.strip() == "":
            ocr_result = ["OCR simulated text"]
            text = " ".join(ocr_result)
        texts.append(text)
    return texts

def process_pdf_directory(pdf_dir, chunk_size=1000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    all_chunks = []
    metadatas = []

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            pages = extract_text_from_pdf(pdf_path)
            for page_num, page_text in enumerate(pages):
                cleaned_text = get_cleaned_ocr_text(page_text)
                chunks = text_splitter.split_text(cleaned_text)
                for i, chunk in enumerate(chunks):
                    all_chunks.append(chunk)
                    metadatas.append({
                        "source": filename,
                        "page": page_num + 1,
                        "chunk_id": i
                    })
    return all_chunks, metadatas




