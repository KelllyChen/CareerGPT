from transformers import pipeline
from search import semantic_search  # Keep your semantic search function
from rouge_score import rouge_scorer

# Load a local LLM (choose a smaller model if needed)
#generator = pipeline("text-generation", model="distilgpt2")
generator = pipeline("summarization", model="facebook/bart-large-cnn")

def query_llm(context, question):
    prompt = f"""
    Based on the following qualifications and skills, list the key technical skills and qualifications needed for this career:

    Context: {context}

    Answer:
    """
    # Generate a response using the local model
    response = generator(prompt, max_new_tokens=100, do_sample=True)

    #return response[0]["generated_text"]
    return response[0]["summary_text"]

def evaluate_summary(generated_summary, reference_summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_summary, generated_summary)
    return scores


# Test semantic search and then pass to LLM
#query = "Machine learning engineer with Python experience"  # Example user query
query = "Engineer with Python experience"
search_results = semantic_search(query)  # Perform the semantic search

# Combine the metadata or chunks for context (adjust based on your structure)
retrieved_chunks = " ".join([chunk["text"] for chunk in search_results])  # Adjust if necessary

print("Retrieved Chunks:", retrieved_chunks)
question = "Summarize the skills"

# Query the LLM with context and question
response = query_llm(retrieved_chunks, question)

# Print the LLM response
print("LLM Response:", response)


# Example reference summary (ground truth)
reference_summary = "C++, Python, SQL, Scikit-learn, Pandas"
# Compute ROUGE scores
rouge_scores = evaluate_summary(response, reference_summary)
print("ROUGE Scores:", rouge_scores)