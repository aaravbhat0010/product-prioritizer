# Product Prioritizer

A local AI tool for product managers. Enter a product goal and customer feedback to get one issue to investigate, a supporting quote, a metric, and a question to answer before committing to a fix.

## Run locally

Install Python 3 and [Ollama](https://ollama.com/download). Start Ollama, then run these commands from the project folder on macOS:

```bash
ollama pull qwen3:4b-instruct
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. For the Terminal version, run `python prioritize.py`.

## Try it

Use **Improve signup completion** as the goal. Paste this sample feedback:

> The verification email never arrived. I want dark mode. I gave up because the password rules only appeared after I hit submit.

Try changing the goal to **Help users who are stuck waiting for a verification email** and compare the recommendation.

## How it works

Flask handles the browser form. Python sends the goal and feedback to Ollama on the same machine. Qwen3 generates a recommendation. Review the quote against the original feedback and use actual product data to validate the suggested priority.
