import random
import tkinter as tk
from tkinter import messagebox

MAZE_WIDTH = 10
MAZE_HEIGHT = 10
CELL_SIZE = 40
NUM_WALLS = 40
TIME_LIMIT = 30

class MazeGame:
    def __init__(self, master):
        self.master = master
        self.master.title('2D Maze Game')

        self.canvas = tk.Canvas(self.master, width=MAZE_WIDTH * CELL_SIZE, height=MAZE_HEIGHT * CELL_SIZE)
        self.canvas.pack()

        self.info_box = tk.Label(self.master, text='', font=('Arial', 14))
        self.info_box.pack()

        self.timer_label = tk.Label(self.master, text='', font=('Arial', 14))
        self.timer_label.pack()

        self.player_x = 0
        self.player_y = 0
        self.goal_x = 0
        self.goal_y = 0
        self.move_count = 0
        self.remaining_time = TIME_LIMIT
        self.timer_id = None

        self.generate_maze()
        self.draw_maze()
        self.place_objects()
        self.start_timer()

        self.canvas.bind('<KeyPress>', self.on_key_press)
        self.canvas.focus_set()

    def generate_maze(self):
        self.maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]

        for _ in range(NUM_WALLS):
            while True:
                x = random.randint(0, MAZE_WIDTH - 1)
                y = random.randint(0, MAZE_HEIGHT - 1)
                if self.maze[y][x] == 0 and (x != self.player_x or y != self.player_y):
                    self.maze[y][x] = 1
                    break

        self.draw_maze()
        self.update_info_box()

    def draw_maze(self):
        self.canvas.delete('maze')
        for i in range(MAZE_HEIGHT):
            for j in range(MAZE_WIDTH):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='black', tags='maze')

    def place_objects(self):
        if self.goal_x == 0 and self.goal_y == 0:
            while True:
                self.goal_x = random.randint(0, MAZE_WIDTH - 1)
                self.goal_y = random.randint(0, MAZE_HEIGHT - 1)
                if self.maze[self.goal_y][self.goal_x] == 0 and (self.goal_x != self.player_x or self.goal_y != self.player_y):
                    break

            self.canvas.create_rectangle(self.goal_x * CELL_SIZE, self.goal_y * CELL_SIZE,
                                        (self.goal_x + 1) * CELL_SIZE, (self.goal_y + 1) * CELL_SIZE,
                                        fill='red', tags='goal')

        self.draw_player()

    def draw_player(self):
        self.canvas.delete('player')
        x1 = self.player_x * CELL_SIZE
        y1 = self.player_y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_oval(x1, y1, x2, y2, fill='green', tags='player')

    def update_info_box(self):
        player_shape = '\u25cf'
        goal_shape = '\u25a0'
        info_text = f'Moves: {self.move_count}\nPlayer: {player_shape}\nGoal: {goal_shape}'
        self.info_box.config(text=info_text)

    def start_timer(self):
        self.remaining_time = TIME_LIMIT
        self.update_timer_label()
        self.timer_id = self.canvas.after(1000, self.update_timer)

    def update_timer(self):
        self.remaining_time -= 1
        self.update_timer_label()
        if self.remaining_time <= 0:
            self.show_message('Time Up!', 'You ran out of time.')
            self.master.destroy()
        else:
            self.timer_id = self.canvas.after(1000, self.update_timer)

    def update_timer_label(self):
        self.timer_label.config(text=f'Time: {self.remaining_time} s')

    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
            if self.maze[new_y][new_x] == 0:
                self.player_x = new_x
                self.player_y = new_y
                self.move_count += 1
                self.draw_player()
                self.update_info_box()
                if self.player_x == self.goal_x and self.player_y == self.goal_y:
                    self.show_message('Congratulations!', f'You reached the goal in {self.move_count} moves.')
                    self.master.destroy()
                    return  
            else:
                self.show_message('Invalid Move', 'You cannot move there!')
        else:
            self.show_message('Invalid Move', 'You cannot move outside the maze!')

        possible_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        has_possible_move = any(self.is_valid_move(dx, dy) for dx, dy in possible_moves)
        if not has_possible_move or self.is_player_blocked() or self.is_goal_blocked():
            self.show_message('No Possible Moves', 'Regenerating maze...')
            self.generate_maze()
            self.draw_maze()
            self.place_objects()
            self.start_timer()

    def on_key_press(self, event):
        if event.keysym == 'Up':
            self.move_player(0, -1)
        elif event.keysym == 'Down':
            self.move_player(0, 1)
        elif event.keysym == 'Left':
            self.move_player(-1, 0)
        elif event.keysym == 'Right':
            self.move_player(1, 0)

    def is_valid_move(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT:
            return self.maze[new_y][new_x] == 0
        return False

    def is_player_blocked(self):
        blocked_ways = 0
        obstacles = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in obstacles:
            new_x = self.player_x + dx
            new_y = self.player_y + dy
            if not (0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT):
                blocked_ways += 1
            elif self.maze[new_y][new_x] == 1:
                blocked_ways += 1
        return blocked_ways >= 3

    def is_goal_blocked(self):
        blocked_ways = 0
        obstacles = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in obstacles:
            new_x = self.goal_x + dx
            new_y = self.goal_y + dy
            if not (0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT):
                blocked_ways += 1
            elif self.maze[new_y][new_x] == 1:
                blocked_ways += 1
        return blocked_ways >= 3

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def run(self):
        self.master.mainloop()

root = tk.Tk()
maze_game = MazeGame(root)
maze_game.run()