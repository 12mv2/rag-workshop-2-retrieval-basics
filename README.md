# 🏃‍♀️ Runner & Animal Gait RAG Workshop 🪘

A simple demonstration of Retrieval-Augmented Generation (RAG) using runner and animal gait metrics.

## 📝 License

MIT

## 😝 Acknowledgements

* OpenAI for the GPT API
* Google for the Gemini API
* All workshop participants for their interest in RAG systems!

---

## 📋 Overview

This repository contains a simple implementation of a RAG system that:

1. Stores gait metrics (cadence, heel strike, vertical oscillation) for famous runners and animals
2. Allows users to query an LLM about these metrics
3. Demonstrates how RAG can reduce hallucinations by grounding LLM responses in factual data

Perfect for a 30-minute introduction to RAG systems!

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/30min-rag-db.git
cd 30min-rag-db
```

### 2. Create a virtual environment and install dependencies

```bash
# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Set up your API key in a `.env` file

This project supports both **OpenAI** and **Gemini** models.

Create a file called `.env` in the project root and add the relevant API key.

```env
# For OpenAI (default setup)
OPENAI_API_KEY=your-openai-api-key

# For Gemini (optional alternative)
# GEMINI_API_KEY=your-gemini-api-key
```

**Note:** `.env` files are hidden by default. If you don’t see it, check your file explorer settings.

---

### 4. Choose your model in `runner_rag.py`

In the script, you'll see two setup blocks:

* One for **OpenAI**
* One for **Gemini**

Uncomment **only one** of the two. Each block has comments explaining what to do.

Then run the app:

```bash
python runner_rag.py
```

---

## 📍 About `.env` Files

* `.env` files store sensitive credentials like API keys
* This project uses `python-dotenv` to load the keys into environment variables
* **Do not commit ****`.env`**** files to GitHub**

---

## 🤔 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that enhances Large Language Models by:

1. **Retrieving** relevant info from a knowledge base
2. **Augmenting** the LLM's prompt with that info
3. **Generating** a response grounded in facts

This helps reduce hallucinations and makes LLMs more accurate.

---

## 📊 Dataset

This RAG system includes:

* 5 elite human runners:

  * Eliud Kipchoge
  * Usain Bolt
  * Mo Farah
  * Allyson Felix
  * Kenenisa Bekele

* 3 animals:

  * Cheetah
  * Horse
  * Kangaroo

Each has:

* Cadence (steps per minute)
* Heel strike level (low, medium, high, none)
* Vertical oscillation (cm)

---

## 🧪 Workshop Exercises

Check the `workshop/exercises.md` file for suggested activities:

* Ask factual and comparative questions
* Add yourself as a runner
* Extend the retrieval function

---

## ❓ Troubleshooting

### API Key Problems

* Double-check the `.env` file exists in the project root
* Confirm your key is valid and uncommented
* Only one key should be used at a time

### Module Not Found?

* Run `pip install -r requirements.txt`
* Make sure you’re in your virtual environment

### Permission or path issues?

* Try running from your terminal as admin
* Use raw strings (`r"path\\to\\file"`) on Windows

---

## 🔧 Extending the Project

Some ideas if you want to take this further:

* Add vector embeddings for smarter retrieval
* Build a simple web UI
* Compare your own running data
* Add more runners or animals
* Visualize gait metrics

---

## 🙌 Thank You!

Happy hacking! 🏃‍♂️🧠
Questions? Just raise your hand in the workshop.
