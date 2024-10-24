<h1 style="color: #333;">Connect4 Game with AI</h1>

<p style="font-size: 16px; line-height: 1.5;">
    This is a Connect4 project developed in Python using the tkinter library for the graphical interface, with the option to play against an artificial intelligence (AI). The code is designed to be modular, making it easy to maintain and scale.
</p>

<h2 style="color: #444;">Features</h2>
<ul style="font-size: 16px; line-height: 1.5;">
    <li><strong>Classic Connect4 Game:</strong> The game follows the standard rules of Connect4.</li>
    <li><strong>Game Modes:</strong>
        <ul>
            <li><strong>Player vs Player:</strong> Two human players can compete.</li>
            <li><strong>Player vs AI:</strong> Play against an AI that makes decisions based on a simple minimax algorithm.</li>
        </ul>
    </li>
    <li><strong>Graphical Interface:</strong> Intuitive graphical interface using tkinter.</li>
    <li><strong>Board Size Selection:</strong> The player can select different board sizes before starting.</li>
</ul>

<h2 style="color: #444;">Project Structure</h2>
<pre style="background-color: #f4f4f4; padding: 10px;">
/src
    ├── game.py          # Logic of the Connect4 game
    ├── gui.py           # Graphical interface with tkinter
    └── ai.py            # Implementation of the game's AI

README.md                # Project documentation
</pre>

<h2 style="color: #444;">Files</h2>
<ul style="font-size: 16px; line-height: 1.5;">
    <li><strong>game.py:</strong> Contains the game logic, such as board creation, checking for winning moves, and managing turns.</li>
    <li><strong>gui.py:</strong> Handles the graphical interface, drawing the board, button interactions, and controlling game events.</li>
    <li><strong>ai.py:</strong> Implements a basic AI that uses the minimax algorithm to make moves during the game.</li>
</ul>

<h2 style="color: #444;">Requirements</h2>
<p style="font-size: 16px; line-height: 1.5;">
    To run this project, you need to have Python 3 installed along with the following dependencies:
</p>
<ul style="font-size: 16px; line-height: 1.5;">
    <li>tkinter</li>
    <li>numpy</li>
</ul>

<h2 style="color: #444;">Instructions to Play</h2>
<ol style="font-size: 16px; line-height: 1.5;">
    <li>Clone the repository:
        <pre><code>git clone https://github.com/your-username/connect4.git</code></pre>
    </li>
    <li>Navigate to the project folder:
        <pre><code>cd connect4</code></pre>
    </li>
    <li>Run the <code>gui.py</code> file:
        <pre><code>python src/gui.py</code></pre>
    </li>
    <li>Select the board size in the interface and start playing against another player or against the AI.</li>
</ol>

<h2 style="color: #444;">Customization</h2>
<p style="font-size: 16px; line-height: 1.5;">
    You can customize the board size by modifying the parameters in the selection interface or in the code in <code>gui.py</code>.
</p>

<h2 style="color: #444;">Contribute</h2>
<p style="font-size: 16px; line-height: 1.5;">
    If you would like to contribute to this project, feel free to fork it, open an issue, or submit a pull request.
</p>

<h2 style="color: #444;">License</h2>
<p style="font-size: 16px; line-height: 1.5;">
    This project is licensed under the MIT License.
</p>
