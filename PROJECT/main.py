import tkinter as tk


def draw_grid():
    canvas.delete("all")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j]:
                canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                                        fill="white")


def update_grid():
    global is_started
    if is_started:
        new_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                neighbors = sum(
                    [
                        grid[i - 1][j - 1],
                        grid[i - 1][j],
                        grid[i - 1][(j + 1) % GRID_SIZE],
                        grid[i][j - 1],
                        grid[i][(j + 1) % GRID_SIZE],
                        grid[(i + 1) % GRID_SIZE][j - 1],
                        grid[(i + 1) % GRID_SIZE][j],
                        grid[(i + 1) % GRID_SIZE][(j + 1) % GRID_SIZE],
                    ]
                )
                if grid[i][j] and (neighbors == 2 or neighbors == 3):
                    new_grid[i][j] = 1
                elif not grid[i][j] and neighbors == 3:
                    new_grid[i][j] = 1
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                grid[i][j] = new_grid[i][j]
    draw_grid()

    root.after(DELAY, update_grid)


def handle_click(event):
    row = event.y // CELL_SIZE
    col = event.x // CELL_SIZE
    grid[row][col] = 1 - grid[row][col]
    draw_grid()


def stop():
    global is_started
    is_started = False


def start():
    global is_started
    is_started = True


def create_buttons():
    start_button = tk.Button(
        root, text='start', command=start)
    stop_button = tk.Button(
        root, text='stop', command=stop)
    start_button.pack()
    stop_button.pack()


if __name__ == "__main__":
    global is_started
    is_started = False

    GRID_SIZE = 125
    CELL_SIZE = 10
    DELAY = 10

    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    root = tk.Tk()
    root.title("Game of Life")

    canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="black")
    canvas.bind("<Button-1>", handle_click)

    draw_grid()
    canvas.pack()
    create_buttons()
    update_grid()

    root.mainloop()