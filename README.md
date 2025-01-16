Check out my 'peda paad' for completing those not-too-easyy challenges for MLH's Beginner's Week 

## RANDOM NUMBER GENERATOR
### How it works
1. Linear Congruential Generator: The random number generator is based on the Linear Congruential Generator algorithm, a simple and well-known method for generating pseudo-random numbers.
2. Range Calculation: The my_random_range function calculates the random number by adjusting the result from my_random() within the specified range [min, max].
3. Modulo Operation: The formula uses the modulo operator % to ensure the result stays within the bounds of the modulus m.
4. main() function: In main(), the code generates 10 random numbers in the range 0 to 100 and prints them to the console.
### Output example
Random number: 72
Random number: 58
Random number: 25
Random number: 40
Random number: 93
Random number: 17
Random number: 79
Random number: 45
Random number: 100
Random number: 61


## Hack with Gemini- Personalized Story Generator
This project is a simple web application that uses the Gemini API to generate personalized short stories based on user-provided prompts. Users can specify a character, setting, and goal, and the application will create a unique story based on these inputs.
### Features
*   Generates creative short stories based on user input.
*   Simple and intuitive user interface.
*   Demonstrates the power of Gemini's natural language generation capabilities.
### Technologies Used
*   Python
*   Gemini API
### Setup and Installation
1. Clone the repo.
2. Install dependencies- pip install requests python-dotenv
3. Obtain a Gemini API key.
4. Set up environment variables- Create a `.env` file in the same directory as the Python script. Add your Gemini API key to the `.env` file:
    ```
    GEMINI_API_KEY=YOUR_ACTUAL_API_KEY
    ```
5. Run the application.
### Obtain a Gemini API key
 *   Go to Google AI Studio.
 *   Sign in with your Google account.
 *   Find the Gemini API section.
 *   Get your API key.
### Usage
1.  Enter a character, setting, and goal in the input fields.
2.  Click the "Generate Story" button.
3.  The generated story will be displayed on the page.

