import os
import json
import openai
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# Set up OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("⚠️ OPENAI_API_KEY not found. Please set it as an environment variable or in a .env file.")
    print("You can continue with the workshop, but the LLM queries will not work.")

# 1. Store runner and animal data in dictionaries
runners_data = {
    # Famous Professional Runners
    "Eliud Kipchoge": {
        "type": "human",
        "cadence": 185, 
        "heel_strike": "low", 
        "vertical_oscillation": 6.2,
        "description": "Marathon world record holder"
    },
    "Usain Bolt": {
        "type": "human",
        "cadence": 260, 
        "heel_strike": "medium", 
        "vertical_oscillation": 4.8,
        "description": "Sprinting legend, 100m and 200m world record holder"
    },
    "Mo Farah": {
        "type": "human",
        "cadence": 180, 
        "heel_strike": "low", 
        "vertical_oscillation": 7.0,
        "description": "Multiple Olympic gold medalist in 5000m and 10000m"
    },
    "Allyson Felix": {
        "type": "human",
        "cadence": 215, 
        "heel_strike": "low", 
        "vertical_oscillation": 5.5,
        "description": "Most decorated female track athlete in Olympic history"
    },
    "Kenenisa Bekele": {
        "type": "human",
        "cadence": 190, 
        "heel_strike": "low", 
        "vertical_oscillation": 6.8,
        "description": "Former 5000m and 10000m world record holder"
    },
    
    # Animals
    "Cheetah": {
        "type": "animal",
        "cadence": 210, 
        "heel_strike": "low", 
        "vertical_oscillation": 12.5,
        "description": "Fastest land animal with a top speed of 70-75 mph"
    },
    "Horse": {
        "type": "animal",
        "cadence": 150, 
        "heel_strike": "high", 
        "vertical_oscillation": 10.2,
        "description": "Domesticated mammal used for racing and transportation"
    },
    "Kangaroo": {
        "type": "animal",
        "cadence": 70, 
        "heel_strike": "none", 
        "vertical_oscillation": 35.0,
        "description": "Marsupial that moves by hopping with extremely efficient energy return"
    }
}

# 2. Store definitions in a dictionary
definitions = {
    "cadence": "Cadence refers to the number of steps taken per minute. For humans, optimal running cadence is typically around 170-180 steps per minute, with elite sprinters reaching over 200. Animals can have vastly different cadences based on their physiology.",
    
    "heel_strike": "Heel strike describes how the foot/paw contacts the ground. 'Low' indicates a forefoot or midfoot landing with minimal heel contact, 'medium' indicates a moderate heel-to-toe transition, 'high' means a pronounced heel-first landing, and 'none' means the heel never contacts the ground (as in some animals).",
    
    "vertical_oscillation": "Vertical oscillation measures the amount of up-and-down movement during running, measured in centimeters. For human runners, lower values (5-8 cm) generally indicate more efficient running form. Animals have widely varying vertical oscillation based on their gait type."
}

