from gensim.models import Word2Vec

# Medical corpus
corpus = [
    "patient diagnosed with diabetes",
    "diabetes treatment includes insulin therapy",
    "doctor recommends diabetes treatment",
    "patient receives insulin treatment",
    "therapy helps diabetes patients",
    "vaccine prevents viral infections",
    "vaccination protects against infections",
    "doctor recommends vaccine for prevention",
    "symptoms include fever pain and infection",
    "fever and pain are common symptoms",
    "antibiotics treat bacterial infections",
    "infection treatment may involve antibiotics",
    "doctor prescribes antibiotics for infection",
    "therapy improves patient recovery",
    "medical treatment helps patient recovery"
]

# Tokenize sentences
data = [sentence.split() for sentence in corpus]

# Train Word2Vec model
model = Word2Vec(
    sentences=data,
    vector_size=200,
    window=5,
    min_count=1,
    epochs=500
)

# Display top 5 words similar to "treatment"
print("Top 5 words similar to 'treatment':")
print(model.wv.most_similar("treatment", topn=5))

# Get the most similar word
most_similar_word, similarity_score = model.wv.most_similar(
    "treatment",
    topn=1
)[0]

print("\nMost Similar Word to 'treatment':")
print(f"{most_similar_word} ({similarity_score:.2f})")