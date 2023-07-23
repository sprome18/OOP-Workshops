class Graph:
    def __init__(self,number_of_verts):
        self.number_of_verts = number_of_verts
        self.graph_representation = [[] for _ in range(number_of_verts)]    # using an adjacency list

    def add_vertex(self):
        self.number_of_verts+=1
        self.graph_representation.append([])    # appending another list to represent the new vertex

    def add_edge(self,from_idx, to_idx, weight = 1 ):
        # check to see if indexes are invalid (outside the bounds of the graph)
        if (from_idx < 0) or (to_idx < 0) or (from_idx >= self.number_of_verts) or (to_idx >= self.number_of_verts):
            return False
        
        # check to see if the edge already exists
        for to_vertex, _ in self.graph_representation[from_idx]:
            if (to_vertex == to_idx):
                return False
        
        # add the edge if checks are passed
        self.graph_representation[from_idx].append((to_idx, weight))
        return True

    def num_edges(self):
        return sum(len(edges) for edges in self.graph_representation)

    def num_verts(self):
        return self.number_of_verts

    def has_edge(self, from_idx, to_idx):
        # check to see if indices are valid
        if from_idx < 0 or to_idx < 0 or from_idx >= self.number_of_verts or to_idx >= self.number_of_verts:
            return False

        # check for the to_idx in the list of vertices, return True if the edge is found in the adjacency list
        return to_idx in [vertex for vertex, _ in self.graph_representation[from_idx]]

    def edge_weight(self, from_idx,to_idx):
        # check to see if indices are valid
        if from_idx < 0 or to_idx < 0 or from_idx >= self.number_of_verts or to_idx >= self.number_of_verts:
            return None
        
        # check for the given edge and return the weight
        for to_vertex, weight in self.graph_representation[from_idx]:
            if to_vertex == to_idx:
                return weight
        
        # return None if checks were not passed
        return None

    def get_connected(self, v):
        if v < 0 or v >= self.number_of_verts:
            return []
        
        # return portion of the adjacency list at the given vertex, which should contain all connections
        return self.graph_representation[v]

