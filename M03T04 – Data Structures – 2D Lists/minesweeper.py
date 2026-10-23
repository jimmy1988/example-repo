#Declare the size of the grid
rows = 5
cols = 5

blank_symbol = "-" # What the blank symbol is
mine_symbol = "#" # What the mine symbole is

# START OF COUNT MINES

def count_mines(grid = []) -> list:

    """
    Counts the number of mines in the grid.
    Args:
        grid (list): The grid to evaluate

    Returns:
        list: The mines
    """

    grid_counts = [] # Initialize the counts

    #Check that the grid is filled in before proceeding
    if len(grid) == 0 or len(grid) < rows:
        print(f"The grid must be filled in and have rows equal to {rows}")
        return grid_counts
    else:

        #loop around each row to scan for mines
        #Scan in the horizontal, vertical and adjacent positions
        for i, row in enumerate(grid):

            #check that the row is filled in
            if len(row) == 0 or len(row) < cols:
                print(f"Row {i}  must be filled and have items equal to {cols}")

            else:

                new_row = [] # start a new row for the counts
                for j, cell in enumerate(row):
                    total_mines = 0 # default the total mine to 0

                    # if the current cell has a mine within it, set the count to a mine
                    if cell == mine_symbol:
                        total_mines = mine_symbol

                    else:

                        #check that the row before it is not out of bounds, below the 0 index
                        if i-1 >= 0:

                            #scan the previous row, for mines in the adjacent and vertical positions
                            if j-1 >= 0 and grid[i-1][j-1] == mine_symbol : total_mines += 1
                            if grid[i-1][j] == mine_symbol : total_mines += 1
                            if j+1 <= len(row)-1 and grid[i-1][j+1] == mine_symbol : total_mines += 1

                        #scan the current row
                        if j-1 >= 0 and grid[i][j-1] == mine_symbol : total_mines += 1
                        if j+1 <= len(row)-1 and grid[i][j+1] == mine_symbol : total_mines += 1

                        #check the next row, if its out of bounds, above the index of the length of the grid
                        if i+1 < (len(grid)-1):

                            #scan the next row, for mines
                            if j-1 >= 0 and grid[i+1][j-1] == mine_symbol : total_mines += 1
                            if grid[i+1][j] == mine_symbol : total_mines += 1
                            if j+1 <= len(row)-1 and grid[i+1][j+1] == mine_symbol : total_mines += 1

                    new_row.append(total_mines) # append the total to the row

                grid_counts.append(new_row) # append the row to the total counts

    #return the grid counts
    return grid_counts


# END OF COUNT MINES

# START OF SET UP GRID

def set_up_grid(option = 1):

    # convert the option to an integer
    option = int(option)

    if option == 1:

        #The preset grid
        grid = [
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"]
        ]

    else:

        #Empty grid for a custom grid
        grid = []

        #Get the input from the user to fill all the cells and rows with blanks and mines
        for i in range(rows):
            row = []
            for j in range(cols):

                while True:
                    try:
                        # Get the value from the user
                        value = input(f"Please enter either a mine({mine_symbol}) or a blank space ({blank_symbol}) for row {i + 1}, column {j + 1}: ").strip()

                        if value == mine_symbol or value == blank_symbol:
                            row.append(value) # append the value to the end if the row
                            break

                        else:
                            print("Please enter either a mine(#) or a blank space (-)")
                    except ValueError:
                        print("Please enter either a mine(#) or a blank space (-)")

            grid.append(row) # append each row onto the end of the grid

    #return the frid
    return grid

# END OF SET UP GRID

# START OF MAIN PROGRAM

while True:

    # Get the users option
    user_option = input("Would you like to (1) use a preset grid or (2) input a custom grid, (q) to quit?: ")

    # end the program when the user enters q
    if user_option == "q":
        break

    else:
         try:
             user_option = int(user_option) # convert the option to an integer

             # check for a valid option and pass in the value
             if 1 == user_option == 2:
                 grid = set_up_grid(user_option)
                 print(count_mines(grid))
                 continue

             else:
                 #invalid options will ask for input again
                 print("Please enter a valid option")
                 continue

         except ValueError:
             # If the option is not an integer then display a message
             print("Please enter either a valid input")
             continue


# END OF MAIN PROGRAM

