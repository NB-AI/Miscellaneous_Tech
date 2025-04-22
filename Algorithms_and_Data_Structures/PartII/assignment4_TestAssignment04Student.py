import unittest

from Graph import Graph
from Vertex import My_Vertex


class TestAssignment04Student(unittest.TestCase):

    def test_insert_vertex(self):
        map = Graph()
        test = My_Vertex("Linz")

        linz = map.insert_vertex(test)

        self.assertEqual(test, map.get_vertices()[linz])

    def test_get_edges(self):
        map = Graph()
        linz = map.insert_vertex(My_Vertex("Linz"))
        wien = map.insert_vertex(My_Vertex("Wien"))
        graz = map.insert_vertex(My_Vertex("Graz"))

        map.insert_edge(linz, wien, 100)
        test = map.get_edges()

        self.assertEqual(1, len(test))
        self.assertTrue(wien == test[0].vertex_in or wien == test[0].vertex_out)
        self.assertTrue(test[0].vertex_in != test[0].vertex_out)
#        self.assertTrue(linz, test[0].vertex_out or linz == test[0].vertex_in) # false, correction:
        self.assertTrue(linz == test[0].vertex_out or linz == test[0].vertex_in)
        self.assertEqual(100, test[0].weight)

        map.insert_edge(wien, graz, 50)
        test = map.get_edges()

        self.assertEqual(2, len(test))

        self.assertTrue(graz == test[1].vertex_in or graz == test[1].vertex_out)
        self.assertTrue(test[1].vertex_in != test[1].vertex_out)
        self.assertTrue(wien, test[1].vertex_out or wien == test[1].vertex_in)
        self.assertEqual(50, test[1].weight)

    def test_get_vertices(self):
        g = self.init_graph_2_components()
        v = g.get_vertices()

        self.assertTrue(v[0].to_string() == "Linz")
        self.assertTrue(v[1].to_string() == "St.Poelten")
        self.assertTrue(v[2].to_string() == "Wien")
        self.assertTrue(v[3].to_string() == "Innsbruck")
        self.assertTrue(v[4].to_string() == "Bregenz")
        self.assertTrue(v[5].to_string() == "Eisenstadt")
        self.assertTrue(v[6].to_string() == "Graz")
        self.assertTrue(v[7].to_string() == "Klagenfurt")
        self.assertTrue(v[8].to_string() == "Salzburg")

    """Tests example 2"""

    def test_is_connected(self):
        g = self.init_graph_2_components()
        self.assertFalse(g.is_connected())

    def test_print_components(self):
        print("\n- Test1: ")
        g = self.init_graph_2_components()
        print("Expected: \n"
              + "[Linz] [Wien] [Eisenstadt] [Graz] [Klagenfurt] [Innsbruck] [Bregenz] [Salzburg]\n"
              + "[St.Poelten] [London]\n"
              + "Student result: ")
        g.print_components()

    """Helper functions"""

    def init_graph_2_components(self):
        map = Graph()

        linz = map.insert_vertex(My_Vertex("Linz"))

        stpoelten = map.insert_vertex(My_Vertex("St.Poelten"))

        wien = map.insert_vertex(My_Vertex("Wien"))

        innsbruck = map.insert_vertex(My_Vertex("Innsbruck"))

        bregenz = map.insert_vertex(My_Vertex("Bregenz"))

        eisenstadt = map.insert_vertex(My_Vertex("Eisenstadt"))

        graz = map.insert_vertex(My_Vertex("Graz"))

        klagenfurt = map.insert_vertex(My_Vertex("Klagenfurt"))

        salzburg = map.insert_vertex(My_Vertex("Salzburg"))

        map.insert_edge(linz, wien, 1)
        map.insert_edge(wien, eisenstadt, 2)
        map.insert_edge(wien, graz, 3)
        map.insert_edge(graz, klagenfurt, 4)
        map.insert_edge(bregenz, innsbruck, 5)
        map.insert_edge(klagenfurt, innsbruck, 6)
        map.insert_edge(salzburg, innsbruck, 7)

        london = map.insert_vertex(My_Vertex("London"))

        map.insert_edge(stpoelten, london, 10)

        return map


if __name__ == '__main__':
    unittest.main()
