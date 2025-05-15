# 🏃‍♀️ Understanding RAG with Runner Metrics 🦘

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that enhances LLMs by:

1. **Retrieving** relevant information from a knowledge base
2. **Augmenting** the LLM's prompt with this retrieved information
3. **Generating** a response based on both the query and the retrieved context

---

## Why Use RAG?

- **Reduces hallucinations** by grounding responses in factual data
- **Enables use of private/proprietary data** not in the LLM's training
- **Provides up-to-date information** that may be newer than the LLM's training
- **Adds transparency** to where information comes from

---

## Today's Example: Runner & Animal Gait Analysis

We'll build a simple RAG system that:

- Stores data about elite runners and animals
- Answers questions about their gait metrics
- Compares humans and animals based on their running style

---

## The Data

### 5 Elite Runners:
- Eliud Kipchoge (marathon)
- Usain Bolt (sprinter)
- Mo Farah (distance)
- Allyson Felix (sprinter)
- Kenenisa Bekele (distance)

### 3 Animals:
- Cheetah
- Horse
- Kangaroo

### Metrics for each:
- Cadence (steps/min)
- Heel strike (low/medium/high/none)
- Vertical oscillation (cm)

---

## RAG Components

### 1. Knowledge Base
- Python dictionaries (simple for demo)
- No vector embeddings in this example

### 2. Retrieval System
- Keyword-based lookups
- Context formatting

### 3. LLM Integration
- OpenAI API (gpt-3.5-turbo)
- Prompt construction

---

## Code Walkthrough

### 1. Knowledge Base Structure
```python
runners_data = {
    "Eliud Kipchoge": {
        "type": "human",
        "cadence": 185,
        "heel_strike": "low",
        "vertical_oscillation": 6.2,
        "description": "Marathon world record holder"
    },
    # ...more runners and animals...
}
```

---

## Code Walkthrough (cont.)

### 2. Retrieval Function

```python
def retrieve_context(query):
    context = ""
    
    # Check if query is about humans vs animals
    if "human" in query.lower() and "animal" in query.lower():
        # Retrieve all human and animal data
        # ...
    
    # Check if query is about a specific runner/animal
    # ...
    
    return context
```

---

## Code Walkthrough (cont.)

### 3. LLM Query Function

```python
def query_llm(query):
    # Retrieve relevant context
    context = retrieve_context(query)
    
    # Create prompt with context
    prompt = f"""
    You are a sports biomechanics expert.
    Use ONLY the following information:
    
    {context}
    
    QUESTION: {query}
    """
    
    # Send to LLM and return response
    # ...
```

---

## Demo Time!

Let's see our RAG system in action:

1. Basic queries ("What is cadence?")
2. Entity queries ("Tell me about Usain Bolt")
3. Comparison queries ("Which animal is most similar to Kipchoge?")
4. Adding new entities

---

## Workshop Exercises

1. Try different queries
2. Add yourself as a runner
3. Add a new animal
4. Modify the retrieval function
5. Challenge the system

See `exercises.md` for details!

---

## Beyond This Simple Example

Real-world RAG systems often include:

- **Vector embeddings** for semantic search
- **Document chunking** for large knowledge bases
- **Metadata filtering** for more precise retrieval
- **Re-ranking** of retrieved documents
- **Result caching** for performance
- **Evaluation metrics** to measure accuracy

---

## Thank You!

Questions?

Resources:
- This code: [GitHub Repo](https://github.com/your-username/runner-gait-rag)
- LangChain RAG docs: [langchain.com/rag](https://python.langchain.com/docs/use_cases/question_answering/)
- LlamaIndex: [llamaindex.ai](https://www.llamaindex.ai/)
- "RAG: State of the Union" paper: [arxiv.org](https://arxiv.org/abs/2312.10997)