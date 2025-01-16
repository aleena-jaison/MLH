Check out my 'peda paad' for completing those not-too-easyy challenges for MLH's Beginner's Week 

## 1. RANDOM NUMBER GENERATOR
File- random.c
This C program implements a custom random number generator using a Linear Congruential Generator (LCG) algorithm. The program generates and prints 10 random numbers within a specified range (0 to 100).
### How it works 
1.  Linear Congruential Generator: The random number generator is based on the Linear Congruential Generator algorithm, a simple and well-known method for generating pseudo-random numbers.
2.  Range Calculation: The my_random_range function calculates the random number by adjusting the result from my_random() within the specified range [min, max].
3.  Modulo Operation: The formula uses the modulo operator % to ensure the result stays within the bounds of the modulus m.
4.  main() function: In main(), the code generates 10 random numbers in the range 0 to 100 and prints them to the console.


## 2. HACK WITH GEMINI- Personalized Story Generator
This project is a simple web application that uses the Gemini API to generate personalized short stories based on user-provided prompts. Users can specify a character, setting, and goal, and the application will create a unique story based on these inputs.
### Features
*   Generates creative short stories based on user input.
*   Simple and intuitive user interface.
*   Demonstrates the power of Gemini's natural language generation capabilities.
### Technologies Used- Python, Gemini API
### Setup and Installation
1.  Clone the repo.
2.  Install dependencies- pip install requests python-dotenv
3.  Obtain a Gemini API key.
4.  Set up environment variables- Create a `.env` file in the same directory as the Python script. Add your Gemini API key to the `.env` file:
    ```
    GEMINI_API_KEY=YOUR_ACTUAL_API_KEY
    ```
5.  Run the application (story_generator.py). 
### How it works
1.  Enter a character, setting, and goal in the input fields.
2.  Click the "Generate Story" button.
3.  The generated story will be displayed on the page.


## 3. A USELESS HACK- Infinite Loading Simulator
File- useless.py
This is a basic Infinite Loading Simulator built using Python's tkinter library. The application simulates a loading screen with a progress bar and a "loading" message that updates with ellipses (.) to indicate ongoing progress.
### Features
*  An indeterminate progress bar that simulates loading.
*  A dynamic "Still Loading" message that updates with ellipses (.) to show that the program is still running.
*  Built using the Python tkinter library for the graphical user interface (GUI).


## 4. USING LIBRARIES- Interactive Drawing Canvas
This is an interactive drawing application built using p5.js, where users can draw on a canvas with different colors and brush sizes. The app allows for simple interactions through key presses and mouse movements, making it an engaging tool for creative exploration.
### Features
*  Color Selection: Change the drawing color using the keyboard:
-  R or r: Red
-  G or g: Green
-  B or b: Blue
*  Brush Size Adjustment:
-  Use the Up Arrow to increase the brush size.
-  Use the Down Arrow to decrease the brush size (minimum size is 1).
*  Clear Canvas: Press C or c to clear the canvas and start drawing from scratch.
### Setup
1.  Clone or download the repository to your local machine.
2.  Open the HTML file (canvas.html) in your browser to start using the app.
### Technologies Used- html, p5.js, js
### How it Works
1.  The canvas is created with dimensions of 900x600 pixels and a default background color of light gray.
2.  You can interact with the canvas by pressing certain keys to change the color, modify the brush size, or clear the canvas.
3.  When the mouse is pressed, it draws a line from the previous mouse position (pmouseX, pmouseY) to the current mouse position (mouseX, mouseY), allowing you to draw freely.


## 5. USE AN API- Weather Application
File- weather.py
The Weather App fetches weather data from the OpenWeather API for a given city and displays it to the user. The app provides the current weather description and the temperature in Celsius. It handles API requests, error checking, and provides a user-friendly output.
### Features
*  Fetch Weather Data: Get the current weather information for any city.
*  Temperature in Celsius: Displays temperature in metric units (Celsius).
*  Error Handling: Displays appropriate error messages if there are issues with the city name, API response, or connectivity.
### Setup
1.  Clone the repo.
2.  Install dependencies- pip install requests 
3.  Obtain a API key from OpenWeather.
4.  Add API key to "your_api_key_here" 
5.  Run the application.
### How it works
When prompted, enter the name of the city for which you want to check the weather. The app will return weather description (e.g., clear sky, cloudy, etc.) and temperature in Celsius.


## 6. HELLO WORLD PROGRAM
File- hello.py
This is a simple Python program that prints "Hello, World!" to the console. 


## 7. ROCK PAPER SCISSORS GAME
File- rockpaperscissors.py
This is a simple Rock Paper Scissors game implemented in Python. The game allows the user to play against the computer. The player selects one of the three choices—rock, paper, or scissors—and the computer makes a random selection. The game is played for a specified number of rounds, and the final scores are displayed at the end.
### Features
*  Player vs. Computer: The player competes against the computer.
*  Game Choices: The player can choose from "rock", "paper", or "scissors".
*  Round Scoring: Each round, the winner is determined based on the game rules:
1.  Rock beats Scissors.
2.  Scissors beats Paper.
3.  Paper beats Rock.
*  Multiple Rounds: The number of rounds is configurable.
*  Real-time Score Tracking: Displays the current score after each round.
*  Final Result: Displays the winner after all rounds are completed.
### Game Instructions:
1.  You will be prompted to input the number of rounds you want to play.
2.  After each round, you will enter your choice of "rock", "paper", or "scissors".
3.  The program will display the computer's choice and determine the winner of the round.
4.  After all rounds are completed, the program will display the final scores and announce the winner.


## 8. SORTING PROGRAM
This C program implements the Bubble Sort algorithm, which is a simple comparison-based sorting algorithm. It sorts an array of integers in ascending order. The program first takes an array from the user, prints the array before and after sorting, and sorts it using the Bubble Sort technique.
### Features
*  Bubble Sort: The program uses the Bubble Sort algorithm to arrange the elements of the array in ascending order.
*  User Input: The user is prompted to input the size of the array and the array elements.
*  Before and After Sorting: The program displays the array before and after sorting.
