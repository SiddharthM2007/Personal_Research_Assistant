from flask import Flask, request, jsonify

# Serve files from ./static and map "/" to index.html
app = Flask(__name__, static_url_path='', static_folder='static')

@app.route("/")
def serve_home():
    # Send static/index.html when "/" is requested
    return app.send_static_file("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    # Read JSON: { "question": "..." }
    data = request.get_json(force=True)  # force=True tolerates missing headers
    topic = (data or {}).get("question", "").strip()

    if not topic:
        return jsonify({"error": "No question provided"}), 400

    # Demo response (we'll plug in ChatGPT next)
    summary = f"(demo) You asked about: {topic}\nThis is where an AI summary will appear."
    return jsonify({"answer": summary})

if __name__ == "__main__":
    app.run(debug=True)
    