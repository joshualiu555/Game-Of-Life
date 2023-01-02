# Game-Of-Life
A Python / Pygame simulation of Conway's Game of Life

The entire simulation runs on a Program Class. Once an instance is initialized, the program creates a new board. Each cell is its own class and is able to change states. 
Once initialized, the program object begins an infinite while loop until the user exits the program.

There is a 2D Grid of cells. Each cell checks its 4 neighbors. 

1) Every live cell with 2 or 3 neighbors lives on.
2) Every live cell with 4 neighbors dies due to overpopulation.
3) Every live cell with 1 neighbor dies due to underpopulation.
4) Every dead cell with 3 neighbors is reborn due to reproduction.

<img width="481" alt="Screen Shot 2023-01-02 at 4 25 03 PM" src="https://user-images.githubusercontent.com/53412192/210281828-762512ce-5a9e-40a6-a653-7eef12620b32.png">
