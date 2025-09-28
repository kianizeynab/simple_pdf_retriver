
from pdf_processor import process_pdf_directory
from embeddings import create_vectorstore

def build_index_main():
    print("⚙️ Starting to build index...")
    docs,metadatas = process_pdf_directory("pdfs")
    create_vectorstore(docs,metadatas)
    print("✅ Index build completed.")

if __name__ == "__main__":
    build_index_main()

