# Install Groq
# !pip install groq

from groq import Groq

# Enter your Groq API Key
client = Groq(api_key="")

# Knowledge base for related concepts
related_words = {
    "healthcare": ["medicine", "hospital", "clinical"],
    "ai": ["machine learning", "automation", "intelligence"],
    "education": ["learning", "teaching", "students"],
    "technology": ["innovation", "computing", "digital"]
}

# Find related words
def find_similar_words(word):
    return related_words.get(word.lower(), [])

# Enrich prompt
def enrich_prompt(prompt):
    words = prompt.split()
    enriched = []

    for word in words:
        clean_word = word.lower().strip(".,!?;:()")

        similar = find_similar_words(clean_word)

        if similar:
            enriched.append(
                f"{word} (related concepts: {', '.join(similar)})"
            )
        else:
            enriched.append(word)

    return " ".join(enriched)

# Get Groq response
def get_groq_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

# Original prompt
original_prompt = "Write about AI in healthcare."

print("Original Prompt:")
print(original_prompt)

# Enriched prompt
enriched_prompt = enrich_prompt(original_prompt)

print("\nEnriched Prompt:")
print(enriched_prompt)

# Generate responses
original_response = get_groq_response(original_prompt)
enriched_response = get_groq_response(enriched_prompt)

# Display responses
print("\n--- Original Prompt Response ---")
if len(original_response) > 500:
    print(original_response[:1000] + "...")
else:
    print(original_response)

print("\n--- Enriched Prompt Response ---")
if len(enriched_response) > 500:
    print(enriched_response[:1000] + "...")
else:
    print(enriched_response)

# Comparison
print("\nComparison:")

print("Original response length:",
      len(original_response.split()),
      "words")

print("Enriched response length:",
      len(enriched_response.split()),
      "words")

print("Original unique words:",
      len(set(original_response.lower().split())))

print("Enriched unique words:",
      len(set(enriched_response.lower().split())))