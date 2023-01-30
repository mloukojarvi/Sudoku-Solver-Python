import math

def read_puzzle():
    '''Reads in the puzzle from a text file "puzzle.txt" and stores it in a list'''

    puzzle = []
    f = open('puzzle.txt', 'r')
    
    for row in f:
        puzzle.append(list(map(int, row.split())))
    f.close()

    return puzzle


def write_solution(puzzle):
    '''Writes the solved puzzle into a text file "solution.txtx" '''
    
    f = open('solution.txt', 'w')

    for row in puzzle:
        f.write(" ".join(str(n) for n in row) + "\n")
    f.close()


def next_empty(puzzle):
    '''Finds the next empty cell and returns the corresponding coordinates.
    If the puzlle is filled, returns a tuple of Nones'''
    
    dim = len(puzzle) # dimension of the puzzle
    
    for row in range(dim):
        for col in range(dim):
            if puzzle[row][col] == 0:
                return row, col
            
    return None, None


def is_valid(puzzle, guess, row, col):
    '''Checks if adding the guess to the given coordinates in the puzzle
    would lead to a new valid puzzle'''
    
    dim = len(puzzle) # dimension of the whole puzzle
    cont_dim = int(math.sqrt(dim)) #dimension of each container

    # Check if the guess already is in the row or the column
    if guess in puzzle[row]:
        return False
    if guess in [puzzle[n][col] for n in range(dim)]:
        return False

    # The coordinates of the top-left cell of the guesse's container
    cont_row = row//cont_dim*cont_dim
    cont_col = col//cont_dim*cont_dim

    # Check if the guess already is in the container
    for r in range(cont_row, cont_row + cont_dim):
        for c in range(cont_col, cont_col + cont_dim):
            if guess == puzzle[r][c]:
                return False

    return True


def solve(puzzle):
    '''Solves the sudoku puzzle given as input. Returns True
    if it can be solved, otherwise returns False'''
    
    # Find the next empty cell
    row, col = next_empty(puzzle)

    # Check if the puzzle is already full and solved
    if row is None:
        return True

    # Make a guess for the value of the empty cell and check its validity
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            # If the guess is valid, continue guessing recursively
            if solve(puzzle):
                return True

        # Reset the last guess in the stack if it leads to an invalid puzzle
        puzzle[row][col] = 0

    # If reached, no solution can be found for the original puzzle
    return False


def main():
    puzzle = read_puzzle()
    solved = solve(puzzle)

    if solved:
        write_solution(puzzle)
        print("Solved!")
    else:
        print("No solution could be found")
    
if __name__ == "__main__":
    main()
