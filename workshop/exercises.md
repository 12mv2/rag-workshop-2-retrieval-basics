# Exercises for the RAG Workshop

Here are some exercises to try during the workshop to better understand how RAG works and to customize the system.

## 📊 Basic Queries

First, try these basic queries to understand how the system works:

1. "What is cadence?"
2. "Tell me about Usain Bolt's running metrics"
3. "Which animal has the highest vertical oscillation?"
4. "Compare the heel strike patterns of humans and animals"
5. "Which runner has a cadence most similar to a cheetah?"

## 🔍 Understanding the Retrieval System

These exercises help you understand how the retrieval system works:

1. Open the `runner_rag.py` file and look at the `retrieve_context()` function
2. Modify a query slightly and observe how the retrieved context changes
3. Add a print statement to show the prompt sent to the LLM

## 🧩 Customizing the System

Try these exercises to customize the system:

1. **Add yourself as a runner:**
   - Use the 'add' command to add your own running metrics
   - Compare yourself to the elite runners

2. **Add a new animal:**
   - Add another animal like a "Greyhound" or "Ostrich" with realistic metrics
   - Query the system to compare the new animal with existing runners

3. **Modify the retrieval function:**
   - Open `runner_rag.py` and find the `retrieve_context()` function
   - Add support for a new type of query, such as "Who has the most efficient running form?"
   - Hint: You'll need to define what "efficient" means in terms of the available metrics

## 🧠 Challenging the System

These exercises test the limits of the simple RAG system:

1. **Ask a question the system can't answer:**
   - "What is Usain Bolt's marathon time?"
   - Notice how the system handles missing information

2. **Try a vague query:**
   - "Who is the best runner?"
   - See how the system handles subjective questions

3. **Ask a question that requires calculation:**
   - "What is the average cadence of all human runners?"
   - See if the LLM can perform calculations based on the retrieved data

## 🚀 Extensions (If Time Permits)

If you finish early, try one of these extension exercises:

1. **Modify the code to calculate average metrics for humans vs animals**
   - Add a new command like 'stats' to display these averages

2. **Add a new metric to all runners and animals**
   - E.g., "stride length" or "ground contact time"
   - Update the retrieval function to support queries about this metric

3. **Create a simple scoring system**
   - Add a function that scores running efficiency based on the metrics
   - Allow queries like "Who has the most efficient running form?"