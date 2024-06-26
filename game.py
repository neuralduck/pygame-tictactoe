import pygame as pg 
import sys
from tictactoe import Tictactoe
tile_size = 200
(width, height) = (3*tile_size, 3*tile_size)
bg_color1 = (165, 221, 227, 0.45)
bg_color2 = (145, 189, 193, 0.45)
X_color = (7, 183, 38, 0.76)
O_color = (119, 3, 179, 0.76)
class Game:
	def __init__(self):
		pg.init()
		self.surface = pg.display.set_mode((width, height), pg.SRCALPHA)
		pg.display.set_caption('Tic tac toe')
		self.surface.fill(bg_color1)
		self.font = pg.font.SysFont('Arial', 100)
		self.game_over = False
		self.move_history = []
		self.turn = 1
		self.player1 = 1
		self.player2 = -1
		self.grid2board = {
		(100.0, 100.0): 0,
		(300.0, 100.0): 1,
		(500.0, 100.0): 2,
		(100.0, 300.0): 3,
		(300.0, 300.0): 4,
		(500.0, 300.0): 5,
		(100.0, 500.0): 6,
		(300.0, 500.0): 7,
		(500.0, 500.0): 8,
		}
		self.win_lines = {
		(0, 1, 2): ((0, 100), (600, 100)),
		(3, 4, 5): ((0, 300), (600, 300)),
		(6, 7, 8): ((0, 500), (600, 500)),
		(0, 3, 6): ((100, 0), (100, 600)),
		(1, 4, 7): ((300, 0), (300, 600)),
		(2, 5, 8): ((500, 0), (500, 600)),
		(0, 4, 8): ((0, 0), (600, 600)),
		(2, 4, 6): ((600, 0), (0, 600))
		}
		for row in range(width):
			for col in range(row%2, width, 2):
				pg.draw.rect(self.surface, bg_color2, (row*tile_size, col*tile_size, tile_size, tile_size))
		pg.draw.line(self.surface, 'black', (200, 0), (200, height), 3)
		pg.draw.line(self.surface, 'black', (400, 0), (400, height), 3)
		pg.draw.line(self.surface, 'black', (0, 200), (width, 200), 3)
		pg.draw.line(self.surface, 'black', (0, 400), (width, 400), 3)

	def draw_text(self, text, x = 200, y = 200, text_col = 'black'):
		img = self.font.render(text, True, text_col)
		self.surface.blit(img, (x, y))
	def mark_square(self, pos, player):
		if player == -1:
			pg.draw.circle(self.surface, O_color, pos, 80, width = 15)
		if player == 1:
			#pg.draw.circle(self.surface, (0, 0, 255), pos, 80)
			x1, y1 = pos[0] - 60, pos[1] + 60
			x2, y2 = pos[0] + 60, pos[1] - 60
			x3, y3 = pos[0] + 60, pos[1] + 60
			x4, y4 = pos[0] - 60, pos[1] - 60
			pg.draw.line(self.surface, X_color, (x1, y1), (x2, y2), width = 15)
			pg.draw.line(self.surface, X_color, (x3, y3), (x4, y4), width = 15)
	def play(self):
		board = Tictactoe()
		while True:
			result, squares = board.check(index = True)
			if not(self.game_over):
				if (result == 1):
						print('x wins')
						print(squares)
						start, end = self.win_lines[squares]
						pg.draw.line(self.surface, (0, 0, 255), start, end, width = 10)
						#self.draw_text('X Wins')
						self.game_over = True
				elif (result == -1):
					print('o wins')
					print(squares)
					start, end = self.win_lines[squares]
					pg.draw.line(self.surface, (0, 0, 255), start, end, width = 10)
					self.surface.set_alpha(255)
					#self.draw_text('O wins')
					self.game_over = True
				elif(result == 0):
					print('draw')
					self.draw_text('Draw')
					self.game_over = True
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				if (event.type == pg.MOUSEBUTTONUP) and not(self.game_over):
					pos = pg.mouse.get_pos()
					x = (tile_size * (pos[0] // tile_size)) + (tile_size/2)
					y = (tile_size * (pos[1] // tile_size)) + (tile_size/2)
					if (x, y) not in self.move_history:
						self.move_history.append((x, y))
						if self.turn:
							self.mark_square((x, y), player = 1)
							board.move(self.grid2board[(x, y)], 1)
						else:
							self.mark_square((x, y), player = -1)
							board.move(self.grid2board[(x, y)], -1)
						self.turn = int(not(self.turn))
			pg.display.update()


if __name__ == '__main__':
	game = Game()
	game.play()