# Runner & Animal Gait RAG Workshop

A simple demonstration of Retrieval-Augmented Generation (RAG) using runner and animal gait metrics.

## 📋 Overview

This repository contains a simple implementation of a RAG system that:

1. Stores gait metrics (cadence, heel strike, vertical oscillation) for famous runners and animals
2. Allows users to query an LLM about these metrics
3. Demonstrates how RAG can reduce hallucinations by grounding LLM responses in factual data

Perfect for a 30-minute introduction to RAG systems!

## 🚀 Quick Start

1. Clone this repository:
   ```
   git clone https://github.com/your-username/runner-gait-rag.git
   cd runner-gait-rag
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```
   # On Linux/Mac
   export OPENAI_API_KEY="your-api-key"
   
   # On Windows
   set OPENAI_API_KEY=your-api-key
   ```

4. Run the example:
   ```
   python runner_rag.py
   ```

## 🤔 What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that enhances Large Language Models by:

1. **Retrieving** relevant information from a knowledge base
2. **Augmenting** the LLM's prompt with this retrieved information
3. **Generating** a response based on both the question and the retrieved context

This approach helps ground the LLM's responses in factual information, reducing hallucinations.

## 📊 Dataset

The repository includes data on:

- 5 elite human runners (Eliud Kipchoge, Usain Bolt, Mo Farah, Allyson Felix, Kenenisa Bekele)
- 3 animals (Cheetah, Horse, Kangaroo)

For each entity, we track:
- Cadence (steps per minute)
- Heel strike level (low, medium, high, none)
- Vertical oscillation (cm)

## 🧪 Workshop Exercises

See the `workshop/exercises.md` file for exercises to try during the workshop.

## 🔧 Extending the Project

Here are some ways to extend this simple RAG implementation:

1. Add vector embeddings for semantic search
2. Implement a web interface
3. Add your own running metrics to compare with professionals
4. Expand the dataset with more runners or animals
5. Add visualization of gait metrics

## 📝 License

MIT

## 🙏 Acknowledgements

- OpenAI for the GPT API
- All workshop participants for their interest in RAG systems!
