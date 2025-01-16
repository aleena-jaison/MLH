import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_ENDPOINT = "YOUR_GEMINI_API_ENDPOINT"  # Replace with the correct endpoint

def generate_story(character, setting, goal):
    if not all([character, setting, goal]):
        return "Please fill in all fields."

    try:
        prompt = f"Write a short story about a {character} who lives in a {setting} and wants to {goal}. Make it engaging and creative."
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt
        }
        response = requests.post(GEMINI_API_ENDPOINT, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        story_data = response.json()

        if "choices" in story_data and len(story_data["choices"]) > 0 and "text" in story_data["choices"][0]:
            return story_data["choices"][0]["text"].strip()
        else:
            print(f"Unexpected API Response: {story_data}")
            return "Error: Unexpected API response format."

    except requests.exceptions.RequestException as e:
        return f"Error communicating with Gemini API: {e}"
    except (KeyError, IndexError) as e:
        print(f"Error processing API Response: {story_data}")
        return f"Error processing API response: {e}. Check the API response format."

if __name__ == "__main__":
    character = input("Enter a character: ")
    setting = input("Enter a setting: ")
    goal = input("Enter a goal: ")

    story = generate_story(character, setting, goal)
    print("\nYour Story:\n")
    print(story)

    input("\nPress Enter to exit.") # Keep the console open
