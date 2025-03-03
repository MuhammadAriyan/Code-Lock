# 🎮 DAY 2 | Tic-Tac-Toe AI (Pygame)

## 📌 Overview
This is a **Tic-Tac-Toe** game built using **Python** and **Pygame**, featuring an AI opponent powered by a simple decision-making algorithm. The game supports two-player mode and AI mode, where the computer makes smart moves to challenge the player.

## 🚀 Features
✅ Two-player local mode (X and O)  
✅ AI opponent with decision-making logic  
✅ Automatic winner detection with an on-screen message  
✅ Simple and clean UI with smooth drawing  
✅ Automatic game restart after showing results  

## 🎮 How to Play
1. **Run the script**: Start the game by running the Python file.
2. **Click on a square**: The first player (X) makes a move, followed by the second player (O) or AI.
3. **Win the game**: The first player to get three marks in a row, column, or diagonal wins!
4. **Game restarts automatically** after displaying the winner for 3 seconds.

## 🛠️ Installation
### **1. Install Python**
Make sure you have Python **3.x** installed. You can download it from: [Python.org](https://www.python.org/downloads/)

### **2. Install Pygame**
Run the following command to install Pygame:
```sh
pip install pygame
```

### **3. Run the Game**
Navigate to the project folder and run:
```sh
python app.py
```

## 🏗️ Code Structure
- **`draw_grid()`** → Draws the Tic-Tac-Toe grid.
- **`mark_cell(row, col, player)`** → Marks a square for the player.
- **`draw_shapes()`** → Draws X and O symbols.
- **`check_winner()`** → Checks for a winner.
- **`display_winner(winner)`** → Displays the winner.
- **`win_move(board)`** → AI move logic (currently basic, will be upgraded with Minimax).
- **`reset_board()`** → Clears the board and restarts the game.

## 📝 License
This project is open-source and free to use! Feel free to contribute and improve it. 🚀

