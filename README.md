# Workshop 2: Retrieval Basics

**Learn:** Stop LLM hallucinations by grounding responses in retrieved data

## Quick Start
```bash
git clone https://github.com/12mv2/rag-workshop-2-retrieval-basics.git
cd rag-workshop-2-retrieval-basics
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python demo.py
```

When prompted, enter your OpenAI API key (or Gemini key).

## What You'll Do

| **Phase** | **Action** | **Outcome** | **Time** |
|-----------|------------|-------------|----------|
| **Setup** | Run commands above, enter API key | Demo starts with prompt | 3 min |
| **See It** | Ask: "Which animal runs like Usain Bolt?" | Gets Cheetah with explanation from data | 2 min |
| **Concept** | **Retrieve → Augment → Generate = No hallucination** | Grounding prevents making things up | 5 min |
| **Your Turn** | Try 3 queries: 1) "What is cadence?" 2) "Compare Kipchoge and Bolt" 3) "Who's fastest?" | See retrieval patterns | 10 min |
| **Learned** | RAG = LLM + your data = accurate answers | ✅ You get RAG | 2 min |

## The Core Insight

Without RAG, LLMs guess based on training data. **With RAG, they answer from YOUR facts**:

1. **Retrieve** relevant data (runner metrics)
2. **Augment** the prompt with that context
3. **Generate** response grounded in facts

You'll see the retrieved context printed before each answer—transparency is key!

## The 3-Step RAG Pipeline

```python
def query_llm(question):
    context = retrieve_context(question)  # 1. Retrieve
    prompt = f"Use this data: {context}\n\nQuestion: {question}"  # 2. Augment
    return llm.generate(prompt)  # 3. Generate
```

<details>
<summary><strong>📚 Understanding the Data</strong></summary>

**8 entities with 3 gait metrics each:**

| Name | Type | Cadence | Heel Strike | Vert. Osc |
|------|------|---------|-------------|-----------|
| Eliud Kipchoge | Human | 185 | low | 6.2 |
| Usain Bolt | Human | 260 | medium | 4.8 |
| Mo Farah | Human | 180 | low | 7.0 |
| Cheetah | Animal | 210 | low | 12.5 |
| Kangaroo | Animal | 70 | none | 35.0 |
| ... | ... | ... | ... | ... |

**Retrieval Logic:**
- Keyword matching finds relevant entities
- Context includes definitions and comparisons
- LLM only sees what's retrieved (not its training data)

</details>

<details>
<summary><strong>🔧 Advanced: Using Gemini Instead of OpenAI</strong></summary>

Create `.env` with Gemini key:
```env
GEMINI_API_KEY=your-gemini-key-here
```

Then in `demo.py`, comment out OpenAI block and uncomment Gemini block (lines clearly marked).

</details>

<details>
<summary><strong>💡 Want to modify and save your changes?</strong></summary>

Fork it first:
1. Click "Fork" on GitHub
2. Clone YOUR fork: `git clone https://github.com/YOUR_USERNAME/rag-workshop-2-retrieval-basics.git`
3. Experiment freely

</details>

---

**Previous:** [Workshop 1 - Vector Fundamentals](https://github.com/12mv2/rag-workshop-1-vector-fundamentals)  
**Next:** [Workshop 3 - Production Pipeline](https://github.com/12mv2/rag-workshops-part3-production)

---

**Questions?** [GitHub Discussions](https://github.com/12mv2/rag-workshop-2-retrieval-basics/discussions)
