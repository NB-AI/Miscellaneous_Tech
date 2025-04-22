from random import random
import numpy as np
from rectangle import Rectangle

class MonteCarlo:

    def __init__(self, length, width, rectangles):
        """constructor
        :param length - length of the enclosing rectangle
        :param width - width of the enclosing rectangle
        :param rectangles - array that contains the embedded rectangles
        :raises ValueError if any of the paramters is None
        """

        if length == None or width == None or rectangles == None:
            raise ValueError('Invalid input values!')

        self.length = int(length)
        self.width = int(width)
        self.rectangles = rectangles

        # Firstly, generate the big rectangle which consists only of 0s:
        self.big_rec_array = np.zeros((self.width, self.length), dtype=int) # dtype could be also bool




    def area(self, num_of_shots):
        """Method "area "to estimate the area of the enclosing rectangle that is not covered by the embedded rectangles
        :param num_of_shots - Number (>0) of generated random points whose location (inside/outside) is analyzed
        :return float
        :raises ValueError if any of the paramters is None
        """
        if num_of_shots == None:
            raise ValueError('Invalid input values!')

        elif self.rectangles == []:
            return self.length*self.width

        big_rec_array1 = self.big_rec_array

        # Change the values of the big rectangle by putting in the extended small rectangles:
        # self.rectangles is array that contains small rectangles. This array like list with elements.
        # --> Split up big array into smaller arrays:
        for small_rec in self.rectangles:
            # Create instances of the class Rectangle with the list 'rectangles' filled up with Rectangle objects:
            single_object = small_rec.call()
            origin_length, origin_width, small_rec_array, small_rec_length, small_rec_width = single_object[0], single_object[
                1], single_object[2], single_object[3], single_object[4]
            #origin_length, origin_width, small_rec_array, small_rec_length, small_rec_width = small_rec[0], small_rec[1], small_rec[2], small_rec[3], small_rec[4]

            extended_small_rec = np.pad(small_rec_array, ((origin_width, (self.width - origin_width - small_rec_width)),
                                                          (origin_length,
                                                           (self.length - origin_length - small_rec_length))),
                                        mode='constant', constant_values=(0, 0))
            # first (number empty lines above array, number empty lines under array),
            # second (number empty columns left of array, number empty columns right of array)

            # Combine big rectangle array with extended small rectangle array:
            big_rec_array1 += extended_small_rec  # Everywhere where small rectangle is a 1 is added to the element of the big rectangle


        # Firstly, generate the random points num_of_shots times:
        counter = 1
        number_outside_small = 0
        while counter < num_of_shots:
            # Generate the scaled points:
            coordinate_pt = (int((random()*self.length)), int((random()*self.width))) # (x,y)

            # Look if a point is inside a small rectangle: # ??? Big rectangle array produzierung verschieben!!!!!!!!!!
            if big_rec_array1[coordinate_pt[1]][coordinate_pt[0]] == 0: # then the point is outside a small rectangle
                number_outside_small += 1

            counter += 1
        estimated_area = float(((self.length*self.width)*number_outside_small)/num_of_shots) # =(area_big_rectangle*number_hits/total_number_of_points
        return estimated_area


    def inside(self, x, y, rect):
        """Method "inside" to determine if a given point (x,y) is inside a given rectangle
        :param x,y - coordinates of the point to check
        :param rect - given rectangle
        :return bool
        :raises ValueError if any of the paramters is None
        """
        if x == None or y == None or rect == None:
            raise ValueError('Invalid input values!')

        elif rect == []:
            return False

        big_rec_array2 = np.zeros((self.width, self.length), dtype=int)

        # Change the values of the big rectangle by putting in the extended small rectangles:
        # self.rectangles is array that contains small rectangles. This array like list with elements.
        # --> Split up big array into smaller arrays:
        single_object = rect.call()
        origin_length, origin_width, small_rec_array, small_rec_length, small_rec_width = single_object[0], \
                                                                                          single_object[
                                                                                              1], single_object[2], \
                                                                                          single_object[3], \
                                                                                          single_object[4]
       # origin_length, origin_width, small_rec_array, small_rec_length, small_rec_width = rect[0], rect[1], rect[2], rect[3], rect[4]
        extended_small_rec = np.pad(small_rec_array, ((origin_width,(self.width-origin_width-small_rec_width)) ,
                                                      (origin_length, (self.length-origin_length-small_rec_length))), mode = 'constant', constant_values=(0, 0))
        # first (number empty lines above array, number empty lines under array),
        # second (number empty columns left of array, number empty columns right of array)

        # Combine big rectangle array with extended small rectangle array:
        big_rec_array2 += extended_small_rec # Everywhere where small rectangle is, 1 is added to the element of the big rectangle


        # Have a look if the point is within the rectangle:
        if big_rec_array2[int(y)][int(x)] > 0:
            return True
        else:
            return False