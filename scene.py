
class Scene:
    filename = None
    rows = 0
    cols = 0
    grid = None

    def __init__(self, filename=None):
        if filename is not None:
            self.filename = filename
            self._load_initial_values()


    def _load_initial_values(self):
        i = 0
        with open(self.filename, 'r+') as f:
            for line in f:
                line = line.rstrip('\n')
                if i is 0:
                    rows_and_cols = line.split(" ")
                    self.rows = int(rows_and_cols[0])
                    self.cols = int(rows_and_cols[1])
                    self.grid = [["."] * int(rows_and_cols[1]) ] * int(rows_and_cols[0])
                    i += 1
                else:
                    self.grid[i-1] = list(line)
                    i += 1
        f.close()
