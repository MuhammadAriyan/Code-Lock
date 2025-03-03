import pygame,sys
import numpy as np
# Initialize Pygame
pygame.init()
# heoght and width of the screen
WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COLS = 3

X_COLOR = (84, 84, 84)  
O_COLOR = (242, 235, 211) 

# set display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption
pygame.display.set_caption("TIC TAC TOE")

# initialize bg color and Line color
BG_COLOR = (27, 176, 160)
LINE_COLOR = (23, 145, 135)
# set background color
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))


# draw lines
def draw_lines():
	pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3, 50), (WIDTH // 3, HEIGHT - 50), 7)
	pygame.draw.line(screen, LINE_COLOR, (2 * WIDTH // 3, 50), (2 * WIDTH // 3, HEIGHT - 50), 7)
	pygame.draw.line(screen, LINE_COLOR, (50, HEIGHT // 3), (WIDTH - 50, HEIGHT // 3), 7)
	pygame.draw.line(screen, LINE_COLOR, (50, 2 * HEIGHT // 3), (WIDTH - 50, 2 * HEIGHT // 3), 7)

draw_lines()

# mark square
def mark_square(row, col, player):
	if board[row][col] == 0:  # 0 means an empty square
		board[row][col] = player
		return True  # move successful
	return False  # move invalid (already occupied)

# checks if board is completed
def is_board_full():
	for row in board:
		for box in row:
			if box == 0:
				return False
	return True

# draw figures
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):      
			cell_x = col * WIDTH // BOARD_COLS
			cell_y = row * HEIGHT // BOARD_ROWS
			cell_size = WIDTH // BOARD_COLS
			margin = 50  # Padding inside the cell
			if board[row][col] == 1:
				# Draw first diagonal (Top-Left to Bottom-Right)
				pygame.draw.line(screen, X_COLOR, 
					(cell_x + margin, cell_y + margin),  
	 				(cell_x + cell_size - margin, cell_y + cell_size - margin), 7)
				# Draw second diagonal (Top-Right to Bottom-Left)
				pygame.draw.line(screen, X_COLOR,  
				(cell_x + cell_size - margin, cell_y + margin),  
				(cell_x + margin, cell_y + cell_size - margin), 7)
			elif board[row][col] == 2:
				pygame.draw.circle(screen, O_COLOR,
					(int(col * WIDTH // BOARD_COLS + WIDTH // BOARD_COLS // 2), int(row * HEIGHT // BOARD_ROWS + HEIGHT // BOARD_ROWS // 2)), WIDTH // BOARD_COLS // 3, 7)

def check_winner():
    # CHECK ROW AND COL
    for i in range(BOARD_ROWS):
        # check row
        if board[i][0] ==  board[i][1] ==  board[i][2] != 0:
            return board[i][0]
        if board[0][i] ==  board[1][i] ==  board[2][i] != 0:
            return board[0][i]
        if board[0][0] ==  board[1][1] ==  board[2][2] != 0:
            return board[0][0]
        if board[0][2] ==  board[1][1] ==  board[2][0] != 0:
            return board[0][0]
    return 0
# mouse click
def get_mouse_click():
	mouseX,mouseY = pygame.mouse.get_pos()
	row = mouseY // (HEIGHT // BOARD_ROWS)
	col = mouseX // (WIDTH // BOARD_COLS)
	return row, col

def draw_winner_text(winner):
    font = pygame.font.Font(None, 50)  # Use default font, size 50
    text = font.render(f"Player {winner} Wins!", True, (255, 255, 255))  # White color
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text

    screen.fill(BG_COLOR)  # Clear screen
    screen.blit(text, text_rect)  # Draw text
    pygame.display.update()

player = 1

# main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			row,col = get_mouse_click()
			if mark_square(row, col, player):
				if player == 1:
					player = 2
				else:
					player = 1
	pygame.display.update()
	draw_figures()
	if check_winner() != 0:
		draw_winner_text(check_winner())