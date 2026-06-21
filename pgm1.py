import numpy as np
from gensim.downloader import load
import pprint

# Load FastText model (downloads ~1GB the first time)
model = load('fasttext-wiki-news-subwords-300')

# Similar words to king
print("Similar words to 'king':")
pprint.pprint(model.most_similar('king'))

# Analogy: King - Man + Woman = ?
result = model.most_similar(
    positive=['king', 'woman'],
    negative=['man'],
    topn=1
)
print("\nKing - Man + Woman =", result)

# Analogy: Paris - France + Italy = ?
result = model.most_similar(
    positive=['paris', 'italy'],
    negative=['france'],
    topn=1
)
print("Paris - France + Italy =", result)

# Word vectors
vec_king = model['king']
vec_queen = model['queen']
vec_man = model['man']
vec_woman = model['woman']

# Cosine similarity between king and queen
cosine_similarity = np.dot(vec_king, vec_queen) / (
    np.linalg.norm(vec_king) * np.linalg.norm(vec_queen)
)

print("Cosine Similarity between 'king' and 'queen':",
      cosine_similarity)

# Analogy: Uncle - Man + Woman = ?
result = model.most_similar(
    positive=['uncle', 'woman'],
    negative=['man'],
    topn=1
)
print("Uncle - Man + Woman =", result)

# Exploring semantic similarity
print("\nMost similar words to 'good':")
print(", ".join(word for word, _ in model.most_similar('good')))

print("\nMost similar words to 'bad':")
print(", ".join(word for word, _ in model.most_similar('bad')))