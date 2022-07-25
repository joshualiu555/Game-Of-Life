WIDTH = 1200
HEIGHT = 800
FPS = 30

CELL_SIZE = 10

NUM_ROWS = int(WIDTH / CELL_SIZE)
NUM_COLUMNS = int(HEIGHT / CELL_SIZE)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
