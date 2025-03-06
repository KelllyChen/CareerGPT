import openai
import streamlit as st
from modules.search import semantic_search  
from rouge_score import rouge_scorer

# Set up OpenAI API key
openai.api_key = ""  # Use your OpenAI API key here

def query_llm(context, question):
    # Prepare the conversation structure for GPT-4
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context: {context}"},
        {"role": "user", "content": f"Question: {question}"}
    ]
    
    # Call the GPT-4 model via OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4",  # Use GPT-4 model
        messages=messages,  # Messages structure as required
        max_tokens=200,  # Limit the number of tokens in the response
        temperature=0.7,  # Control randomness in the response
    )
    
    # Extract the generated text from the response
    return response.choices[0].message.content.strip()

def evaluate_summary(generated_summary, reference_summary):
    """Compute ROUGE scores for evaluating the generated summary."""
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_summary, generated_summary)
    return scores

def main():
    st.title("LLM Query Application")

    # User input: Query and Question
    query = st.text_input("Enter your career:", "Machine Learning Engineer")
    question = st.text_input("Enter your question:", "What skills do they have")
    reference_summary = st.text_area("Enter reference summary (for evaluation):", "Python, Scikit-learn, Pandas, deep learning")

    # Display the query and question
    st.write("Query:", query)
    st.write("Question:", question)

    if query and question:
        # Perform semantic search
        search_results = semantic_search(query)  # Perform the semantic search

        # Combine the metadata or chunks for context
        retrieved_chunks = " ".join([chunk["text"] for chunk in search_results])  # Adjust if necessary
        st.write("Retrieved Chunks:", retrieved_chunks)

        # Query the LLM with context and question
        response = query_llm(retrieved_chunks, question)

        # Display the LLM response
        st.write("LLM Response:", response)

        if reference_summary:
            scores = evaluate_summary(response, reference_summary)
            st.write("ROUGE Scores:", scores)

if __name__ == "__main__":
    main()
