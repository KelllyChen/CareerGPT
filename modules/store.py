import chromadb
from sentence_transformers import SentenceTransformer
import torch
import uuid
from chunking import chunk_text  # Import chunking function
from data import all_resume_texts # Import extracted resume texts

chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection for resumes
collection = chroma_client.get_or_create_collection(name="resumes")

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2", device="cuda")

print(f"Using device: {embedding_model.device}")


# Batch size for processing chunks
BATCH_SIZE = 32  


for i, resume_text in enumerate(all_resume_texts):
    chunks = chunk_text(resume_text, max_length=300)

    for j in range(0, len(chunks), BATCH_SIZE):
        chunk_batch = chunks[j:j + BATCH_SIZE]
        chunk_embeddings = embedding_model.encode(chunk_batch, batch_size=BATCH_SIZE).tolist()

        # Generate IDs for batch
        doc_ids = [str(uuid.uuid4()) for _ in chunk_batch]

        # Store all embeddings 
        collection.add(
            ids=doc_ids,
            embeddings=chunk_embeddings,
            metadatas=[{"resume_id": i, "chunk_index": j + k, "text": chunk} for k, chunk in enumerate(chunk_batch)]
        )

   

print("Resumes successfully stored in ChromaDB!")    