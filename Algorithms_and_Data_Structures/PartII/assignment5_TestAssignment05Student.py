import unittest

from Roadmap import Roadmap
from Vertex import My_Vertex
from Station import Station


class TestAssignment05Student(unittest.TestCase):

    map = None
    linz= stpoelten= wien= innsbruck= bregenz= eisenstadt= graz= klagenfurt= salzburg= washington= 0

    def setUp(self):
        self.map = Roadmap()
        self.linz = self.map.insert_vertex(Station("Linz"))
        self.stpoelten = self.map.insert_vertex(Station("St.Poelten"))
        self.wien = self.map.insert_vertex(Station("Wien"))
        self.innsbruck = self.map.insert_vertex(Station("Innsbruck"))
        self.bregenz = self.map.insert_vertex(Station("Bregenz"))
        self.eisenstadt = self.map.insert_vertex(Station("Eisenstadt"))
        self.graz = self.map.insert_vertex(Station("Graz"))
        self.klagenfurt = self.map.insert_vertex(Station("Klagenfurt"))
        self.salzburg = self.map.insert_vertex(Station("Salzburg"))
        self.washington = self.map.insert_vertex(Station("Washington"))

        self.map.insert_edge(self.linz, self.stpoelten, 140)
        self.map.insert_edge(self.stpoelten, self.wien, 80)
        self.map.insert_edge(self.linz, self.wien, 200)
        self.map.insert_edge(self.wien, self.eisenstadt, 100)
        self.map.insert_edge(self.wien, self.graz, 190)
        self.map.insert_edge(self.graz, self.klagenfurt, 160)
        self.map.insert_edge(self.klagenfurt, self.salzburg, 210)
        self.map.insert_edge(self.linz, self.salzburg, 150)
        self.map.insert_edge(self.salzburg, self.innsbruck, 250)
        self.map.insert_edge(self.klagenfurt, self.innsbruck, 300)
        self.map.insert_edge(self.bregenz, self.innsbruck, 200)


    def test_wien_bregenz(self):
        print("Test: from Wien to Bregenz")
        print("-----------------------------")
        print("Output solution: ")
        print("Shortest distance from Wien to Bregenz: 800")
        print("    over Linz: 200")
        print("    over Salzburg: 350")
        print("    over Innsbruck: 600")
        print("    to Bregenz: 800")
        print("-----------------------------")

        print("Your output: ")
        res = self.map.print_shortest_distance(self.wien, self.bregenz)
        self.assertEqual(0, res[0][1])
        self.assertEqual("Wien", res[0][0])
        self.assertEqual(200, res[1][1])
        self.assertEqual("Linz", res[1][0])
        self.assertEqual(350, res[2][1])
        self.assertEqual("Salzburg", res[2][0])
        self.assertEqual(600, res[3][1])
        self.assertEqual("Innsbruck", res[3][0])
        self.assertEqual(800, res[len(res)-1][1])
        self.assertEqual("Bregenz", res[len(res)-1][0])
        print("-----------------------------")


    def test_innsbruck_eisenstadt(self):
        print("Test: from Innsbruck to Eisenstadt")
        print("-----------------------------")
        print("Output solution: ")
        print("Shortest distance from Innsbruck to Eisenstadt: 700")
        print("    over Salzburg: 250")
        print("    over Linz: 400")
        print("    over Wien: 600")
        print("    to Eisenstadt: 700")
        print("-----------------------------")
        print("Your output: ")
        res = self.map.print_shortest_distance(self.innsbruck,self.eisenstadt)
        self.assertEqual(0, res[0][1])
        self.assertEqual("Innsbruck", res[0][0])
        self.assertEqual(250, res[1][1])
        self.assertEqual("Salzburg", res[1][0])
        self.assertEqual(400, res[2][1])
        self.assertEqual("Linz", res[2][0])
        self.assertEqual(600, res[3][1])
        self.assertEqual("Wien", res[3][0])
        self.assertEqual(700, res[len(res)-1][1])
        self.assertEqual("Eisenstadt", res[len(res)-1][0])
        print("-----------------------------")


    def test_wien_klagenfurt(self):
        print("Test: from Wien to Klagenfurt")
        print("-----------------------------")
        print("Output solution: ")
        print("Shortest distance from Wien to Klagenfurt: 350")
        print("    over Graz: 190")
        print("    to Klagenfurt: 350")
        print("-----------------------------")
        print("Your output: ")
        res = self.map.print_shortest_distance(self.wien,self.klagenfurt)
        self.assertEqual(0, res[0][1])
        self.assertEqual("Wien", res[0][0])
        self.assertEqual(190, res[1][1])
        self.assertEqual("Graz", res[1][0])
        self.assertEqual(350, res[len(res)-1][1])
        self.assertEqual("Klagenfurt", res[len(res)-1][0])
        print("-----------------------------")

    def test_all_distances(self):
        distances = self.map.print_shortest_distances(self.wien)

        self.assertEqual(200, distances[self.linz])
        self.assertEqual(80, distances[self.stpoelten])
        self.assertEqual(0, distances[self.wien])
        self.assertEqual(600, distances[self.innsbruck])
        self.assertEqual(800, distances[self.bregenz])
        self.assertEqual(100, distances[self.eisenstadt])
        self.assertEqual(190, distances[self.graz])
        self.assertEqual(350, distances[self.klagenfurt])
        self.assertEqual(350, distances[self.salzburg])
        self.assertEqual(-1, distances[self.washington])


if __name__ == '__main__':
    unittest.main()
