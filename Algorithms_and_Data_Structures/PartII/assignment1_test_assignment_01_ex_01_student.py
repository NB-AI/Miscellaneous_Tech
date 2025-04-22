import unittest

from montecarlo import MonteCarlo
from rectangle import Rectangle


class TestAssignment01ex01Student(unittest.TestCase):
    # my code:
    def test_my_mc_test(self):
        rectangle1 = Rectangle(1.0, 1.0, 3.0, 4.0)
        rectangle2 = Rectangle(4.0, 0.0, 5.0, 2.0)
        rectangle3 = Rectangle(4.0, 1.0, 2.0, 5.0)
        rectangle4 = Rectangle(6.0, 7.0, 4.0, 3.0)
        rectangle_list = []
        rectangle_list.append(rectangle1)
        rectangle_list.append(rectangle2)
        rectangle_list.append(rectangle3)
        rectangle_list.append(rectangle4)
        mc = MonteCarlo(10, 10, rectangle_list)

        area = mc.area(10)
        print("Area of two embedded four rectangles is " + str(area))
        self.assertTrue(area > -1 and area < 101)

        area = mc.area(100)
        print("Area of two embedded four rectangles is " + str(area))
        self.assertTrue(area > -1 and area < 101)

        area = mc.area(1000)
        print("Area of two embedded four rectangles is " + str(area))
        self.assertTrue(area > 10 and area < 80)

        area = mc.area(10000)
        print("Area of two embedded four rectangles is " + str(area))
        self.assertTrue(area > 40 and area < 60)

        area = mc.area(100000)
        print("Area of two embedded four rectangles is " + str(area))
        self.assertTrue(area > 45 and area < 60)

        # test the inside method:
        self.assertEqual(mc.inside(1.0, 1.0, rectangle1), True)
        self.assertEqual(mc.inside(9.0, 9.0, rectangle1), False)
        self.assertEqual(mc.inside(0.0, 9.0, rectangle4), False)


        # test if error raises:
        self.assertRaises(ValueError, mc.inside, 9.0, 9.0, None)
        self.assertRaises(ValueError, MonteCarlo, 10, None, rectangle_list)


    def test_monte_carlo_with_2_rects(self):
        """area if the enclosing rectangle is 50
        area of embedded rectangles = 2+12
        result is 50-14 = 36
        """
        rect1 = Rectangle(0.0, 0.0, 1.0, 2.0)
        rect2 = Rectangle(7.0, 1.0, 3.0, 4.0)
        rects = []
        rects.append(rect1)
        rects.append(rect2)

        mc = MonteCarlo(10, 5, rects)

        # my code:
        area = mc.area(10)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > -1 and area < 51)

        area = mc.area(100)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 51)

        area = mc.area(1000)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 45)

        area = mc.area(10000)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 40)


        area = mc.area(100000)      # for 10000 random points the estimated area should already be close to the correct result of 36
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 40)


        area = mc.area(100000)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 40)        # Run the algorithm 2 more times to see the differences in the estimation when using a randomized algorithm

        area = mc.area(100000)
        print("Area of two embedded rectangles (1x2 and 3x4) is " + str(area))
        self.assertTrue(area > 30 and area < 40)

    def test_monte_carlo_with_0_rects(self):
        """area of the enclosing rectangle is 50
        area of the embedded rectangles is 0
        """
        rects = []

        mc = MonteCarlo(10, 5, rects)
        area = mc.area(100000)
        self.assertEqual(area, 50)
        print("Area of no embedded rectangles is " + str(area))


if __name__ == '__main__':
    unittest.main()
