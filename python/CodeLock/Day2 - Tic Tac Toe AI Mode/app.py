import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
BG_COLOR = (27, 176, 160)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)

# Game board
board = np.zeros((ROWS, COLS))

# Winning combinations
WINNING_COMBOS = [
	[(0, 0), (0, 1), (0, 2)],  # Row 1
	[(1, 0), (1, 1), (1, 2)],  # Row 2
	[(2, 0), (2, 1), (2, 2)],  # Row 3
	[(0, 0), (1, 0), (2, 0)],  # Col 1
	[(0, 1), (1, 1), (2, 1)],  # Col 2
	[(0, 2), (1, 2), (2, 2)],  # Col 3
	[(0, 0), (1, 1), (2, 2)],  # Diagonal 1
	[(0, 2), (1, 1), (2, 0)]   # Diagonal 2
]

# Draw grid lines
def draw_grid():
	screen.fill(BG_COLOR)
	for i in range(1, ROWS):
		pygame.draw.line(screen, LINE_COLOR, (i * WIDTH // 3, 50), (i * WIDTH // 3, HEIGHT - 50), 7)
		pygame.draw.line(screen, LINE_COLOR, (50, i * HEIGHT // 3), (WIDTH - 50, i * HEIGHT // 3), 7)

def mark_cell(row, col, player):
	if board[row][col] == 0:
		board[row][col] = player
		return True
	return False

def board_full():
	return not (board == 0).any()

def draw_shapes():
	for row in range(ROWS):
		for col in range(COLS):
			x, y = col * WIDTH // COLS, row * HEIGHT // ROWS
			size = WIDTH // COLS
			margin = 50
			if board[row][col] == 1:
				pygame.draw.line(screen, X_COLOR, (x + margin, y + margin), (x + size - margin, y + size - margin), 7)
				pygame.draw.line(screen, X_COLOR, (x + size - margin, y + margin), (x + margin, y + size - margin), 7)
			elif board[row][col] == 2:
				pygame.draw.circle(screen, O_COLOR, (x + size // 2, y + size // 2), size // 3, 7)

def check_winner(board_to_check):
	for combo in WINNING_COMBOS:
		if board_to_check[combo[0][0]][combo[0][1]] == board_to_check[combo[1][0]][combo[1][1]] == board_to_check[combo[2][0]][combo[2][1]] != 0:
			return board_to_check[combo[0][0]][combo[0][1]]
	return 0

def get_click():
	x, y = pygame.mouse.get_pos()
	return y // (HEIGHT // ROWS), x // (WIDTH // COLS)

def display_winner(winner):
	font = pygame.font.Font(None, 50)
	text = font.render(f"Player {winner} Wins!", True, (255, 255, 255))
	screen.fill(BG_COLOR)
	screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
	pygame.display.update()
	pygame.time.wait(3000)

def reset_board():
	global board
	board = np.zeros((ROWS, COLS))
	draw_grid()


# DAY2 
# def for rating move


# def to get remaining box 
def get_remaining_boxes(board):
	remaining_boxes = []
	for i in range(ROWS):
		for box in range(COLS):
			if board[box][i] == 0:
				remaining_boxes.append((box, i))
	return remaining_boxes

def win_move(board_to_check):
	remaining_boxes = get_remaining_boxes(board_to_check)
	if board_to_check[1][1] == 0 :
		return 1,1
	for box in remaining_boxes:
		x, y = box
		board_to_check[x][y] = 2
		if check_winner(board_to_check) == 2:
			board_to_check[x][y] = 0  # Reset the board after checking
			return box
		else :
			board_to_check[x][y] = 1
			if check_winner(board_to_check) == 1:
				board_to_check[x][y] = 0
				return box
		board_to_check[x][y] = 0  # Reset the board after checking
	return remaining_boxes[0] if remaining_boxes else None

def main():
	screen.fill(BG_COLOR)
	draw_grid()
	player = 1
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and not board_full():
				if player == 1:
					row, col = get_click()
					if mark_cell(row, col, player):
						player = 2
		
		if player == 2 and not board_full():
			move = win_move(board)
			if move:
				row, col = move
				if mark_cell(row, col, player):
					player = 1
		
		draw_shapes()
		winner = check_winner(board)
		if winner:
			display_winner(winner)
			reset_board()
			player = 1
		elif board_full():
			reset_board()
			player = 1
		pygame.display.update()

if __name__ == "__main__":
	main()


# so guys right now i am tired and i will continue tomorrow
