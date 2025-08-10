# Personal Research Assistant (Local Ollama Backend)

A simple Flask web app that acts as a local AI‑powered research assistant.  
It uses [Ollama](https://ollama.com) to run open‑weight LLMs **on your machine** — no cloud API, no usage fees.

---

## Features
- 🔒 **Local‑only** backend (no internet model calls)
- 🔁 Works with any Ollama model (e.g., `mistral`, `llama3.1`, `qwen2:7b`, `phi3:mini`)
- 🧩 Simple HTML + JS frontend served by Flask
- 🧠 JSON `/ask` endpoint you can reuse in other tools
- ⚙️ Tunable performance (`num_ctx`, `num_threads`, `timeout`)

---

## Requirements
- macOS / Linux (tested on macOS M2 Pro)
- [Ollama](https://ollama.com/download) installed & running
- Python **3.11+**
- Python packages: `flask`, `requests`

---

## Quick Start

### 1) Install & start Ollama
```bash
# Install from https://ollama.com/download (run the app once)

# Pull a lightweight model (recommended for laptops)
ollama pull mistral

# (Optional) keep logs visible for debugging
ollama serve
```
### 2) Clone the Project
``` bash
git clone https://github.com/YOUR_USERNAME/personal-research-assistant.git
cd personal-research-assistant
```
### 3) Install Python Deps
```bash
pip install flask requests
```
### 4) Run the App
```bash
# Choose your model (can be mistral, llama3.1, qwen2:7b, phi3:mini)
export OLLAMA_MODEL=mistral

# Start Flask (serves static/index.html)
python app.py
```
### 5) Open in your Browser
```bash
http://127.0.0.1:5000
Type a topic → Ask.
```
## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

