from Vertex import My_Vertex
from Edge import My_Edge
import numpy as np

class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices in the graph
        self.edges = []     # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

        self.free_vertex = False
        self.no_name_index_vertex = 0 # can be an arbitrary number for initialistaion
        self.free_edge = False
        self.no_name_index_edge = 0 # can be an arbitrary number for initialistaion

        self.cycle = False
        self.already_visited = list(self.num_vertices * 'f')  # when all nodes are visited we know that graph is connected
        # 'f' stands for False/not visited

    def double_array_size(self):

        self.vertices = self.vertices.copy() + [My_Vertex()] * len(self.vertices) * 2
        self.edges = self.edges.copy() + [My_Edge()] * len(self.edges) * 2 * (len(self.edges) * 2 -1)


    def get_number_of_vertices(self):
        """return: the number of vertices in the graph
        """
        return self.num_vertices

    def get_number_of_edges(self):
        """return: the number of edges in the graph
        """
        return self.num_edges

    def get_vertices(self):
        """return: array of length get_number_of_vertices() with the vertices in the graph
        """
        # the self.vertices list contains already in the beginning a vertex with no name, therefore:
        # it also could be that some ele are empty:
        return self.vertices[:self.num_vertices]


    def get_edges(self):
        """return: array of length get_number_of_edges() with the edges in the graph
        """

        return self.edges[:self.num_edges] # self.num_edges is one value higher than index but when you slice like [:number]
        # that than the number itself is exculded: go only until the end of index number one smaller than number

    def insert_vertex(self, vertex):
        """Inserts a new vertex into the graph and returns its index in the vertex array.
	    If the vertex array is already full, then the method double_array_size() shall be called
	    before inserting.
        None parameter is not allowed (ValueError).
        :param vertex: the vertex to be inserted
        :return: index of the new vertex in the vertex array
        :raises: ValueError if any of the parameters is None
        """
        if vertex == None:
            raise ValueError('You tried to insert None')


        if len(self.vertices) == 0:
            self.vertices = [vertex]
            # self.vertices[0].name = vertex.name # We don't need that because in the class object vertex is the variable 'name' already memorized


        elif self.vertices[-1].name != '': # then the array is already full
            self.double_array_size() # now self.vertices and self.edges in len doubled with new vertices with names == ''

            self.vertices[self.num_vertices] = vertex # here we have the first new added element to the list

            if len(self.vertices) >= self.num_vertices + 1:
                self.no_name_index_vertex = self.num_vertices + 1
                self.free_vertex = True

        elif self.free_vertex == True:
            self.vertices[self.no_name_index_vertex] = vertex

            if len(self.vertices) > self.no_name_index_vertex + 1: # when there is also another element after the current insertion position
                # then it has to have the name '' and here we can insert the next time
                # self.free_vertex can stay true
                self.no_name_index_vertex += 1
            else: # the list is after the insertion of the current index full, therefore there exists no free position to insert next
                self.free_vertex = False

        else: # the list isn't full but we haven't checked for free vertices so far # the list is full
            for ind, ele in enumerate(self.vertices): # for loop has a higher time complexity. Therefore, we only use it, when the
                # other if-clauses aren't fulfilled
                if ele.name == '': # then insert here
                    self.vertices[ind] = vertex

        self.num_vertices += 1
        return self.num_vertices-1 # vertex always inserted in the last free position of self.vertices

    def has_edge(self, vertex1, vertex2):
        """Returns the edge weight if there is an edge between index vertex1 and vertex2, otherwise -1.
	    In case of unknown or identical vertex indices raise a ValueError.
        :param vertex1: first vertex
        :param vertex2: second vertex
        :return: edge weight of -1 if there is no edge
        :raises: ValueError if any of the parameters is None
        """
        if vertex1 == None or vertex2 == None:
            raise ValueError('You tried to find a None value')
        # first check if they have the same index in self.vertices:

        if isinstance(vertex1, My_Vertex):
            # Modify vertices to indices because we search for the indices in self.edges:
            try:
                vertex1 = self.vertices.index(vertex1)
                vertex2 = self.vertices.index(vertex2)
            except:
                raise ValueError('At least one of the given vertices doesn\'t exist.')

        ind1=None
        ind2=None
        for i, vertex in enumerate([vertex1, vertex2]):
            for ind, ele in enumerate(self.vertices):
                if ind == vertex: # argument vertices are only indices
                    if i == 0: # the vertex1 is the current vertex index
                        ind1 = ind
                    else: # the vertex2 is the current vertex
                        ind2 = ind

        if ind1 == None or ind2 == None: # The searched vertex doesn't exist in the graph
            raise ValueError('Searched vertex doesn\'t exist in the graph.')

        if ind1 == ind2:
            raise ValueError('There is no edge when the vertices are identical with the same position in the graph.')

        # Lets find the searched edge in the self.edges:
        for edge in self.edges:
            if (edge.vertex_in == ind1 and edge.vertex_out == ind2) or (edge.vertex_in == ind2 and edge.vertex_out == ind1):
                # vertex_in is an index
                return edge.weight

        return -1 # when we didn't found the corresponding edge

    def insert_edge(self, vertex1, vertex2, weight):
        """Inserts an edge between vertices with index of vertex1 and index of vertex2. False is returned if the edge already exists,
	    True otherwise. A ValueError shall be raised if the vertex indices are unknown (out of range) or
	    if v1 == v2 (loop).
        .
        .
        :param vertex1: first index of vertex
        :param vertex2: second index of vertex
        :param weight: weight of the edge
        :return: True if the edge could be created, False otherwise
        :raises: ValueError if any of the parameters is None any of the vertices is out of range
        """
        if vertex1 == None or vertex2 == None or weight == None:
            raise ValueError('You cannot use None arguments/parameters.')

        try:
            self.vertices[vertex1]# find the index of the given vertex in self.vertices
            self.vertices[vertex2]

        except: # searched vertices aren't in self.vertices
            raise ValueError('Searched vertices don\'t exist.')

        if vertex1 == vertex2: # We would have a loop
            raise ValueError('The vertices aren\'t allowed to have the same index position.')


        # Now let's check if there is already existing an edge between those vertices:
        maybe_weight = self.has_edge(vertex1, vertex2)

        if maybe_weight != -1: # -1 means that there was no edge found
            return False # When the edge already exists then we cannot insert it anymore --> return False

        else: # No existing edge found, therefore create one
            # Generate an class object of My_Edge because when you use def double_array size, the new added objects aren't
            # independent of each other; when I insert at one index also at other index change because we have the
            # exactly same class object. That's bad. Therefore:
            insert_edge = My_Edge()
            insert_edge.vertex_in = vertex1
            insert_edge.vertex_out = vertex2
            insert_edge.weight = weight

            # Firstly, find the index position in the self.vertices:
            # Modify the code from def insert_vertex a bit:
            if len(self.edges) == 0:

                self.edges = [insert_edge]


            elif self.edges[-1].weight != None:  # then the array is already full
                self.double_array_size()  # now self.vertices and self.edges in len doubled with new vertices with names == ''

                self.edges[self.num_edges] = insert_edge # the vertex_in, vertex_out and weight are already initialised for
                # the class_object insert_edge and therefore we don't have to fix it at the self.edges list position

                if len(self.edges) >= self.num_edges + 1:
                    self.no_name_index_edge = self.num_edges + 1
                    self.free_edge = True

            elif self.free_vertex == True:
                self.edges[self.no_name_index_edge] = insert_edge

                if len(
                        self.edges) > self.no_name_index_edge + 1:  # when there is also another element after the current insertion position
                    # then it has to have the name '' and here we can insert the next time
                    # self.free_vertex can stay true
                    self.no_name_index_edge += 1
                else:  # the list is after the insertion of the current index full, therefore there exists no free position to insert next
                    self.free_edge = False

            else:  # the list isn't full but we haven't checked for free vertices so far # the list is full

                for ind, ele in enumerate(
                        self.edges):  # for loop has a higher time complexity. Therefore, we only use it, when the
                    # other if-clauses aren't fulfilled
                    if ele.vertex_in == None:  # then insert here
                        self.edges[ind] = insert_edge

            self.num_edges += 1
            return True

    def get_adjacency_matrix(self):
        """Returns an NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains 1 if there is an edge at the corresponding index position, otherwise 0.
        :return: NxN adjacency matrix
        """
        dim = self.get_number_of_vertices()
        adjacency_matrix = np.zeros(shape=(dim, dim))

        # Go thourgh self.edges to find the indices which are adjacent
        for edge in self.edges:
            if edge.vertex_in == None:
                break

            ind1 = edge.vertex_in
            ind2 = edge.vertex_out

            adjacency_matrix[ind1][ind2] = 1
            adjacency_matrix[ind2][ind1] = 1

        return adjacency_matrix


    def get_adjacent_vertices(self, vertex):
        """Returns an array of vertices which are adjacent to the vertex with index "vertex".
        :param vertex: The vertex of which adjacent vertices are searched.
        :return: array of adjacent vertices to "vertex".
        :raises: ValueError if the vertex index "vertex" is unknown
        """
        if vertex == None:
            raise ValueError('You cannot use None arguments/parameters.')

        try:
            ind_in_vertices = self.vertices.index(vertex) # find the index of the given vertex in self.vertices

        except: # searched vertices aren't in self.vertices
            raise ValueError('Searched vertex doesn\'t exist.')

        # Search for the adjacent vertices and add them to an array/list:
        adjacent_list = []

        for edge in self.edges:
            if edge.vertex_in != None:

                if edge.vertex_in == ind_in_vertices:
                    adjacent_list.append(self.vertices[edge.vertex_out])

                elif edge.vertex_out == ind_in_vertices:
                    adjacent_list.append(self.vertices[edge.vertex_in])

            # There will only come None, therefore break:
            else:
                break

        return adjacent_list

    # ------------- """Example 2""" -------------

    def is_connected(self):
        """return: True if the graph is connected, otherwise False.
        """
        """
        if len(self.edges) > 0:
            if self.edges[0].vertex_in != None:
                return True # it es enough when there is only one edge

        return False"""
        self.already_visited = list(self.num_vertices * 'f')
        self.DFS(0, 0)

        if 'f' in self.already_visited:
            return False
        return True

    def get_number_of_components(self):
        """return: The number of all (weak) components
        """
        number_components = 0
        self.already_visited = list(self.num_vertices * 'f')

        while 'f' in self.already_visited:
            number_components += 1
            first_not_visited_index = self.already_visited.index('f') # that function chooses the first found object in a list
            self.DFS(first_not_visited_index, first_not_visited_index)

        return number_components

    def print_components(self):
        """Prints the vertices of all components (one line per component).
        E.g.: A graph with 2 components (first with 3 vertices, second with 2 vertices) should look like:
   	 	[vertex1] [vertex2] [vertex3]
   	    [vertex4] [vertex5]
        """
        self.already_visited = list(self.num_vertices * 'f')
        string = ''
        not_use_again = []
        while 'f' in self.already_visited:
            first_not_visited_index = self.already_visited.index('f') # that function chooses the first found object in a list
            self.DFS(first_not_visited_index, first_not_visited_index)

            string += '#' # is needed to split the string later, we can distinguish between the several components/DFS iterations
            for index, visit in enumerate(self.already_visited):
                if visit == 't' and index not in not_use_again:
                    visited_vertex = self.vertices[index]
                    string += f'[{visited_vertex.name}] '
                    not_use_again.append(index)

        splitted_ele = string.split('#')
        for component in splitted_ele:
            print(component)
        return

    def is_cyclic(self):
        """return: Returns True if the graphs contains cycles, otherwise False.
        """
        self.cycle = False
        self.already_visited = list(self.num_vertices * 'f')

        # Search for cycles even if the graph is not connected:
        while self.cycle == False and 'f' in self.already_visited:
            first_not_visited_index = self.already_visited.index('f') # that function chooses the first found object in a list
            self.DFS(first_not_visited_index, first_not_visited_index)

        return self.cycle


    def DFS(self, current_ind, last_node_ind):

        self.already_visited[current_ind] = 't'

        if current_ind == self.num_vertices:
            return

        list_of_neighbours = self.get_adjacent_vertices(self.vertices[current_ind])

        # Check if the graph can go deeper or has to stop: # ??? needed
        if len(list_of_neighbours) == 1 and list_of_neighbours[0] == 't':
            return

        for node in list_of_neighbours:
            ind_node = self.vertices.index(node) # we need the index of neighbour to work with
            if self.already_visited[ind_node] == 'f':
                self.DFS(ind_node, current_ind)
            elif self.already_visited[ind_node] == 't' and ind_node != last_node_ind: # check if we have a loop here
                # ind_node is a neighbour of the current_ind which was already visited and is not the last checked index
                # Then a loop is built within the graph
                self.cycle = True

        return


