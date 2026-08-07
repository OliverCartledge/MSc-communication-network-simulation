from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

from transformers import pipeline

#SBERT model for semantic similarity
model = SentenceTransformer('all-mpnet-base-v2')

#Sentiment analysis model | https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
sentiment_model = pipeline("sentiment-analysis", model = "cardiffnlp/twitter-roberta-base-sentiment-latest")

def semantic_similarity(text1, text2):

    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)

    score = cos_sim(emb1, emb2)
    
    return float(score)

def sentiment_analysis(text):
    result = sentiment_model(text)[0]

    return {
        "label": result["label"],
        "confidence": float(result["score"])
    }