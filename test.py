import unittest
from life import GameOfLife
from scene import Scene

class TestGameLife(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_game_of_life_is_not_none(self):
        gl = GameOfLife("casethreealiveneighbours.txt")
        self.assertIsNotNone(gl)

    def test_game_of_life_has_loaded_initial_values(self):
        gl = GameOfLife("casethreealiveneighbours.txt")
        self.assertEqual("........", "".join(gl.scene.grid[0]))
        self.assertEqual("....*...", "".join(gl.scene.grid[1]))
        self.assertEqual("...**...", "".join(gl.scene.grid[2]))
        self.assertEqual("........", "".join(gl.scene.grid[3]))

    def test_dead_cell_with_three_alive_neighbours_will_live(self):
        gl = GameOfLife("casethreealiveneighbours.txt")
        next_generation = gl.next()
        self.assertEqual("........", "".join(next_generation[0]))
        self.assertEqual("...**...", "".join(next_generation[1]))
        self.assertEqual("...**...", "".join(next_generation[2]))
        self.assertEqual("........", "".join(next_generation[3]))

    def test_alive_cell_with_two_or_three_alive_neighbours_will_live(self):
        gl = GameOfLife("casetwoorthreealiveneighbours.txt")
        next_generation = gl.next()
        self.assertEqual("........", "".join(next_generation[0]))
        self.assertEqual("......*.", "".join(next_generation[1]))
        self.assertEqual("......*.", "".join(next_generation[2]))
        self.assertEqual("......*.", "".join(next_generation[3]))


    def test_alive_cell_with_less_of_two_alive_neighbours_will_dead(self):
        gl = GameOfLife("caselessoftwoaliveneighbourswilldead.txt")
        next_generation = gl.next()
        self.assertEqual("........", "".join(next_generation[0]))
        self.assertEqual("......*.", "".join(next_generation[1]))
        self.assertEqual("......*.", "".join(next_generation[2]))
        self.assertEqual("......*.", "".join(next_generation[3]))
        pass
    def test_alive_cell_with_more_than_three_alive_neighbours_will_dead(self):
        gl = GameOfLife("casemorethanthreealiveneighbourswilldead.txt")
        next_generation = gl.next()
        self.assertEqual("*.*.....", "".join(next_generation[0]))
        self.assertEqual("*.*...*.", "".join(next_generation[1]))
        self.assertEqual(".**...*.", "".join(next_generation[2]))
        self.assertEqual("......*.", "".join(next_generation[3]))
        pass

    def test_final(self):
        gl = GameOfLife("casemorethanthreealiveneighbourswilldead.txt")
        next_generation = gl.next()
        print(next_generation)
        for i in range(30):
            scene = Scene()
            scene.grid = next_generation
            scene.rows = 4
            scene.cols = 8
            gl.scene = scene
            next_generation = gl.next()
            print(next_generation)

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
