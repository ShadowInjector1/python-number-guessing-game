# python-number-guessing-game
A Python-based number guessing game where players guess a randomly generated number between 1 and 100 with helpful hints and an attempt counter.

🎮 Python Number Guessing Game
📌 Project Overview

The Python Number Guessing Game is a beginner-friendly command-line game developed using Python.

In this game, the computer randomly selects a secret number between 1 and 100, and the player must guess the correct number.

The game provides helpful hints such as "Too High" or "Too Low" to guide the player toward the correct answer.

This project helps beginners understand Python fundamentals and improve their problem-solving skills.

✨ Features

🎲 Random number generation between 1 and 100.
⬆️ Too High hint when the guess is greater than the secret number.
⬇️ Too Low hint when the guess is smaller than the secret number.
🏆 Winning message when the correct number is guessed.
🔢 Tracks the total number of attempts.
🔄 Play Again option.
⚠️ Handles invalid user input.
🚫 Prevents guesses outside the 1–100 range.

🛠️ Technologies Used
Programming Language: Python 3
Modules: Random
Concepts Used:
Variables
Functions
While Loops
Conditional Statements (if-elif-else)
User Input
Exception Handling (try-except)
Random Number Generation

📥 Installation Instructions
Follow these steps to run the project on your local machine.

1. Clone the Repository

bash
git clone https://github.com/your-username/python-number-guessing-game.git
2. Navigate to the Project Directory

bash
cd python-number-guessing-game
3. Check Python Installation
Make sure Python 3 is installed.

bash
python --version

▶️ How to Run
Run the following command in your terminal:


bash
python guessing_game.py

💻 Example Output

text
===== NUMBER GUESSING GAME =====

Guess a number between 1 and 100!

Enter your guess: 50
Too Low! Try Again.

Enter your guess: 75
Too High! Try Again.

Enter your guess: 65

Congratulations! You Won!

Secret Number: 65
Total Attempts: 3

Play Again? (yes/no): no

Thanks for playing!

🔮 Future Improvements
The following features can be added in future versions:

Add different difficulty levels (Easy, Medium, Hard).
Introduce a maximum number of attempts.
Add a scoring system.
Implement a countdown timer.
Create a leaderboard to track high scores.
Develop a graphical user interface (GUI) using Tkinter.

⭐ Support
If you like this project, don't forget to give it a ⭐ on GitHub!

Made with ❤️ using Python
