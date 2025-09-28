from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embedding_model_name = "sentence-transformers/distiluse-base-multilingual-cased-v2"
embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

def create_vectorstore(chunks, metadatas, save_path="vectorstore"):
    vectorstore = FAISS.from_texts(chunks, embeddings, metadatas=metadatas)
    vectorstore.save_local(save_path)
    return vectorstore

from langchain_community.vectorstores import FAISS

def load_vectorstore(path="vectorstore"):
    from embeddings import embeddings
    return FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True  # ← اینو اضافه کن
    )


