from Graph import Graph
from typing import List
import numpy as np
class Roadmap(Graph):
    def __init__(self):

        super().__init__()

        self.weight_matrix = []
        self.visited_set = set()# visited list will also be used as path ????????
        self.not_visited_set = set()

    def recursive_path_finder(self, from_station, to_station, current_ind, visited_list3, weight_list2, final_list):
        current_vertex = self.vertices[current_ind]
        current_name = current_vertex.name

        current_weight = weight_list2[current_ind]

        # Append the final list but put new elements at the first position because we go from the aim to the start:
        final_list = [(current_name,current_weight)] + final_list

        visited_list3[current_ind] = True

        list_of_neighbours = self.get_adjacent_vertices(current_vertex)

        for single_neighbour in list_of_neighbours:
            ind_neighbour = self.vertices.index(single_neighbour)

            if visited_list3[ind_neighbour] == False: # we don't want to go into a cycle. Therefore, we mark all vertices which were already added to the final list.

                street_weight = self.has_edge(current_vertex, single_neighbour)
                weight_of_neighbour = weight_list2[ind_neighbour]

                if current_weight - street_weight - weight_of_neighbour == 0 and street_weight != -1: # when the weight difference is 0 we know that our searched path is found

                    if ind_neighbour == from_station: # we reached our start vertex, so we can stop
                        name_from_station = single_neighbour.name
                        final_list = [(name_from_station,weight_of_neighbour)] + final_list
                        return final_list

                    return self.recursive_path_finder(from_station,to_station,ind_neighbour, visited_list3, weight_list2,final_list)

    def print_shortest_distance(self, from_station: int, to_station: int):
        """This method determines and prints the shortest path between two stations (= vertex indices) "from_station" and "to_station",
       	 using the dijkstra algorithm. The shortest distance is returned.
       	 @param from_station
       	 	vertex index of the start station
       	 @param to_station
       	 	vertex index of the destination station
       	 @return
       	    The path with the already covered distance is returned as List of tuples. This list contains sequentially
       	    each station's name along the shortest path, together with the already covered distance.
       	    (see example on the assignment sheet)
    	 """


        # Create a boolean list where no node was vistied:
        visited_list = [False] * self.num_vertices
        # Create list where all weights will be updated:
        weight_list = [float('Inf')] * self.num_vertices

        # The starting node gets weight of 0:
        weight_list[from_station] = 0

        weight_list2,visited_list2, path_saver = self.new_try(weight_list,visited_list,from_station,to_station,[], True)
        visited_list3 = [False] * len(weight_list2)

        final_list = self.recursive_path_finder(from_station,to_station,to_station, visited_list3, weight_list2, [])

        # At last step we create an printed output:
        string = f"""Shortest distance from {self.vertices[from_station].name} to {self.vertices[to_station].name}: {final_list[-1][1]}"""

        for index, (name,final_weight) in enumerate(final_list):
            if index == 0: # we are at the starting vertex
                pass
            elif index == len(final_list)-1: # we are at the destination vertex
                string += f"\n\tto {name}: {final_weight}"
            else:
                string += f"\n\tover {name}: {final_weight}"

        print(string)

        return final_list



    def new_try(self, weight_list, visited_list, current_ind, to_station, path_saver, with_target_stopping):

        # We mark the current node as visited:


        current_weight_node = weight_list[current_ind]
        current_vertex = self.vertices[current_ind]

        # First we want to look at all neighbours to update their weights:
        list_of_neighbours = self.get_adjacent_vertices(current_vertex)

        # Look at the neighbours by searching their weights:
        for single_neighbour in list_of_neighbours:
            distance_bw_current_neigh = self.has_edge(current_vertex, single_neighbour)

            # Update their weights:
            index_of_neigh = self.vertices.index(single_neighbour)

            if visited_list[index_of_neigh] == False and distance_bw_current_neigh < weight_list[index_of_neigh]:
                # we only can update the weights when the nodes weren't visited so far.

                # We only update weights which are worse than the current value:
                potential_new_weight = distance_bw_current_neigh + current_weight_node
                if potential_new_weight < weight_list[index_of_neigh]:
                    weight_list[index_of_neigh] = potential_new_weight


        if False not in visited_list: # We have visited all nodes by now --> We can stop.

            return weight_list,visited_list,path_saver

        else:
            # Find next place to go:
            curr_min_weight = float('Inf')
            index = 0
            min_index = None

            for bool_, weight_ in zip(visited_list,weight_list):
                if bool_ == False and weight_ < curr_min_weight:

                    curr_min_weight = weight_
                    min_index = index
                index += 1

            # Append the path_saver list: Here we store all nodes which we visted:
            # Search for edge between the current node and the node with minimal weight in whole graph
            found_edge = False

            for single_edge in self.edges:

                if ((single_edge.vertex_in == current_ind and single_edge.vertex_out == min_index) or (single_edge.vertex_in == min_index and single_edge.vertex_out == current_ind)) and \
                        single_edge.weight+weight_list[current_ind]<weight_list[min_index]: # delete thing after or ???

                    path_saver.append(single_edge)
                    found_edge = True
                    break # we no longer need to loop through all edges because we found the required one.


            # 31.01.21:
            # When we don't find any connection between current vertex in minimal vertex then
            # search for the minimal vertex the node (already visitied neighbour) which determines the weight of the minimal vertex.
            # One neighbour which fulfills that conditions is enough:
            if found_edge == False:

                for vistied_ind, vert in enumerate(visited_list):

                    if vert == True and (weight_list[min_index] - weight_list[vistied_ind] - self.has_edge(min_index, vistied_ind) == 0) and vistied_ind != -1:
                        for single_edge in self.edges:
                            if (single_edge.vertex_in == vistied_ind and single_edge.vertex_out == min_index) or (single_edge.vertex_in == min_index and single_edge.vertex_out == vistied_ind):
                                path_saver.append(single_edge)



            if min_index == to_station and with_target_stopping == True: # the next current node is already our destination

                return weight_list,visited_list,path_saver

            if min_index == None:
                return weight_list,visited_list,path_saver

            visited_list[current_ind] = True
            return self.new_try(weight_list, visited_list, min_index, to_station,path_saver, with_target_stopping)



    def dijkstra_shortest_path(self, current_vertex: int, visited : List[bool], distances: List[int],total_weight): #only search for nearest neighbour
        # Firstly, find where the current vertex index in the graph is:
        current_vertex_node = self.vertices[current_vertex]

        # Now have a look at the adjacent vertices. Therefore, use get_adjacent_vertices method from Graph.py:
        current_neighbours = self.get_adjacent_vertices(
            current_vertex_node)  # we have to feed in the vertex and not the index,
        # the method get_adjacent_vertices changes the vertex into an index and the works with it

        # we want to find the adjacent vertex with the least weight and also update all weights for the adjacent vertices:
        min_weight = float('Inf')
        min_neighbour = None
        for single_neighbour in current_neighbours:  # We loop over the list of neighbours


            if single_neighbour not in self.visited_set: # else we have to ignore the vertex because vertices' weights in the vistied set aren't changable

                single_weight = self.has_edge(current_vertex, single_neighbour)
                single_weight = total_weight + single_weight
                index_neighbour = self.vertices.index(single_neighbour)

                weight_update = False


                self.weight_matrix[current_vertex][index_neighbour] = single_weight # we update the weight to a smaller one
                self.weight_matrix[index_neighbour][current_vertex] = single_weight # because we have no directed graphs

                if single_weight < self.weight_matrix[index_neighbour][index_neighbour]:
                    self.weight_matrix[index_neighbour][index_neighbour] = single_weight
                    weight_update = True
                # Find the smallest weight among the adjacent vertices:
                if single_weight < min_weight:
                    min_weight = single_weight
                    min_neighbour = single_neighbour
                    min_index = index_neighbour
                    min_weight_update = weight_update

        if min_neighbour != None:
            # Add node to visited and delete it from not visited set:
            self.visited_set.add(min_neighbour)
            self.not_visited_set.remove(min_neighbour)

            # return the adjacent matrix with the minimal weight:
            return min_weight, min_neighbour, min_index, min_weight_update, total_weight

        return None,None,None, None, None # There are no neighbours which could be visited any longer


    def print_shortest_distances(self, from_station: int):
        """This method determines and prints the shortest path from station (= vertex index) "from_station" to all other stations
       	 using the dijkstra algorithm, and returns them in a list.
       	 @param from_station
       	 	vertex index of the start station
       	 @return:
       	 	the results in form of a list of integers, where the indices correspond to the indices of the stations.
       	    (see example on the assignment sheet)
        """


        # Create a boolean list where no node was vistied:
        visited_list = [False] * self.num_vertices
        # Create list where all weights will be updated:
        weight_list = [float('Inf')] * self.num_vertices

        # The starting node gets weight of 0:
        weight_list[from_station] = 0

        self.print_components()

        for single_list in self.my_components_nested:


            if from_station not in single_list:
                for single_list_ind in single_list:
                    # We now treat the components which are not reachable from the from_station index as visited nodes.
                    # Through that the weight of -1 can't change anymore, such that this is the final weight.
                    visited_list[single_list_ind] = True
                    weight_list[single_list_ind] = -1


        weight_list2,visited_list2,path_saver2 = self.new_try(weight_list, visited_list, from_station, 99, [], False) # we can ignore to_station = 99

        string = """from """

        # First add starting vertex to string:
        name_start = self.vertices[from_station].name
        string += name_start

        for index, single_weight in enumerate(weight_list2):
            #if index != from_station: # You can use it or not
            name = self.vertices[index].name
            string += f"\n\tto {name}: {single_weight}"

        print(string)
        return weight_list2



