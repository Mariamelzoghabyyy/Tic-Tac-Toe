# Tic-Tac-Toe
AI-powered Tic-Tac-Toe Game
This project implements a classic Tic-Tac-Toe game where users can play against an AI opponent powered by multiple search algorithms. The game is developed using Python, and the AI makes decisions using various strategies to ensure an optimal gameplay experience.

Features:

AI Opponent: The AI makes decisions using different search algorithms, including Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), and Iterative Deepening Search (IDS), providing diverse gameplay experiences.

User vs. AI Gameplay: Players can play against the AI in a turn-based system where the AI takes the role of one player and the user controls the other.

Interactive Console Interface: The game operates through a simple text-based interface in the console, where players make moves by entering their desired row and column.

Optimal Move Selection: The AI evaluates possible moves and selects the optimal one based on the current game state, ensuring competitive and challenging gameplay.

Algorithms:

DFS (Depth-First Search): Explores deeper game states first, making it useful for more exhaustive decision-making.

BFS (Breadth-First Search): Explores all possible moves level by level, providing a more level-headed approach to finding the best move.

UCS (Uniform Cost Search): Implements pathfinding strategies that prioritize fewer moves and minimal cost.

IDS (Iterative Deepening Search): Combines the benefits of BFS and DFS by gradually increasing the depth limit.

How to Play:

Clone the repository or download the code.

Run the tic_tac_toe.py file in your Python environment.

Play against the AI by entering your moves as row and column numbers (e.g., "1 1" for the top-left corner).

The AI will respond with its move, and the game will continue until there is a winner or a draw.


Future Improvements:

GUI Implementation: A graphical user interface for a more intuitive user experience.

Advanced AI: Implementing Minimax or Alpha-Beta Pruning for even more advanced AI decision-making.

Multiplayer Mode: Adding a two-player mode to play with a friend locally.
