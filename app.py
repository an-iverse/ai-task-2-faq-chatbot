"""Task 2: FAQ chatbot using TF-IDF vectors and cosine similarity."""
import json
from pathlib import Path

from flask import Flask, jsonify, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
FAQS = json.loads(Path("faq_data.json").read_text(encoding="utf-8"))

# TF-IDF preprocesses words into numerical features. English stop words such as
# "the" and "is" are removed because they do not help identify intent.
vectorizer = TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))
question_vectors = vectorizer.fit_transform([item["question"] for item in FAQS])
MIN_CONFIDENCE = 0.10


@app.get("/")
def index():
    return render_template("index.html", suggestions=[item["question"] for item in FAQS])


@app.post("/ask")
def ask():
    message = str((request.get_json(silent=True) or {}).get("message", "")).strip()
    if not message:
        return jsonify(answer="Please type a question first.", confidence=0), 400

    user_vector = vectorizer.transform([message])
    scores = cosine_similarity(user_vector, question_vectors)[0]
    best_index = scores.argmax()
    confidence = float(scores[best_index])

    if confidence < MIN_CONFIDENCE:
        return jsonify(answer="I do not have an answer for that yet. Please try asking about AI, machine learning, NLP, Python, or learning AI.", confidence=round(confidence, 2))
    return jsonify(answer=FAQS[best_index]["answer"], matched_question=FAQS[best_index]["question"], confidence=round(confidence, 2))


if __name__ == "__main__":
    app.run(debug=True)
