# Personal Research Assistant (Local Ollama Backend)

A simple Flask web app that serves as a local AI-powered research assistant, using [Ollama](https://ollama.com) to run open-weight LLMs directly on your machine — no cloud API or usage costs.

## Features
- Local-only backend (no internet model calls)
- Runs with any Ollama-supported model (e.g., `mistral`, `llama3.1`, `qwen2:7b`, `phi3:mini`)
- Simple HTML + JavaScript frontend served from Flask
- JSON-based `/ask` endpoint for easy integration with other tools
- Adjustable performance settings (`num_ctx`, `num_threads`, `timeout`)

## Requirements
- macOS / Linux (tested on macOS M2 Pro)
- [Ollama](https://ollama.com/download) installed and running
- Python 3.11+
- pip packages:
  ```bash
  pip install flask requests

##Quick Start
Install and run Ollama
  2.  Clone the Repo 
  3.  Run Flask
  4.  Open in Browser

Work in Progress

This is an early work-in-progress (WIP). Planned improvements:
	•	Frontend styling and better UX
	•	More flexible backend prompt templates
	•	Optional remote API support (OpenAI, Anthropic, etc.)
	•	Docker containerization

License

MIT License

Copyright (c) 2025 Siddharth Manguluru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
THE USE OR OTHER DEALINGS IN THE SOFTWARE.
