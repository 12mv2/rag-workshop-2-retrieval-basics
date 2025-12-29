import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

### === MODEL SETUP SELECTION === ###
### Uncomment ONE of the blocks below to activate your model ###

# === OpenAI Setup === 
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("\n🔑 OpenAI API key not found.")
    print("You can either:")
    print("  1. Create a .env file with: OPENAI_API_KEY=your-key")
    print("  2. Enter it now (this session only)")
    key = input("\nEnter API key (or press Enter to skip): ").strip()
    if key:
        openai.api_key = key
    else:
        print("⚠️ Without an API key, the demo won't work.")
        exit(1)

# === GEMINI SETUP ===
# Uncomment the block below to use Gemini instead of OpenAI
# import google.generativeai as genai
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_API_KEY:
#     print("\n🔑 Gemini API key not found.")
#     print("You can either:")
#     print("  1. Create a .env file with: GEMINI_API_KEY=your-key")
#     print("  2. Enter it now (this session only)")
#     key = input("\nEnter API key (or press Enter to skip): ").strip()
#     if key:
#         GEMINI_API_KEY = key
#     else:
#         print("⚠️ Without an API key, the demo won't work.")
#         exit(1)
# genai.configure(api_key=GEMINI_API_KEY)

# Data: runners and animals with gait metrics
runners_data = {
    "Eliud Kipchoge": {"type": "human", "cadence": 185, "heel_strike": "low", "vertical_oscillation": 6.2, "description": "Marathon world record holder"},
    "Usain Bolt": {"type": "human", "cadence": 260, "heel_strike": "medium", "vertical_oscillation": 4.8, "description": "Sprinting legend, 100m and 200m world record holder"},
    "Mo Farah": {"type": "human", "cadence": 180, "heel_strike": "low", "vertical_oscillation": 7.0, "description": "Multiple Olympic gold medalist in 5000m and 10000m"},
    "Allyson Felix": {"type": "human", "cadence": 215, "heel_strike": "low", "vertical_oscillation": 5.5, "description": "Most decorated female track athlete in Olympic history"},
    "Kenenisa Bekele": {"type": "human", "cadence": 190, "heel_strike": "low", "vertical_oscillation": 6.8, "description": "Former 5000m and 10000m world record holder"},
    "Cheetah": {"type": "animal", "cadence": 210, "heel_strike": "low", "vertical_oscillation": 12.5, "description": "Fastest land animal with a top speed of 70-75 mph"},
    "Horse": {"type": "animal", "cadence": 150, "heel_strike": "high", "vertical_oscillation": 10.2, "description": "Domesticated mammal used for racing and transportation"},
    "Kangaroo": {"type": "animal", "cadence": 70, "heel_strike": "none", "vertical_oscillation": 35.0, "description": "Marsupial that moves by hopping with extremely efficient energy return"}
}

definitions = {
    "cadence": "Cadence refers to the number of steps taken per minute. For humans, optimal running cadence is typically around 170-180 steps per minute, with elite sprinters reaching over 200.",
    "heel_strike": "Heel strike describes how the foot/paw contacts the ground. 'Low' indicates forefoot or midfoot landing, 'medium' is heel-to-toe, 'high' is pronounced heel-first, 'none' means heel never contacts ground.",
    "vertical_oscillation": "Vertical oscillation measures up-and-down movement during running in centimeters. For human runners, lower values (5-8 cm) indicate more efficient form."
}

# Retrieval function: finds relevant context for the query
def retrieve_context(query):
    context = ""
    query_lower = query.lower()
    found_entity = False

    # Check for specific entities (supports partial name matching)
    query_words = set(query_lower.split())
    for name, data in runners_data.items():
        name_words = set(name.lower().split())
        if name.lower() in query_lower or query_words & name_words:
            entity_type = "runner" if data["type"] == "human" else "animal"
            context += f"{name} ({entity_type}): {data['description']}\n"
            context += f"  Cadence: {data['cadence']} steps/min | Heel strike: {data['heel_strike']} | Vertical osc: {data['vertical_oscillation']} cm\n\n"
            found_entity = True
    
    # Check for metric definitions (handles both "heel strike" and "heel_strike")
    query_normalized = query_lower.replace(" ", "_")
    for metric in ["cadence", "heel_strike", "vertical_oscillation"]:
        metric_spaced = metric.replace("_", " ")
        if metric in query_normalized or metric_spaced in query_lower:
            context += f"{metric.title()}: {definitions[metric]}\n\n"
            for name, data in runners_data.items():
                entity_type = "Human" if data["type"] == "human" else "Animal"
                context += f"  {entity_type} - {name}: {data[metric]}\n"
            found_entity = True
    
    # If nothing specific found, include all data
    if not found_entity:
        context += "Humans:\n"
        for name, data in runners_data.items():
            if data["type"] == "human":
                context += f"  {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vert_osc={data['vertical_oscillation']}\n"
        context += "\nAnimals:\n"
        for name, data in runners_data.items():
            if data["type"] == "animal":
                context += f"  {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vert_osc={data['vertical_oscillation']}\n"
    
    return context

# Query LLM with retrieved context (RAG pipeline)
def query_llm(query):
    context = retrieve_context(query)
    
    print("\n📚 Retrieved Context:")
    print("-" * 60)
    print(context)
    print("-" * 60)
    
    prompt = f"""You are a sports biomechanics expert. Use ONLY the following information to answer the question.
If the information doesn't contain the answer, say "I don't have enough information to answer that."

INFORMATION:
{context}

QUESTION: {query}"""
    
    try:
        # OpenAI (comment out if using Gemini)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful sports biomechanics expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
        
        # Gemini (uncomment to use instead of OpenAI)
        # model = genai.GenerativeModel("gemini-1.5-flash")
        # response = model.generate_content(prompt)
        # return response.text
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

# Simple REPL
if __name__ == "__main__":
    print("=" * 60)
    print("🏃‍♀️ Runner & Animal Gait Analysis RAG System")
    print("=" * 60)
    print("\nAsk questions about runner biomechanics!")
    print("Type 'quit' to exit\n")
    print("Example questions:")
    print("  - Which animal runs most like Usain Bolt?")
    print("  - What is cadence?")
    print("  - Compare Kipchoge and Bolt")
    
    while True:
        query = input("\n🔍 Your question: ").strip()
        
        if query.lower() == 'quit':
            print("Thanks for trying RAG!")
            break
        
        if not query:
            continue
            
        print("\n⏳ Retrieving and generating response...")
        answer = query_llm(query)
        print(f"\n🤖 Answer:")
        print("=" * 60)
        print(answer)
        print("=" * 60)
