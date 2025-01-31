class Game:
    def __init__(self, board_type=1):
        print("Game way to creating...")
        self.create_board(board_type)
        self.path = []  # To store the path taken

    def create_board(self, board_type):
        # ... (board configurations as before)

        if board_type == 1:
            self.gameBoard = [
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                [-1, 0,-1,-1,-1,-1,-1,-1, 0,-1],
                [-1, 0,-1, 0, 0, 0, 0,-1, 0,-1],
                [-1, 0,-1, 0,-1,-1,-1, 0, 0,-1],
                [-1, 0,-1, 0,-1, 0, 0, 0,-1,-1],
                [-1, 0,-1, 0, 0, 0,-1,-1,-1,-1],
                [-1, 0, 0, 0,-1,-1, 0, 0, 0,-1],
                [-1,-1,-1,-1,-1,-1,-1, 0, 2,-1],  # End point (2)
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]    
            ]
            self.start = (1, 1)
            self.end = (8, 8)  # Define end here

        elif board_type == 2:
            self.gameBoard = [
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                [-1, 1, 0, 0, 0, 0, 0, 0, 0, -1],  # Start point (1)
                [-1, 0, -1, 0, -1, -1, -1, 0, -1, -1],
                [-1, 0, -1, 0, 0, 0, 0, 0, -1, -1],
                [-1, 0, -1, -1, -1, -1, -1, 0, -1, -1],
                [-1, 0, 0, 0, 0, 0, 0, 0, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1],
                [-1, 0, 0, 0, 0, 0, 0, 0, -1, -1],
                [-1, 0, 0, 0, 0, 0, 0, 2, -1, -1],  # End point (2)
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            ]
            self.start = (1, 1)
            self.end = (8, 7)  # Define end here

        # Add more board types (elif board_type == 3:, etc.) as needed

        self.gameBoard[self.start[0]][self.start[1]] = 1  # Start is always 1

    def is_valid(self, row, col):
        return 0 <= row < 10 and 0 <= col < 10 and self.gameBoard[row][col] != -1

    def dfs(self, row, col):
        if (row, col) == self.end:
            self.path.append((row, col))  # Add the end to the path
            return True

        if not self.is_valid(row, col) or (row, col) in self.path:  # Check if valid and not visited
            return False

        self.path.append((row, col))  # Add current cell to path
        self.gameBoard[row][col] = 3 # Mark as visited in path

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if self.dfs(new_row, new_col):  # Explore neighbors
                return True

        self.path.pop()  # Backtrack: remove from path if no solution found
        return False

    def print_board_with_path(self):
        for row in range(10):
            for col in range(10):
                print(self.gameBoard[row][col], end=" ")
            print()



if __name__ == "__main__":
    game1 = Game(1)
    if game1.dfs(game1.start[0], game1.start[1]):  # Start DFS from the start
        print("Path found:")
        game1.print_board_with_path()

    else:
        print("No path found.")

    game2 = Game(2)
    if game2.dfs(game2.start[0], game2.start[1]):
        print("\nGame 2:")
        game2.print_board_with_path()
    else:
        print("\nGame 2:")
        print("No path found.")