import os
import random
import google.generativeai as genai
from error_handler import handle_error

def generate_quote(system_prompt):
    try:
        # Configure the Gemini API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # Generate a quote using Gemini
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(system_prompt)
        
        return response.text.strip()

    except Exception as e:
        handle_error(e)
        # Fallback to random quote generation
        return generate_random_quote()

def generate_random_quote():
    templates = [
        "Success is not final, failure is not fatal: {action}.",
        "The only way to do great work is to {action}.",
        "Believe you can and you're {percentage} there.",
        "Your {noun} is limited only by your {noun}.",
        "The future belongs to those who {action} in the beauty of their dreams."
    ]
    
    actions = ["keep moving forward", "persevere", "never give up", "stay focused", "embrace change"]
    nouns = ["potential", "imagination", "determination", "ambition", "vision"]
    percentages = ["halfway", "almost", "nearly", "practically"]
    
    template = random.choice(templates)
    return template.format(
        action=random.choice(actions),
        noun=random.choice(nouns),
        percentage=random.choice(percentages)
    )