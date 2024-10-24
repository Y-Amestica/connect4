#Connect4 Game with AI
This is a Connect4 project developed in Python using the tkinter library for the graphical interface, with the option to play against an artificial intelligence (AI). The code is designed to be modular, making it easy to maintain and scale.

#Features
Classic Connect4 Game: The game follows the standard rules of Connect4.

#Game Modes:
Player vs Player: Two human players can compete.
Player vs AI: Play against an AI that makes decisions based on a simple minimax algorithm.
Graphical Interface: Intuitive graphical interface using tkinter.
Board Size Selection: The player can select different board sizes before starting.

#Project Structure
The project follows a modular structure and is divided into several files to enhance code scalability and readability.

bash
Copy code
/src
    ├── game.py          # Logic of the Connect4 game
    ├── gui.py           # Graphical interface with tkinter
    └── ai.py            # Implementation of the game's AI

README.md                # Project documentation

#Files
#game.py:
Contains the game logic, such as board creation, checking for winning moves, and managing turns.
#gui.py:
Handles the graphical interface, drawing the board, button interactions, and controlling game events.
#ai.py:
Implements a basic AI that uses the minimax algorithm to make moves during the game.
#Requirements
To run this project, you need to have Python 3 installed along with the following dependencies:

tkinter
numpy

#Instructions to Play

#Clone the repository:
bash
Copy code
git clone https://github.com/your-username/connect4.git

#Navigate to the project folder:
bash
Copy code
cd connect4

#Run the gui.py file:
bash
Copy code
python src/gui.py

Select the board size in the interface and start playing against another player or against the AI.
Customization
You can customize the board size by modifying the parameters in the selection interface or in the code in gui.py.

#Contribute
If you would like to contribute to this project, feel free to fork it, open an issue, or submit a pull request.

#License
This project is licensed under the MIT License.
