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
		self.surface = pg.display.set_mode((width, height))
		self.surface.fill(bg_color1)
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
		for row in range(width):
			for col in range(row%2, width, 2):
				pg.draw.rect(self.surface, bg_color2, (row*tile_size, col*tile_size, tile_size, tile_size))

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
			result = board.check()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
				
				if result == 1:
					print('x wins')
				elif result == -1:
					print('o wins')
				elif result == 3:
					if event.type == pg.MOUSEBUTTONUP:
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