## 📝 License

MIT

## 🙏 Acknowledgements

- OpenAI for the GPT API
- All workshop participants for their interest in RAG systems!# Runner & Animal Gait RAG Workshop

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
   git clone https://github.com/your-username/30min-rag-db.git
   cd 30min-rag-db
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install the specific version
   pip install openai==0.28.1 python-dotenv==1.1.0
   ```

3. Set up your OpenAI API key in a .env file:
   ```bash
   # Create a .env file in the project root directory
   # On Windows:
   echo OPENAI_API_KEY=your-api-key-here > .env
   
   # On macOS/Linux:
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```
   
   > **Note:** Replace `your-api-key-here` with your actual OpenAI API key. You can get an API key from [OpenAI's website](https://platform.openai.com/api-keys).

4. Run the example:
   ```
   python runner_rag.py
   ```

## 📝 About .env Files

This project uses a `.env` file to securely store your API keys and other sensitive information:

- **What is a .env file?** It's a simple text file that stores key-value pairs in the format `KEY=value`
- **Why use it?** It keeps sensitive data (like API keys) out of your code and version control
- **How does it work?** The `python-dotenv` package loads these values into environment variables

### .env File Example
```
OPENAI_API_KEY=sk-abcdef123456789
# You can add other environment variables as needed
# ANOTHER_VARIABLE=another_value
```

### Important Security Notes
- **NEVER commit your .env file to version control**
- Add `.env` to your `.gitignore` file
- Each developer should create their own local `.env` file
- For the workshop, everyone will need their own OpenAI API key

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

## ❓ Troubleshooting

### Common Issues

1. **API Key Issues**
   - Error message about invalid API key: Double-check your API key in the .env file
   - "OpenAI API key not set": Ensure your .env file is in the correct location (project root)

2. **Python Environment Problems**
   - "Module not found": Make sure you've activated your virtual environment
   - Version conflicts: Ensure you're using exactly `openai==0.28.1`

3. **Running the Code**
   - Windows path issues: Use `\\` or raw strings (r"path\to\file") for file paths
   - Permission errors: Check that you have write access to the project directory

If you encounter other issues during the workshop, please raise your hand for assistance.

## 🔧 Extending the Project

Here are some ways to extend this simple RAG implementation:

1. Add vector embeddings for semantic search
2. Implement a web interface
3. Add your own running metrics to compare with professionals
4. Expand the dataset with more runners or animals
5. Add visualization of gait metrics
