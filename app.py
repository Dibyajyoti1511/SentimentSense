# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")
USE_LOCAL_MODEL = os.path.isdir(MODEL_DIR) and os.listdir(MODEL_DIR)

if USE_LOCAL_MODEL:
    # Load the local fine-tuned model and tokenizer
    from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
    print("Loading local model from", MODEL_DIR)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
else:
    # Fallback: use HF hosted pipeline (downloads model automatically)
    from transformers import pipeline
    print("Local model not found — using HF pipeline (distilbert-base-uncased-finetuned-sst-2-english).")
    nlp = pipeline("sentiment-analysis")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Expects JSON: {"text": "some input text"}
    Returns: {"label": "POSITIVE"/"NEGATIVE", "score": float}
    """
    data = request.get_json(force=True)
    text = data.get("text", None)
    if not text or not isinstance(text, str):
        return jsonify({"error": "Invalid input. Send JSON with 'text' key."}), 400

    try:
        result = nlp(text[:1000])  # limit length for efficiency
        # pipeline returns a list of dicts; get first
        out = result[0]
        return jsonify({"label": out.get("label"), "score": float(out.get("score"))})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model_loaded": bool(USE_LOCAL_MODEL)})

if __name__ == "__main__":
    # For local dev
    app.run(host="0.0.0.0", port=5000, debug=True)
