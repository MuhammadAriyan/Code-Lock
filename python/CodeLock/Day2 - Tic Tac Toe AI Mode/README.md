# DAY 1  |  Tic-Tac-Toe Game (Pygame)

## 📌 Overview
This is a simple **Tic-Tac-Toe** game built using **Python** and **Pygame**. Players take turns marking spaces on a 3×3 grid until one player gets three marks in a row, column, or diagonal.

## 🎮 How to Play
1. **Run the script**: Start the game by running the Python file.
2. **Click on a square**: The first player (X) makes a move, followed by the second player (O).
3. **Win the game**: The first player to get three marks in a row, column, or diagonal wins!
4. **Game restarts automatically** after displaying the winner for 2 seconds.

## ⚙️ Features
✅ Two-player local game mode (X and O)  
✅ Winner detection with an on-screen message 
✅ Simple and clean UI with smooth drawing  

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

## 📜 Code Structure
- **`draw_lines()`** → Draws the Tic-Tac-Toe grid lines.
- **`mark_square(row, col, player)`** → Marks a square for the player.
- **`draw_figures()`** → Draws X and O symbols.
- **`check_winner()`** → Checks for a winning player.
- **`draw_winner_text(winner)`** → Displays the winner text.
- **`restart_game()`** → Clears the board and restarts the game.


## 📝 License
This project is open-source and free to use!

