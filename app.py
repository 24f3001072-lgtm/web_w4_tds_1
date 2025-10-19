from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# --- Enable CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Example answers (could be replaced with RAG logic) ---
answers = {
    "what does the author affectionately call the => syntax": {
        "answer": "The author affectionately calls the '=>' syntax the fat arrow.",
        "sources": "TypeScript Book – Functions > Fat Arrow",
    },
    "which operator converts any value into an explicit boolean": {
        "answer": "The !! operator converts any value into an explicit boolean.",
        "sources": "TypeScript Book – Truthy & Falsy",
    },
}


@app.get("/search")
def search(q: str = Query(..., description="Developer question")):
    query = q.lower().strip()

    # --- simple lookup ---
    for key, value in answers.items():
        if key in query:
            return value

    # --- fallback ---
    return {
        "answer": "No direct match found. Please rephrase your question.",
        "sources": None,
    }
