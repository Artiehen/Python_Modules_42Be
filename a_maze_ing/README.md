_This project has been created as part
of the 42 curriculum by macarrara[,jhenriqu]_

# A_MAZE_ING

**Description**

• This is a Maze generator created as part of the 42 curriculum. The project uses Depth-First Search(DFS) to generate a Maze with parameters defined in its configuration file named "config.txt", it will then display it in the terminal and be able to interract with the maze. It will also output a file that contains the solution path as well as the maze generated encoded in hexadecimal values. 



**Instructions**

The project directory contains a sub-directory named 'mazegen', containing the maze generation and manipulation scripts, a_maze_ing.py script used to start the program, a config.txt file that contains the maze's parameters, pyproject.toml for building the mazegen package, the packages mazegen-1.0.0.tar.gz & mazegen-1.0.0-py3-none-any.whl used to install mazegen and a make file.

1. To run the program you must run: python3 a_maze_ing.py config.txt in your terminal or simply run commands make or make run.
2. Once the UI displays you can type the number of the option you selected and press enter.

	    1 -> Will re-generate the maze.

	    2 -> Show or Hide the solution path.

	    3 -> Change colors in the maze.

	    4 -> Exit (or pressing Ctrl + C)


To change the parameters of the maze, you must change the values in "config.txt" file.

 Maze configuration file with examples

WIDTH=15 -> changes with of maze

HEIGHT=15 -> changes height of maze

ENTRY=0,0 -> starting point in the maze(cannot be outside boundries or inside 42 logo)

EXIT=14,14 -> Exit point in the maze(cannot be outside boundries or inside 42 logo)

OUTPUT_FILE=maze.txt -> output file containing the maze in hexadecimal and the solution path

PERFECT=False -> Parameter that determines if the maze is perfect or not.

SEED=42 -> (OPTIONAL) Reproducibility of the maze

Makefile instructions

We include a makefile that is very useful in running the program and performing additional task simpler.

* make -> Will install the necessary dependencies like mypy and flake8 and will then run the program.
* make run -> Will just run the program same typing in your terminal "python3 a_maze_ing.py config.txt".
* make vrt -> will create a virtual environment and install the necessary dependencies to re-build the mazegen package.
* make debug -> Will run the program in debugger mode.
* make build -> will build and install the mazegen module.
* make lint -> Will run flake8 and mypy with flags --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
* make clean -> Will remove temporary files and pip uninstall mazegen package.
* make re -> will run make clean and re-run make.


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

We used Randomized Depth-First Search backtracking to generate our maze. From the starting point it will take random paths to traverse the grid until it reaches the exit point, while doing so it sill be removing walls and going back(backtracking) once it reach an already visited node or dead end, hence creating a perfect maze. If the Perfect maze is set to false it will then start opening wall to create a non-perfect maze.

Due to the amount of information found online and examples found on youtube we thought it would be the best option to generate mazes.

**Code Reusability**

The module 'mazegen' is capable of generating a perfect(or non-perfect) maze, display it and write the output file needed. By running make build, 'mazegen' will be made a package that can later be installed using pip and used for later project. 

**Project Management**

Initially the project was divided, Marco worked on parsing the config.txt file and handling error, while Joel worked on the maze algorithm, then it was programmed that on wednesdays we were going to work together and the first thing we worked on was displaying the maze. However this brought a challenge that was that both working on the same task created some discrepancies on the code so we solved that by working in a 'relay race' format by picking up work where the other left it. We finished the project with that management and in that way we ensured we were all clear in every aspect of the code. We recognized that we could improve in better time management that could have helped us finish the project earlier. Besides AI for debugging purposes and providing useful information (like ANSI color tables) no additional tool was used for this project.