from scene import Scene

class GameOfLife:

    def __init__(self, filename):
        self.scene = Scene(filename)

    def next(self):
        threeneighbours = 0
        next_generation = [["." for x in range(self.scene.cols)] for x in range(self.scene.rows)]
        for i in range(self.scene.rows):
            for j in range(self.scene.cols):
                if self.are_more_than_three_neighbours_alive_and_im_alive(i, j):
                    next_generation[i][j] = "."
                    continue
                    
                if self.are_three_neighbours_alive_and_im_dead(i, j):
                    next_generation[i][j] = "*"
                    continue

                if self.are_two_or_three_alive_neighbours_and_im_alive(i, j):
                    next_generation[i][j] = "*"
                    continue


                next_generation[i][j] = "."
        return next_generation

    def are_three_neighbours_alive_and_im_dead(self, i, j):
        if self.get_neighbours_alive(i, j) == 3 and self.scene.grid[i][j] == ".":
            return True
        return False

    def are_two_or_three_alive_neighbours_and_im_alive(self, i, j):
        if 2 <= self.get_neighbours_alive(i, j) <= 3 and self.scene.grid[i][j] == "*":
            return True
        return False

    def are_more_than_three_neighbours_alive_and_im_alive(self, i, j):
        if self.get_neighbours_alive(i, j) > 3 and self.scene.grid[i][j] == "*":
            return True
        return False


    def get_neighbours_alive(self, row, col):
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        alives = 0
        for neighbour in neighbours:
            if self.is_out_of_top_rows(row, neighbour) or self.is_out_of_bottom_rows(row, neighbour): continue
            if self.is_out_of_left_cols(col, neighbour) or self.is_out_of_right_cols(col, neighbour): continue

            final_row = row + neighbour[0]
            final_col = col + neighbour[1]
            if self.scene.grid[final_row][final_col] == "*":
                alives += 1

        return alives

    def is_out_of_top_rows(self, row, neighbour):
        if (row + neighbour[0]) < 0: return True
        return False

    def is_out_of_bottom_rows(self, row, neighbour):
        if (row + neighbour[0]) >= self.scene.rows: return True
        return False

    def is_out_of_left_cols(self, col, neighbour):
        if (col + neighbour[1]) < 0: return True
        return False

    def is_out_of_right_cols(self, col, neighbour):
        if (col + neighbour[1]) >= self.scene.cols: return True
        return False