# 3. Retrieval function
def retrieve_context(query):
    """Retrieval function that returns relevant information based on the query"""
    context = ""
    
    # Check if query is about humans vs animals
    if ("human" in query.lower() and "animal" in query.lower()) or ("compare" in query.lower() and ("human" in query.lower() or "animal" in query.lower())):
        context += "Humans vs Animals Comparison:\n\n"
        humans = {name: data for name, data in runners_data.items() if data["type"] == "human"}
        animals = {name: data for name, data in runners_data.items() if data["type"] == "animal"}
        
        context += "Human runners:\n"
        for name, data in humans.items():
            context += f"- {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vertical_oscillation={data['vertical_oscillation']}\n"
        
        context += "\nAnimals:\n"
        for name, data in animals.items():
            context += f"- {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vertical_oscillation={data['vertical_oscillation']}\n"
    
    # Check if query is about similarity between humans and animals
    elif "similar" in query.lower() and ("human" in query.lower() or "animal" in query.lower()):
        context += "All runners and animals data for similarity comparison:\n\n"
        for name, data in runners_data.items():
            type_str = "Human runner" if data["type"] == "human" else "Animal"
            context += f"{type_str} - {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vertical_oscillation={data['vertical_oscillation']}\n"
    
    # Check if query is about a specific runner or animal
    else:
        found_entity = False
        for name, data in runners_data.items():
            if name.lower() in query.lower():
                entity_type = "runner" if data["type"] == "human" else "animal"
                context += f"Data for {name} ({entity_type}):\n"
                context += f"- Description: {data['description']}\n"
                context += f"- Cadence: {data['cadence']} steps/minute\n"
                context += f"- Heel strike: {data['heel_strike']}\n"
                context += f"- Vertical oscillation: {data['vertical_oscillation']} cm\n\n"
                found_entity = True
        
        # Check if query is about a specific metric
        for metric in ["cadence", "heel_strike", "vertical_oscillation"]:
            if metric in query.lower():
                context += f"Definition of {metric}: {definitions[metric]}\n\n"
                context += f"All {metric} data:\n"
                for name, data in runners_data.items():
                    entity_type = "Human" if data["type"] == "human" else "Animal"
                    context += f"- {entity_type} - {name}: {data[metric]}\n"
                found_entity = True
        
        # If nothing specific was found, include all data
        if not found_entity:
            humans = {name: data for name, data in runners_data.items() if data["type"] == "human"}
            animals = {name: data for name, data in runners_data.items() if data["type"] == "animal"}
            
            context += "Human runners:\n"
            for name, data in humans.items():
                context += f"- {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vertical_oscillation={data['vertical_oscillation']}\n"
            
            context += "\nAnimals:\n"
            for name, data in animals.items():
                context += f"- {name}: cadence={data['cadence']}, heel_strike={data['heel_strike']}, vertical_oscillation={data['vertical_oscillation']}\n"
            
            context += "\nMetric definitions:\n"
            for metric, definition in definitions.items():
                context += f"- {metric}: {definition}\n"
    
    return context

# 4. Function to query the LLM with the retrieved context
def query_llm(query):
    """Query the LLM with the retrieved context"""
    if not openai.api_key:
        return "⚠️ OpenAI API key not set. Please set OPENAI_API_KEY environment variable."
    
    # Retrieve relevant context
    context = retrieve_context(query)
    
    # Print the retrieved context (for educational purposes in the workshop)
    print("\n📚 Retrieved Context:")
    print("-" * 40)
    print(context)
    print("-" * 40)
    
    # Prepare the prompt with context and query
    prompt = f"""
    You are a sports biomechanics expert that analyzes running gaits of both humans and animals. 
    Use ONLY the following information to answer the question. If the information doesn't contain
    the answer, say "I don't have enough information to answer that."
    
    INFORMATION:
    {context}
    
    QUESTION: {query}
    
    ANSWER:
    """
    
    # Call the API - using ChatGPT (gpt-3.5-turbo)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful sports biomechanics expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

# 5. Functions to save and load data
def ensure_data_dir():
    """Ensure the data directory exists"""
    if not os.path.exists("data"):
        os.makedirs("data")

def save_data_to_json():
    """Save the current data to JSON files"""
    ensure_data_dir()
    
    with open("data/runners_data.json", "w") as f:
        json.dump(runners_data, f, indent=2)
    
    with open("data/definitions.json", "w") as f:
        json.dump(definitions, f, indent=2)
    
    print("✅ Data saved to JSON files in the data/ directory")

def load_data_from_json():
    """Load data from JSON files"""
    global runners_data, definitions
    
    try:
        with open("data/runners_data.json", "r") as f:
            runners_data = json.load(f)
        
        with open("data/definitions.json", "r") as f:
            definitions = json.load(f)
        
        print("✅ Data loaded from JSON files")
    except FileNotFoundError:
        print("⚠️ JSON files not found. Using default data.")

