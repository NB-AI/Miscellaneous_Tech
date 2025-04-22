class My_Maze:
    def __init__(self, new_maze=None):
        import numpy as np
        np.asarray(new_maze)
        self._maze = new_maze

        deep = 0
        self._depth = deep
        self._depthstart = None
        self.x_start = None
        self.y_start = None

    # helping methods for coordination through maze:
    # indirect recursion
    def right(self, x, y, depth):
        self._maze[x][y + 1] = '.'
        y += 1
        depth += 1
        call_maze = My_Maze(self._maze)
        call_maze.find_exits(x, y, depth)

    def left(self, x, y, depth):
        self._maze[x][y - 1] = '.'
        y -= 1
        depth += 1
        call_maze = My_Maze(self._maze)
        call_maze.find_exits(x, y, depth)

    def up(self, x, y, depth):
        self._maze[x - 1][y] = '.'
        x -= 1
        depth += 1
        call_maze = My_Maze(self._maze)
        call_maze.find_exits(x, y, depth)

    def down(self, x, y, depth):
        self._maze[x + 1][y] = '.'
        x += 1
        depth += 1
        call_maze = My_Maze(self._maze)
        call_maze.find_exits(x, y, depth)


    def find_exits0(self, x, y, depth): # this function is used by other functions

        # if clauses to set an X instead of a .
        if self._maze[x][y+1] == '' and self._maze[x][y] == '.': # replace right . by X
            self._maze[x][y] = 'X'

        if self._maze[x][y-1] == '' and self._maze[x][y] == '.': # replace left . by X
            self._maze[x][y] = 'X'

        if self._maze[x - 1][y] == '' and self._maze[x][y] == '.':  # replace upper . by X
            self._maze[x][y] = 'X'

        if self._maze[x+1][y] == '' and self._maze[x][y] == '.': # replace lower . by X
            self._maze[x][y] = 'X'


        # if clauses of recursion; discover maze and set points:
        if self._maze[x][y+1] == ' ': # go right
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.right(x, y, depth)

        if self._maze[x][y - 1] == ' ':  # go left
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.left(x, y, depth)

        if self._maze[x-1][y] == ' ': # go up
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.up(x, y, depth)

        if self._maze[x+1][y] == ' ': # go down
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.down(x, y, depth)

        # when the maximal depth is reached the function should determine if there is an X in it:
        # first step: determine if the maze can walk further
        x_index2 = 0
        y_index2 = 0
        counter = 0 # shows if there are free fields
        for line in self._maze:
            for ele in line:
                if ele == '.' or ele == 'X' or ele == 'S':

                    if self._maze[x_index2][y_index2+1] == ' ':
                        counter += 1
                    elif self._maze[x_index2][y_index2-1] == ' ':
                        counter += 1
                    elif self._maze[x_index2+1][y_index2] == ' ':
                        counter += 1
                    elif self._maze[x_index2-1][y_index2] == ' ':
                        counter += 1
                y_index2 += 1
            x_index2 += 1
            y_index2 = 0

        # second step: when there aren't any free achievable fields you can check the array for exits:
        if counter == 0:
            string_exits = ''
            for line in self._maze:
                for ele in line:
                    if ele == 'X':
                        string_exits += 'X'
                    if ele == 'X' or ele == '.':
                        self._depth += 1 # get the maximal recursion depth
            # check if there is an exit in the final array
            if 'X' in string_exits:
                t = True
            else:
                t = False
            f = self._maze
            return t, f, counter, self._depth


    def find_exits(self, x, y, depth): # Is the same function as find_exits0 but only returns t
        """ Side note: I asked the lecturers and other students to understand what the sense of the input depth
        is. However, I don't understand it after all efforts."""
        if self.x_start == None:
            self.x_start = x
        if self.y_start == None:
            self.y_start = y
        if self._depthstart == None:
            self._depthstart = depth

        # get length of maze:
        length_maze = 0
        for ele in self._maze:
            length_maze += 1

        if depth == 0:
            import numpy as np
            new_maze_long = np.zeros(shape=(length_maze + 2, length_maze + 2), dtype=str)
            # Generate big array:
            xx = 0
            yy = 0
            for line in self._maze:
                for element in line:
                    new_maze_long[xx + 1][yy + 1] = self._maze[xx][yy]
                    yy += 1
                xx += 1
                yy = 0
            self._maze = new_maze_long

            # Set the S for start point:
            x += 1 # index has to be fitted to the new bigger array
            y += 1
            self._maze[x][y] = 'S'

        # if clauses to set an X instead of a .
        if self._maze[x][y+1] == '' and self._maze[x][y] == '.': # replace right . by X
            self._maze[x][y] = 'X'

        if self._maze[x][y-1] == '' and self._maze[x][y] == '.': # replace left . by X
            self._maze[x][y] = 'X'

        if self._maze[x - 1][y] == '' and self._maze[x][y] == '.':  # replace upper . by X
            self._maze[x][y] = 'X'

        if self._maze[x+1][y] == '' and self._maze[x][y] == '.': # replace lower . by X
            self._maze[x][y] = 'X'


        # if clauses of recursion; discover maze and set points:
        if self._maze[x][y+1] == ' ': # go right
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.right(x, y, depth)

        if self._maze[x][y - 1] == ' ':  # go left
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.left(x, y, depth)

        if self._maze[x-1][y] == ' ': # go up
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.up(x, y, depth)

        if self._maze[x+1][y] == ' ': # go down
            depth += 1
            call_maze = My_Maze(self._maze)
            call_maze.down(x, y, depth)


        # when the maximal depth is reached the function should determine if there is an X in it:
        # first step: determine if the maze can walk further
        x_index2 = 0
        y_index2 = 0
        counter = 0 # shows if there are free fields
        for line in self._maze:
            for ele in line:
                if ele == '.' or ele == 'X' or ele == 'S':

                    if self._maze[x_index2][y_index2+1] == ' ':
                        counter += 1
                    elif self._maze[x_index2][y_index2-1] == ' ':
                        counter += 1
                    elif self._maze[x_index2+1][y_index2] == ' ':
                        counter += 1
                    elif self._maze[x_index2-1][y_index2] == ' ':
                        counter += 1
                y_index2 += 1
            x_index2 += 1
            y_index2 = 0

        # second step: when there aren't any free achievable fields you can check the array for exits:
        if counter == 0:
            string_exits = ''
            for line in self._maze:
                for ele in line:
                    if ele == 'X':
                        string_exits += 'X'


            # check if there is an exit in the final array
            if 'X' in string_exits:
                t = True
            else:
                t = False

            return t


    def get_list_of_exits(self):
        call = My_Maze(self._maze)

        t, f, counter, self._depth = call.find_exits0(self.x_start,self.y_start,self._depthstart)

        # get length of f:
        length_f = 0
        for ele in f:
            length_f += 1

        # Because two arrays where combined to a bigger one through function call you have to shrink the size of
        # the array:
        # first step: delete not needed lines:
        import numpy as np
        x_index3 = 0
        smaller_arr = np.zeros(shape=(length_f - 2, length_f), dtype=str)
        for line in f:
            if x_index3 == length_f-1 or x_index3 == length_f-1:
                pass

            elif x_index3 < length_f-2 or x_index3 >= 1:
                smaller_arr[x_index3-1] = line

            x_index3 += 1

        # second step: shrink the size of each line:
        # Create the final array which has the size of the input array:
        final_arr = np.zeros(shape=(length_f - 2, length_f-2), dtype=str)
        x_index4 = 0
        y_index4 = 0
        for line in smaller_arr:
            for ele in line:
                if ele != '':
                    final_arr[x_index4][y_index4-1] = smaller_arr[x_index4][y_index4]
                y_index4 += 1
            x_index4 += 1
            y_index4 = 0

        self._maze = final_arr


        # get a list with the length of the number of X-es:
        counter = [] # will stay empty when there is no X in the array
        for line in self._maze:
            for ele in line:
                if ele == 'X':
                    counter += ['X']

        # get length counter
        length_counter = 0
        for ele in counter:
            length_counter += 1


        # replace the X-es in the list through the coordinates of the X-es:
        t = 0 # index for list "counter"
        y_index6 = 0
        x_index6 = 0

        for line in self._maze:
            for ele in line:
                if ele == 'X':
                    if t <= length_counter-1:
                        counter[t] = y_index6, x_index6

                        t += 1
                y_index6 += 1

            x_index6 += 1
            y_index6 = 0

        return counter




    def get_max_recursion_depth(self):
        call_maze = My_Maze(self._maze)
        t, f, counter, deep = call_maze.find_exits0(self.x_start,self.y_start,self._depthstart)

        return deep


