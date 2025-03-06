# Assignment 3
## Objective
- Improve response performance in career development using Retrieval-Augmented Generation (RAG).
- Enhance career guidance by combining semantic search and large language models (LLMs). 

## Real Time Use Case
 - Retrieve the most recent public resumes.
 - Introduce users to essential skills in demand for specific careers.
 - Utilize RAG to ensure contextually relevant and up-to-date responses.
 - Help users gain career guidance based on current job market trends. 

 ## Data
 - Resume Dataset – [Kaggle](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset?resource=download)

 ## Pipeline
 - Use fitz package to extract texts from pdfs
 - Chunk the texts by paragraph, set max_length=300
 - Use all-MiniLM-L6-v2 for embedding
 - Store into ChromaDB
 - Semantic Search => cosine_similarity 
 - Insert relevant context into the GPT-4 prompt 

 ## Model
 - OpenAI’s GPT-4

 ## Evaluation
 - Rouge Score
    - ROUGE-1 (Measures Unigram Overlap - single words)
    - ROUGE-2 (Measures Bigram Overlap - two-word sequences)
    - ROUGE-L (Measures Longest Common Subsequence Overlap)
 
 ## Demo
 - https://huggingface.co/spaces/kellly/RAG_resume
 - Or run it locally
 `streamlit run app.py `

 
 



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/a87xfYGP)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18256923)
