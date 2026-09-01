# 🎮 Tic-Tac-Toe AI

A command-line Tic-Tac-Toe game built in Python with an AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning**.

The project demonstrates game-tree search, recursion, decision making, and basic modular software design.

## ✨ Features

- Human vs AI gameplay
- Minimax algorithm for optimal decisions
- Alpha-Beta pruning to eliminate unnecessary branches
- Easy, Medium, and Hard difficulty levels
- Automatic win and draw detection
- Input validation
- Replay support
- No external dependencies

## 🧠 AI Approach

The Hard difficulty uses **Minimax**.

The AI treats every possible future board position as a node in a game tree:

- AI moves try to **maximize** the score.
- Human moves try to **minimize** the score.
- A win for the AI receives a positive score.
- A win for the human receives a negative score.
- A draw receives zero.

### Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax by skipping branches that cannot affect the final decision.

This reduces the number of positions that need to be evaluated while producing the same optimal move.

## 🎯 Difficulty Levels

| Difficulty | Behavior |
|---|---|
| Easy | Random moves |
| Medium | Wins, blocks, and usually uses strategic moves |
| Hard | Unbeatable Minimax + Alpha-Beta pruning |

## 📁 Project Structure

```text
TIC-TAC-TOE/
├── main.py
├── game.py
├── ai.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `main.py`
Handles the user interface, game loop, difficulty selection, and replay.

### `game.py`
Contains the Tic-Tac-Toe board and game-state logic.

### `ai.py`
Contains the AI logic, including Minimax and Alpha-Beta pruning.

## ▶️ How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/vbalagopal10/TIC-TAC-TOE.git
cd TIC-TAC-TOE
```

Run:

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

## 🕹️ How to Play

The board positions are:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Choose `X` or `O`, select a difficulty, and enter the number corresponding to the square where you want to move.

## 📚 Concepts Demonstrated

- Recursion
- Backtracking
- Game-tree search
- Minimax
- Alpha-Beta pruning
- Time/space complexity
- Object-oriented programming
- Modular Python development

## 🚀 Future Improvements

Possible extensions include:

- Graphical interface using Tkinter or Pygame
- Player statistics and score tracking
- Human vs human mode
- Adjustable AI strength
- Move-history visualization
- Web version using Flask

## 📄 License

This project is open source and available for learning and personal use.