# 6. Function to add a new runner or animal
def add_entity():
    """Add a new runner or animal to the database"""
    print("\n➕ Add New Runner or Animal")
    print("-" * 40)
    
    name = input("Name: ")
    
    # Check if name already exists
    if name in runners_data:
        print(f"⚠️ {name} already exists in the database.")
        return
    
    # Get entity type
    entity_type = ""
    while entity_type not in ["human", "animal"]:
        entity_type = input("Type (human/animal): ").lower()
        if entity_type not in ["human", "animal"]:
            print("Please enter either 'human' or 'animal'.")
    
    # Get description
    description = input("Description: ")
    
    # Get metrics
    try:
        cadence = int(input("Cadence (steps/minute): "))
        
        heel_strike = ""
        while heel_strike not in ["low", "medium", "high", "none"]:
            heel_strike = input("Heel strike (low/medium/high/none): ").lower()
            if heel_strike not in ["low", "medium", "high", "none"]:
                print("Please enter one of: low, medium, high, none.")
        
        vertical_oscillation = float(input("Vertical oscillation (cm): "))
    except ValueError:
        print("⚠️ Invalid input. Entity not added.")
        return
    
    # Add to database
    runners_data[name] = {
        "type": entity_type,
        "cadence": cadence,
        "heel_strike": heel_strike,
        "vertical_oscillation": vertical_oscillation,
        "description": description
    }
    
    print(f"✅ {name} added to the database.")

# Example usage with a simple CLI
if __name__ == "__main__":
    print("=" * 60)
    print("🏃‍♀️ Runner & Animal Gait Analysis RAG System 🦘")
    print("=" * 60)
    print("\nThis system compares gait metrics of famous runners and animals.")
    print("\nAvailable commands:")
    print("  - Just type a question to query the system")
    print("  - 'runners': List all runners and animals")
    print("  - 'add': Add a new runner or animal")
    print("  - 'save': Save current data to JSON files")
    print("  - 'load': Load data from JSON files")
    print("  - 'help': Show this help message")
    print("  - 'quit': Exit the program")
    print("\nExample questions:")
    print("  - Which animal has a running gait most similar to Usain Bolt?")
    print("  - Compare human and animal vertical oscillation")
    print("  - Which runner has the highest cadence?")
    
    # Initialize by saving default data
    ensure_data_dir()
    if not os.path.exists("data/runners_data.json"):
        save_data_to_json()
    
    while True:
        user_query = input("\n🔍 Your question or command: ")
        
        if user_query.lower() == 'quit':
            print("Thank you for using the Gait Analysis RAG System!")
            break
        elif user_query.lower() == 'help':
            print("\nAvailable commands:")
            print("  - Just type a question to query the system")
            print("  - 'runners': List all runners and animals")
            print("  - 'add': Add a new runner or animal")
            print("  - 'save': Save current data to JSON files")
            print("  - 'load': Load data from JSON files")
            print("  - 'help': Show this help message")
            print("  - 'quit': Exit the program")
        elif user_query.lower() == 'runners':
            print("\n👤 Human Runners:")
            for name, data in {k: v for k, v in runners_data.items() if v["type"] == "human"}.items():
                print(f"  - {name} ({data['description']})")
            print("\n🐾 Animals:")
            for name, data in {k: v for k, v in runners_data.items() if v["type"] == "animal"}.items():
                print(f"  - {name} ({data['description']})")
        elif user_query.lower() == 'save':
            save_data_to_json()
        elif user_query.lower() == 'load':
            load_data_from_json()
        elif user_query.lower() == 'add':
            add_entity()
        else:
            print("\n⏳ Retrieving information and generating response...")
            start_time = datetime.now()
            answer = query_llm(user_query)
            end_time = datetime.now()
            print(f"\n🤖 Answer (generated in {(end_time-start_time).total_seconds():.2f}s):")
            print("=" * 60)
            print(answer)
            print("=" * 60)