from cell import *
from random import randint

class Program:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Conway's Game of Life Simulation")
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()
        self.board = []

        self.running = True

    def new(self):
        for x in range(NUM_ROWS):
            row = []
            for y in range(NUM_COLUMNS):
                state = randint(0, 1)
                cell = Cell(state, x, y)
                row.append(cell)
                self.all_sprites.add(cell)
            self.board.append(row)

    def run(self):
        self.clock.tick(FPS)
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        change_state = []

        for x in range(NUM_ROWS):
            for y in range(NUM_COLUMNS):
                cell = self.board[x][y]
                num_neighbors = 0
                for i in range(8):
                    # cells on the edge of the board must wrap around
                    wrap_row = (cell.x + dx[i] + NUM_ROWS) % NUM_ROWS
                    wrap_column = (cell.y + dy[i] + NUM_COLUMNS) % NUM_COLUMNS
                    num_neighbors += self.board[wrap_row][wrap_column].state
                if not cell.state and num_neighbors == 3:
                    change_state.append((x, y))
                elif cell.state == 1 and (num_neighbors < 2 or num_neighbors > 3):
                    change_state.append((x, y))

        # must separately reiterate so the board updates in unison
        for cell in change_state:
            self.board[cell[0]][cell[1]].change_state()
    
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.update()

simulation = Program()
simulation.new()
while simulation.running:
    simulation.run()

pg.quit()
