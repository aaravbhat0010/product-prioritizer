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

## Glossary

| Term | In plain English |
| --- | --- |
| **Ollama** | The software that downloads and runs AI models on your Mac. |
| **Qwen3 4B Instruct** | The model that writes the answer. Alibaba trained it before you downloaded it. `4B` means about four billion learned values, and `Instruct` means it was tuned to follow directions. |
| **Weights and quantization** | Weights are those learned values. Quantization stores them with fewer bits so the model takes up less space and memory. |
| **Prompt and context** | The prompt is the message you send Qwen. The goal and customer comments are context that helps it answer your specific question. |
| **Inference** | Running an already trained model to get an answer. Each click runs inference using the goal and feedback you entered. |
| **API, `curl`, and JSON** | The API is how programs talk to Ollama. `curl` let you try that connection by hand. JSON is the format used to send the prompt and receive the answer. |
| **Python, Flask, and `.venv`** | Python runs your app logic. Flask connects that logic to the browser page. `.venv` gives the project its own place to install packages like Flask. |
| **`localhost`** | An address for your own computer. Your browser page and Ollama both run on your Mac. |