from Station import Station
map = Roadmap()
"""
a = map.insert_vertex(Station("A"))
b = map.insert_vertex(Station("B"))
c = map.insert_vertex(Station("C"))
map.insert_edge(a,b, 80)
map.insert_edge(a,c,200)
map.insert_edge(b,c,140)
"""
"""
a = map.insert_vertex(Station("A"))
b = map.insert_vertex(Station("B"))
c = map.insert_vertex(Station("C"))
d = map.insert_vertex(Station("D"))
e = map.insert_vertex(Station("E"))
map.insert_edge(a,b, 100)
map.insert_edge(a,c,50)
map.insert_edge(b,d,100)
map.insert_edge(c,d, 200)

map.print_shortest_distance(0,3)
map.print_shortest_distances(0)
#map.dijkstra_shortest_path(0, [],[],0)
#g = Graph()
#print(g.vertices)
#print(map.edges)
for e in map.vertices:
    if len(e.name) >0:
        print(e.name)
"""
map = Roadmap()
linz = map.insert_vertex(Station("Linz"))
stpoelten = map.insert_vertex(Station("St.Poelten"))
wien = map.insert_vertex(Station("Wien"))
innsbruck = map.insert_vertex(Station("Innsbruck"))
bregenz = map.insert_vertex(Station("Bregenz"))
eisenstadt =map.insert_vertex(Station("Eisenstadt"))
graz = map.insert_vertex(Station("Graz"))
klagenfurt = map.insert_vertex(Station("Klagenfurt"))
salzburg = map.insert_vertex(Station("Salzburg"))
washington = map.insert_vertex(Station("Washington"))

map.insert_edge(linz, stpoelten, 140)
map.insert_edge(stpoelten, wien, 80)
map.insert_edge(linz,wien, 200)
map.insert_edge(wien,eisenstadt, 100)
map.insert_edge(wien,graz, 190)
map.insert_edge(graz,klagenfurt, 160)
map.insert_edge(klagenfurt, salzburg, 210)
map.insert_edge(linz, salzburg, 150)
map.insert_edge(salzburg, innsbruck, 250)
map.insert_edge(klagenfurt, innsbruck, 300)
map.insert_edge(bregenz, innsbruck, 200)

res = map.print_shortest_distance(innsbruck,eisenstadt)
res2 = map.print_shortest_distances(wien)