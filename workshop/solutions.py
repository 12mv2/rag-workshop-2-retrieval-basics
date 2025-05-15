"""
Example solutions to the workshop exercises.
These are more advanced features you can add to the basic RAG system.
"""

import os
import json
import statistics
import openai
from datetime import datetime

# 1. Calculate averages for humans vs animals
def calculate_stats():
    """Calculate and display average metrics for humans vs animals"""
    humans = {name: data for name, data in runners_data.items() if data["type"] == "human"}
    animals = {name: data for name, data in runners_data.items() if data["type"] == "animal"}
    
    # Calculate human averages
    human_cadence = [data["cadence"] for data in humans.values()]
    human_oscillation = [data["vertical_oscillation"] for data in humans.values()]
    
    # Calculate animal averages
    animal_cadence = [data["cadence"] for data in animals.values()]
    animal_oscillation = [data["vertical_oscillation"] for data in animals.values()]
    
    print("\n📊 Average Metrics")
    print("-" * 40)
    print("Humans:")
    print(f"  - Average cadence: {statistics.mean(human_cadence):.1f} steps/minute")
    print(f"  - Average vertical oscillation: {statistics.mean(human_oscillation):.1f} cm")
    print("\nAnimals:")
    print(f"  - Average cadence: {statistics.mean(animal_cadence):.1f} steps/minute")
    print(f"  - Average vertical oscillation: {statistics.mean(animal_oscillation):.1f} cm")

# 2. Add stride length as a new metric
def add_stride_length():
    """Add stride length as a new metric to all runners and animals"""
    # Typical stride lengths (in meters)
    stride_lengths = {
        "Eliud Kipchoge": 1.8,
        "Usain Bolt": 2.6,
        "Mo Farah": 1.7,
        "Allyson Felix": 2.2,
        "Kenenisa Bekele": 1.8,
        "Cheetah": 7.5,
        "Horse": 6.0,
        "Kangaroo": 9.0
    }
    
    # Add to each entity
    for name, length in stride_lengths.items():
        if name in runners_data:
            runners_data[name]["stride_length"] = length
    
    # Add to definitions
    definitions["stride_length"] = "Stride length is the distance covered in a single stride (two steps), measured in meters. Elite human runners typically have stride lengths between 1.5-2.6 meters, while animals can have much longer strides."
    
    print("✅ Added stride length metric to all runners and animals")
    
    # Update the retrieve_context function to handle stride length queries
    global retrieve_context
    original_retrieve_context = retrieve_context
    
    def new_retrieve_context(query):
        context = original_retrieve_context(query)
        
        # Add stride length information if the query asks about it
        if "stride" in query.lower() or "length" in query.lower():
            context += "\nStride length data:\n"
            for name, data in runners_data.items():
                if "stride_length" in data:
                    entity_type = "Human" if data["type"] == "human" else "Animal"
                    context += f"- {entity_type} - {name}: {data['stride_length']} meters\n"
            
            context += f"\nDefinition of stride length: {definitions.get('stride_length', 'No definition available')}\n"
        
        return context
    
    # Replace the original function with the new one
    retrieve_context = new_retrieve_context

# 3. Create an efficiency scoring system
def add_efficiency_score():
    """Add an efficiency score calculation based on the metrics"""
    # Calculate an efficiency score for each runner/animal
    # Lower vertical oscillation, optimal cadence, and low heel strike are more efficient
    
    for name, data in runners_data.items():
        # Base score - higher is better
        score = 100
        
        # Penalize high vertical oscillation
        if data["type"] == "human":
            # For humans, optimal VO is around 6 cm
            vo_penalty = abs(data["vertical_oscillation"] - 6) * 5
        else:
            # For animals, we scale based on their size/type
            # This is very simplified
            vo_penalty = max(0, data["vertical_oscillation"] - 15) * 2
        
        # Penalize non-optimal cadence for humans
        if data["type"] == "human":
            # For distance runners, optimal is around 180
            if "marathon" in data.get("description", "").lower() or "distance" in data.get("description", "").lower():
                cadence_penalty = abs(data["cadence"] - 180) * 0.5
            # For sprinters, higher cadence is better
            else:
                cadence_penalty = max(0, 250 - data["cadence"]) * 0.25
        else:
            # For animals, we don't penalize cadence
            cadence_penalty = 0
        
        # Penalize high heel strike for both
        heel_strike_penalty = 0
        if data["heel_strike"] == "high":
            heel_strike_penalty = 15
        elif data["heel_strike"] == "medium":
            heel_strike_penalty = 5
        
        # Calculate final score
        efficiency_score = max(0, score - vo_penalty - cadence_penalty - heel_strike_penalty)
        
        # Add to data
        runners_data[name]["efficiency_score"] = round(efficiency_score, 1)
    
    print("✅ Added efficiency scores to all runners and animals")
    
    # Add to definitions
    definitions["efficiency_score"] = "Efficiency score is a calculated metric (0-100) based on optimal biomechanics. It considers vertical oscillation, cadence, and heel strike pattern, with higher scores indicating more efficient running form."
    
    # Update the retrieve_context function
    global retrieve_context
    original_retrieve_context = retrieve_context
    
    def new_retrieve_context(query):
        context = original_retrieve_context(query)
        
        # Add efficiency information if the query asks about it
        if "efficien" in query.lower() or "score" in query.lower() or "best form" in query.lower():
            context += "\nEfficiency scores (higher is better):\n"
            
            # Sort by efficiency score
            sorted_entities = sorted(
                runners_data.items(), 
                key=lambda x: x[1].get("efficiency_score", 0), 
                reverse=True
            )
            
            for name, data in sorted_entities:
                if "efficiency_score" in data:
                    entity_type = "Human" if data["type"] == "human" else "Animal"
                    context += f"- {entity_type} - {name}: {data['efficiency_score']}/100\n"
            
            context += f"\nDefinition of efficiency score: {definitions.get('efficiency_score', 'No definition available')}\n"
        
        return context
    
    # Replace the original function with the new one
    retrieve_context = new_retrieve_context

# Implementation note: You would need to add these functions to the main CLI loop
# For example, add these options to the help menu and handle them in the main loop:
"""
elif user_query.lower() == 'stats':
    calculate_stats()
elif user_query.lower() == 'add_stride':
    add_stride_length()
elif user_query.lower() == 'add_efficiency':
    add_efficiency_score()
"""