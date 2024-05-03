Introduction:

Welcome to the Puzzle Solver project! This software allows you to generate and solve Sudoku puzzles of varying difficulty levels. Whether you're a Sudoku enthusiast or a beginner, this solver provides a convenient way to play and challenge yourself.

Getting Started:

System Requirements:

 		  	Python 3.x installed on your system.

 		  	Basic understanding of the command line.
     
Installation:

 		  	Clone or download the project repository from https://github.com/sai460/AI_Final_Project.git
 	   
 		  	Navigate to the project directory in the terminal.
     
Install required dependencies using the following command:
 		•	pip install numpy matplotlib
  or	
 		•	pip3 install numpy matplotlib
Usage Instructions:

After successful installation, Let’s run the python file using the following command

 	python puzzle_solver_final.py			or
 	python3 puzzle_solver_final.py
 
Usage Instructions:

User will be prompted to enter the grid size i.e., either 4 or 9 as per standard of sudoku game. (Sudoku Board should contain a Square number nxn grid).
After entering the grid size (limited to 4 or 9), user will be asked to choose the level of difficulty like below: 

![image](https://github.com/ShaikMurthaza/Smartgrid-puzzle-solver/assets/47879123/387d1dd0-30f3-4e4c-9341-6e4aaecbff29)

After choosing the difficulty level, the program generates a Sudoku puzzle for you.

![image](https://github.com/ShaikMurthaza/Smartgrid-puzzle-solver/assets/47879123/31c99197-9a08-4e88-b6e6-a072a6638c5c)

 The puzzle is displayed on the console.
 The program will display the solved puzzle along with performance metrics, including time taken and backtracking information.

Performance Metrics: 
 ![image](https://github.com/ShaikMurthaza/Smartgrid-puzzle-solver/assets/47879123/ef313bed-7c42-414e-a76a-201d86355581)


Advanced Features:

 	Optimized Backtracking
 	The solver utilizes an optimized backtracking algorithm to efficiently solve Sudoku puzzles.
 	This optimization reduces the number of recursive calls and backtracks, improving overall performance.
 	
 	Performance Metrics
 	The solver provides performance metrics such as time taken, number of recursive calls and number of backtracks.
Troubleshooting:

 If you encounter issues, ensure that you have Python installed and the required dependencies are installed using pip.
 	Check for any error messages in the terminal for guidance.
