import tkinter as tk


class GameOfLife:
    def __init__(self):
        self.first_rule = []
        self.second_rule = []
        self.rules_input = None
        self.slider = None
        self.reset_button = None
        self.stop_button = None
        self.start_button = None
        self.is_started = False
        self.GRID_SIZE = 75
        self.CELL_SIZE = 10
        self.DELAY = 10
        self.grid = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]

        self.root = tk.Tk()
        self.root.title("Game of Life")
        self.root.configure(background='black')

        self.canvas = tk.Canvas(self.root, width=self.GRID_SIZE * self.CELL_SIZE,
                                height=self.GRID_SIZE * self.CELL_SIZE, bg="black")
        self.canvas.bind("<Button-1>", self.handle_click)
        self.rules = tk.StringVar()
        self.rules.set("23/3")
        self.handle_rules_update(None, None, None)
        self.rules.trace_add("write", self.handle_rules_update)

        self.draw_grid()
        self.canvas.pack()
        self.create_buttons()
        self.update_grid()

        self.root.mainloop()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.grid[i][j]:
                    self.canvas.create_rectangle(j * self.CELL_SIZE, i * self.CELL_SIZE, (j + 1) * self.CELL_SIZE,
                                                 (i + 1) * self.CELL_SIZE,
                                                 fill="white")

    def update_grid(self):
        if self.is_started:
            new_grid = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
            for i in range(self.GRID_SIZE):
                for j in range(self.GRID_SIZE):
                    neighbors = sum(
                        [
                            self.grid[i - 1][j - 1],
                            self.grid[i - 1][j],
                            self.grid[i - 1][(j + 1) % self.GRID_SIZE],
                            self.grid[i][j - 1],
                            self.grid[i][(j + 1) % self.GRID_SIZE],
                            self.grid[(i + 1) % self.GRID_SIZE][j - 1],
                            self.grid[(i + 1) % self.GRID_SIZE][j],
                            self.grid[(i + 1) % self.GRID_SIZE][(j + 1) % self.GRID_SIZE],
                        ]
                    )

                    if self.grid[i][j] and (any(map(lambda x: neighbors == int(x), self.first_rule))):
                        new_grid[i][j] = 1
                    elif not self.grid[i][j] and any(map(lambda x: neighbors == int(x), self.second_rule)):
                        new_grid[i][j] = 1
            for i in range(self.GRID_SIZE):
                for j in range(self.GRID_SIZE):
                    self.grid[i][j] = new_grid[i][j]
        self.draw_grid()

        self.root.after(self.DELAY, self.update_grid)

    def handle_click(self, event):
        row = event.y // self.CELL_SIZE
        col = event.x // self.CELL_SIZE
        self.grid[row][col] = 1 - self.grid[row][col]
        self.draw_grid()

    def stop(self):
        self.is_started = False

    def start(self):
        self.is_started = True

    def reset(self):
        self.grid = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        self.stop()

    def create_buttons(self):
        self.start_button = tk.Button(
            self.root, text='start', command=self.start)
        self.stop_button = tk.Button(
            self.root, text='stop', command=self.stop)
        self.reset_button = tk.Button(
            self.root, text='reset', command=self.reset)
        self.rules_input = tk.Entry(self.root, textvariable=self.rules)
        self.slider = tk.Scale(self.root, from_=1, to=1000, orient=tk.HORIZONTAL)
        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()
        self.slider.pack()
        self.rules_input.pack()
        self.slider.bind("<ButtonRelease-1>", self.update_value)

    def update_value(self, _):
        self.DELAY = self.slider.get()

    def update_grid_size(self, _):
        self.GRID_SIZE = self.grid_size_slider.get()
        self.draw_grid()

    def handle_rules_update(self, _, __, ___):
        rules = self.rules.get()
        split_rules = rules.split("/")
        self.first_rule = [*split_rules[0]]
        self.second_rule = [*split_rules[1]]
        print(self.first_rule)
        return True


if __name__ == "__main__":
    GameOfLife()
