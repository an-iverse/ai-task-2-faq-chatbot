# Task 2 — FAQ Chatbot for AI

This Flask chatbot finds the closest question in its FAQ dataset using NLP-style text preprocessing (lowercasing, English stop-word removal, TF-IDF vectors) and cosine similarity. It then displays the matching answer.

## Run it

1. Install Python 3.11 or newer from https://www.python.org/downloads/ (tick **Add Python to PATH**).
2. In this folder, open PowerShell and run:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   flask --app app run
   ```
3. Open `http://127.0.0.1:5000` in a browser.

## Demonstration checklist

- Ask: `Explain machine learning`.
- Ask: `Which language should I learn for AI?`.
- Ask an unrelated question to demonstrate the low-confidence fallback.
- Open `faq_data.json` to show how more FAQs can be added.

## One-minute explanation

The app reads FAQ questions from a JSON file. `TfidfVectorizer` changes the known questions and the user question into numerical word vectors. Cosine similarity compares those vectors; the question with the highest score supplies the chatbot's answer. If the score is low, the chatbot says it does not know.
