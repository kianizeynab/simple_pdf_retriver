from build_index import build_index_main

# 🔄 ساخت ایندکس در شروع
build_index_main()

from fastapi import FastAPI
from embeddings import load_vectorstore
from sentence_transformers import CrossEncoder
from pydantic import BaseModel

app = FastAPI()

vectorstore = load_vectorstore()
reranker_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/search")
def search(request: QueryRequest):
    results = vectorstore.similarity_search(request.query, k=request.top_k*2)
    pairs = [(request.query, r.page_content) for r in results]
    scores = reranker_model.predict(pairs)
    ranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
    top_results = [{"metadata": r.metadata, "text": r.page_content[:500]} for r, s in ranked[:request.top_k]]
    return {"results": top_results}
