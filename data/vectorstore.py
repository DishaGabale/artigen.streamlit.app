
import warnings
warnings.filterwarnings("ignore", message="Unsupported Windows version")

import numpy as np
import json
from langchain_community.vectorstores import Chroma

# Load embeddings and metadata from the files
embeddings = np.load(r'D:\prodigal_hackathon\embeddings1.npy')
with open(r'D:\HACKATHON\metadata1.json', 'r', encoding='utf-8') as file:
    metadata = json.load(file)
    
# Initialize Chroma vector store with persistent storage
persist_directory = r'D:\HACKATHON\vector_store'
vector_store = Chroma(collection_name='gov_schemes', persist_directory=persist_directory)

# Prepare documents to add
texts = []
metadatas = []
embeddings_list = []

for i, embedding in enumerate(embeddings):
    page_content = (
        f"{metadata[i]['scheme_name']} "
        f"{metadata[i]['section']} "
    )
    texts.append(page_content)
    
    # Convert keywords list to a string if it exists
    keywords_str = ', '.join(metadata[i].get('keywords', []))  # Convert list to a comma-separated string
    
    metadatas.append({
        'scheme_name': metadata[i]['scheme_name'],
        'section': metadata[i]['section'],
        'keywords': keywords_str,
        'source': metadata[i]['source'],
    })
    embeddings_list.append(embedding.tolist())  

# Add documents to Chroma
for i, text in enumerate(texts):
    vector_store._collection.upsert(
        embeddings=[embeddings_list[i]],
        metadatas=[metadatas[i]],
        documents=[text],
        ids=[metadatas[i]['scheme_name'] + "_" + metadatas[i]['section']]  # Creating a unique ID
    )

vector_store.persist()
def load_vector_store():
    """Load and return the initialized Chroma vector store."""
    return vector_store

def similarity_search(query, k=5):
    """
    Perform a similarity search on the vector store.

    Args:
    - query (str): The query string to search for.
    - k (int): The number of top results to return.

    Returns:
    - list: A list of relevant documents based on the query.
    """
    return vector_store.similarity_search(query, k=k)

# Import functions from vectorstore.py
from vectorstore import load_vector_store, similarity_search
from transformers import pipeline

# Load your vector store
vector_store = load_vector_store()

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt-3.5-turbo')  # Replace with your preferred model

def generate_unique_content(prompt, vector_store):
    """
    Generate unique content by retrieving relevant context from vector store
    and generating text using a language model.

    Args:
    - prompt (str): The initial prompt or query for content generation.
    - vector_store: The loaded vector store for retrieving relevant context.

    Returns:
    - str: Generated article text.
    """
    # Retrieve relevant documents based on the prompt
    retrieved_docs = similarity_search(prompt, k=5)  # Adjust 'k' for the number of results

    # Combine retrieved documents into a context string
    context = "\n\n".join([doc['page_content'] for doc in retrieved_docs])  # Assuming docs have 'page_content'

    # Formulate the prompt for the language model
    full_prompt = f"Generate a detailed article on the following topic: {prompt}\n\nContext: {context}\n\n"

    # Generate text based on the prompt and retrieved context
    result = generator(full_prompt, max_length=1000, truncation=True)

    return result[0]['generated_text']

# Example usage
prompt = "Write an article on the latest government schemes for renewable energy."
unique_content = generate_unique_content(prompt, vector_store)
print(unique_content)
