_This project has been created as part
of the 42 curriculum by macarrara, jhenriqu_

# A_MAZE_ING

**Description**

This is a maze generator created as part of the 42 curriculum. The project uses Depth-First Search (DFS) to generate a maze with parameters defined in its configuration file, config.txt. It then displays the maze in the terminal and allows user interaction. The program also outputs a file containing both the solution path and the generated maze encoded in hexadecimal values.



**Instructions**

The project directory contains a subdirectory named mazegen, which includes the maze generation and manipulation scripts, the a_maze_ing.py script used to start the program, a config.txt file containing the maze parameters, a pyproject.toml file for building the mazegen package, the packages mazegen-1.0.0.tar.gz and mazegen-1.0.0-py3-none-any.whl used to install mazegen, and a Makefile.

To run the program, execute:
`python3 a_maze_ing.py config.txt`

or simply run: 

`make` or `make run`.

Once the UI is displayed, you can type the number corresponding to your chosen option and press Enter:

1 -> Regenerate the maze

2 -> Show or hide the solution path

3 -> Change colors in the maze

4 -> Exit (or press Ctrl + C)

To change the maze parameters, modify the values in the `config.txt` file.

**Maze configuration file (with examples)**

`WIDTH=15` -> Changes width of the maze (Maximum 40, minimum 5).

`HEIGHT=15` -> Changes height of the maze (Maximum 40, minimum 5).

`ENTRY=0,0` -> Starting point (cannot be outside boundaries or inside the 42 logo).

`EXIT=14,14` -> Exit point (cannot be outside boundaries or inside the 42 logo).

`OUTPUT_FILE=maze.txt` -> Output file containing the maze and solution path in hexadecimal.

`PERFECT=False` -> Determines whether the maze is perfect.

`SEED=42` -> (Optional) Ensures reproducibility.

**Makefile instructions**

We include a Makefile to simplify running the program and performing additional tasks. Simply type make in your terminal. For example:

`make`

* `make` -> Will install the necessary dependencies like mypy and flake8 and will then run the program.
* `make run` -> Will just run the program same typing in your terminal "python3 a_maze_ing.py config.txt".
* `make vrt` -> will create a virtual environment and install the necessary dependencies to re-build the mazegen package.
*` make debug` -> Will run the program in debugger mode.
* `make build` -> will build and install the mazegen module.
* `make lint` -> Will run flake8 and mypy with flags --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
* `make clean` -> Will remove temporary files and pip uninstall mazegen package.
* `make re` -> will run make clean and re-run make.


**Resources**

https://www.youtube.com/watch?v=ioUl1M77hww -> Explain various maze generation algorithms

https://medium.com/@nacerkroudir/randomized-depth-first-search-algorithm-for-maze-generation-fb2d83702742 -> DFS Maze Generation

https://en.wikipedia.org/wiki/Depth-first_search -> DFS explained in detail

https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124 -> ANSI Color codes.

 * AI was used in multiple steps in this project but mainly for debugging purposes

 	    1. Missing blocks when printing the path.

 	    2. Located issue over package not importing all of the funtions from the mazegen module.

 	    3. Providing ANSI color codes and identifying alignment issues in path.


**Maze Generation Algorithm**

We used a randomized Depth-First Search (DFS) backtracking algorithm to generate the maze. Starting from the entry point, the algorithm explores random paths through the grid until it has visited every cell. Along the way, it removes walls between cells. When it encounters a previously visited node or a dead end, it backtracks to explore alternative paths, resulting in a perfect maze.

If the PERFECT parameter is set to False, the algorithm will remove additional walls to create a non-perfect maze.

Given the amount of available information and examples online (particularly on YouTube), this approach was chosen as the most suitable for maze generation.

**Code Reusability**

The mazegen module is capable of generating both perfect and non-perfect mazes, displaying them, and writing the output file. By running make build, mazegen is packaged and can later be installed via pip for reuse in other projects.

* `read_configuration` -> will open a file and parse the configurations and add it to class Configuration(read segment *Instructions* to check format for maze configuration file structure).

* `MazeGenerator` -> Accepts the following parameters:

	1. width (maze width)
	2. height (maze height)
	3. value_entry (x, y coordinates of the entry point)
	4. value_exit (x, y coordinates of the exit point)
	5. output_file (name of the output file containing the maze in hexadecimal)
	6. seed (optional, for reproducibility)

* `display_maze` -> will render the maze generated in the terminal.

* `write_maze` -> creates the output file with the maze information in hexadecimal.

**Project Management**

Initially, the project was divided between team members: Marco worked on parsing the config.txt file and handling errors, while Joel focused on the maze generation algorithm. We scheduled collaborative sessions on Wednesdays, starting with implementing the maze display.

However, working simultaneously on the same tasks led to inconsistencies in the code. To address this, we adopted a "relay race" workflow, where each member continued from where the other left off. This approach helped maintain consistency and ensured shared understanding across the codebase.

While this strategy proved effective, we recognized that better time management could have allowed us to complete the project earlier.

Aside from AI (used mainly for debugging and providing helpful references such as ANSI color tables), no additional tools were used in this project.