import tkinter as tk

class UserInterface:
    def __init__(self, root, frame, maze, maze_graphic):
        self.__maze_graphic = maze_graphic
        self.__root = root
        self.__frame = frame
        self.__maze = maze
        self.__default_rows = tk.StringVar(value="15")
        self.__default_cols = tk.StringVar(value="15")
        self.__algorithm_option = tk.StringVar(value="DFS")

        # Maze Settings
        self.__groupbox_maze_settings = tk.LabelFrame(self.__frame, text="Maze Settings", padx=5, pady=5)
        self.__groupbox_maze_settings.grid(row=0, column=0, padx=15, pady=10, sticky="ew")
        self.__groupbox_maze_settings.columnconfigure(0, weight=1)
        # Num Rows
        self.__lbl_rows = tk.Label(self.__groupbox_maze_settings, text="Num Rows (5-30):")
        self.__lbl_rows.grid(row=0, column=0, sticky="w")
        self.__sb_rows = tk.Spinbox(self.__groupbox_maze_settings, justify="right", from_=5, to=30, textvariable=self.__default_rows, increment=1, width=10, command=self.on_spinbox_value_change)
        self.__sb_rows.grid(row=0, column=1)
        # Num Cols
        self.__lbl_cols = tk.Label(self.__groupbox_maze_settings, text="Num Cols (5-30):")
        self.__lbl_cols.grid(row=1, column=0, sticky="w")
        self.__sb_cols = tk.Spinbox(self.__groupbox_maze_settings, justify="right", from_=5, to=30, textvariable=self.__default_cols, increment=1, width=10, command=self.on_spinbox_value_change)
        self.__sb_cols.grid(row=1, column=1)

        # Generate Button
        self.__btn_generate = tk.Button(self.__frame, text="Generate", command=self.__maze.generate_maze)
        self.__btn_generate.grid(row=1, column=0, padx=15, sticky="ew")

        # Algorithm Options
        self.__groupbox_algorithms = tk.LabelFrame(self.__frame, text="Algorithm Options", padx=5, pady=5)
        self.__groupbox_algorithms.grid(row=2, column=0, padx=15, pady=10, sticky="nsew")
        # Radiobuttons
        self.__rb1 = tk.Radiobutton(self.__groupbox_algorithms, text="Depth-First Search", variable=self.__algorithm_option, value="DFS")
        self.__rb2 = tk.Radiobutton(self.__groupbox_algorithms, text="Breadth-First Search", variable=self.__algorithm_option, value="BFS")
        self.__rb3 = tk.Radiobutton(self.__groupbox_algorithms, text="A* Search", variable=self.__algorithm_option, value="A*")
        self.__rb1.grid(row=1, column=0, sticky="w")
        self.__rb2.grid(row=2, column=0, sticky="w")
        self.__rb3.grid(row=3, column=0, sticky="w")

        # Solve Button
        self.__btn_solve = tk.Button(self.__frame, text="Solve", command=self.solve)
        self.__btn_solve.grid(row=3, column=0, padx=15, sticky="ew")

        # Animation Speed
        self.__groupbox_animations = tk.LabelFrame(self.__frame, text="Animation Speed", padx=5, pady=5)
        self.__groupbox_animations.grid(row=4, column=0, padx=15, pady=10, sticky="nsew")
        self.__scale_spd = tk.Scale(self.__groupbox_animations, from_=0, to=10, orient="horizontal", length=250, command=self.on_scale_value_change)
        self.__scale_spd.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.__scale_spd.set(10)

        # Reset Button
        self.__btn_reset = tk.Button(self.__frame, text="Reset", command=self.reset)
        self.__btn_reset.grid(row=6, column=0, padx=15, sticky="ew")

        # Exit Button
        self.__btn_exit = tk.Button(self.__frame, text="Exit", command=self.exit) # Add exit function
        self.__btn_exit.grid(row=7, column=0, padx=15, sticky="ew")

    def on_spinbox_value_change(self):
        self.__maze.set_rows(int(self.__sb_rows.get()))
        self.__maze.set_cols(int(self.__sb_cols.get()))

    def on_scale_value_change(self, value):
        self.__maze.set_speed(int(value))

    def solve(self):
        selected_algorithm = self.__algorithm_option.get()
        self.__maze.solve(selected_algorithm)

    def reset(self):
        self.__default_cols.set("15")
        self.__default_rows.set("15")
        self.__algorithm_option.set("DFS")
        self.__scale_spd.set(10)
        self.on_scale_value_change(10)
        self.on_spinbox_value_change()
        self.__maze.reset()

    def exit(self):
        self.__maze_graphic.close()
        self.__root.destroy()

