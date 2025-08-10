# app.py — Flask + Ollama via /api/generate

from flask import Flask, request, jsonify
import os
import requests

# ---- Config ----
MODEL = os.getenv("OLLAMA_MODEL", "mistral")                 # e.g., mistral, llama3.1, qwen2:7b, phi3:mini
GEN_URL = os.getenv("OLLAMA_GEN_URL", "http://127.0.0.1:11434/api/generate")
NUM_CTX = int(os.getenv("OLLAMA_NUM_CTX", "2048"))           # lower = less RAM
NUM_THREADS = int(os.getenv("OLLAMA_NUM_THREADS", "6"))      # reduce CPU pressure
REQUEST_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "120"))    # allow cold start

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/health")
def health():
    try:
        r = requests.get("http://127.0.0.1:11434/api/tags", timeout=10)
        r.raise_for_status()
        return jsonify({"ok": True, "models": r.json().get("models", [])})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 503

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    topic = (data.get("question") or "").strip()
    if not topic:
        return jsonify({"error": "No question provided"}), 400

    # Build a single prompt (since /api/generate is prompt-based, not chat-based)
    prompt = (
        "You are a concise, factual research assistant.\n\n"
        "Summarize this topic for a beginner in ≤200 words and include 3 follow-up questions.\n"
        f"Topic: {topic}\n"
    )

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": NUM_CTX,
            "num_threads": NUM_THREADS,
        },
    }

    try:
        resp = requests.post(GEN_URL, json=payload, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()

        # /api/generate returns {"response": "...", "done": true, ...}
        content = data.get("response", "")
        if not content:
            return jsonify({"error": "Empty response from model."}), 502

        return jsonify({"answer": content})

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": (
                "Cannot connect to Ollama at 127.0.0.1:11434. "
                "Open the Ollama app and pull a model (e.g., `ollama pull mistral`)."
            )
        }), 502
    except requests.HTTPError as e:
        return jsonify({"error": f"Ollama HTTP error: {e}"}), 502
    except requests.Timeout:
        return jsonify({"error": "Model timed out. Increase OLLAMA_TIMEOUT or try a smaller model."}), 504
    except Exception as e:
        return jsonify({"error": f"Ollama error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

    



