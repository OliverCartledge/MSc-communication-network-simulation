from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('all-mpnet-base-v2')

def semantic_similarity(text1, text2):

    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)

    score = cos_sim(emb1, emb2)
    
    return float(score)

print(semantic_similarity("I love programming.", "I enjoy coding."))