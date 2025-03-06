from data import extract_text_from_resumes
import re


def chunk_text(text, max_length=300):
    # Chunk by paragraphs 
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) < max_length:
            current_chunk += " " + paragraph
        else:
            chunks.append(current_chunk)
            current_chunk = paragraph
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


# Chunking all resume texts
all_chunks = []
base_folder_path = "./data/data" 
all_resume_texts = extract_text_from_resumes(base_folder_path)
for resume_text in all_resume_texts:
    chunks = chunk_text(resume_text, max_length=300)
    all_chunks.extend(chunks)

print(f"Number of chunks: {len(all_chunks)}")
