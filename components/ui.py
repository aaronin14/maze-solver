import tkinter as tk

class Settings:
    def __init__(self, frame, maze):
        self.__frame = frame
        self.__maze = maze
        # Maze Settings
        self.__frame1 = tk.Frame(self.__frame)
        self.__frame1.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.__frame1.columnconfigure(0, weight=1)
        # Num Rows
        self.__lbl_num_rows = tk.Label(self.__frame1, text="Num Rows (max=30):")
        self.__lbl_num_rows.grid(row=0, column=0, sticky="w")
        self.__entry_num_rows = tk.Entry(self.__frame1, width=10)
        self.__entry_num_rows.grid(row=0, column=1)
        # Num Cols
        self.__lbl_num_cols = tk.Label(self.__frame1, text="Num Cols (max=30):")
        self.__lbl_num_cols.grid(row=1, column=0, sticky="w")
        self.__entry_num_cols = tk.Entry(self.__frame1, width=10)
        self.__entry_num_cols.grid(row=1, column=1)
        # Generate Button
        self.__btn_generate = tk.Button(self.__frame1, text="Generate", command=self.__maze.generate_maze)
        self.__btn_generate.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Algorithm Options
        self.__frame2 = tk.Frame(self.__frame)
        self.__frame2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.__frame2.columnconfigure(0, weight=1)
        # Radiobuttons
        self.algorithm_option = tk.StringVar(value="DFS")
        self.__rb1 = tk.Radiobutton(self.__frame2, text="Depth-First Search", variable=self.algorithm_option, value="DFS")
        self.__rb2 = tk.Radiobutton(self.__frame2, text="Breadth-First Search", variable=self.algorithm_option, value="BFS")
        self.__rb3 = tk.Radiobutton(self.__frame2, text="A* Search", variable=self.algorithm_option, value="A*")
        self.__btn_solve = tk.Button(self.__frame2, text="Solve", command=self.__maze.solve)
        self.__rb1.grid(row=4, column=0, sticky="w")
        self.__rb2.grid(row=5, column=0, sticky="w")
        self.__rb3.grid(row=6, column=0, sticky="w")
        self.__btn_solve.grid(row=7, column=0, columnspan=2, sticky="ew")
