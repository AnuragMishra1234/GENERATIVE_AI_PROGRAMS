import PyPDF2
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="")

model = genai.GenerativeModel("gemini-2.5-flash")

# Read PDF
text = "".join(
    page.extract_text() or ""
    for page in PyPDF2.PdfReader(open("indian penal code.pdf", "rb")).pages
)

# Split into chunks
chunks = text.split(". ")

# Create embeddings
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embed_model.encode(chunks)

print("\nIPC Chatbot: Ask me about IPC. Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    # Find best matching chunk
    question_embedding = embed_model.encode([question])

    best_index = np.argmax(
        cosine_similarity(question_embedding, embeddings)
    )

    context = chunks[best_index]

    # Generate detailed answer
    prompt = f"""
    You are an expert Indian Penal Code assistant.

    Context from IPC PDF:
    {context}

    User Question:
    {question}

    Give a detailed answer in simple English.

    Include:
    1. Introduction
    2. Explanation
    3. Important points
    4. Example
    5. Punishment (if applicable)

    Make the answer at least 200-300 words.
    """

    response = model.generate_content(prompt)

    print("\nIPC Bot:\n")
    print(response.text)
    print("\n" + "="*80 + "\n")

print("Exiting chatbot...")