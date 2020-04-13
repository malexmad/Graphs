"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")
            # print("ERROR: vertex does not exist")

    def add_undirected_edge(self, v1, v2):
        """
        Add a undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")
            # print("ERROR: Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the frist vertex
            v = q.dequeue()
            # check if its been visited
            # if it hasn't been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # check if its been visited
            # if it hasn't been visited
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            print(starting_vertex)
            visited.add(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH to the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()

            # grab vertex from the end of the path
            # check if its been visited
            endvertex = path[-1]

            # if it hasn't been visited.....
            if endvertex not in visited:
                # Mark it as visited
                visited.add(endvertex)
                # check if its the destination
                # Enqueue a path to all it's neighbors
                for neighbor in self.get_neighbors(endvertex):
                    if neighbor == destination_vertex:
                        path.append(neighbor)
                        return path

                    # Make a copy to the path
                    # enqueue the copy
                    n_path = path.copy()
                    n_path.append(neighbor)
                    q.enqueue(n_path)




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # push A PATH to the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Dequeue the first path
            path = s.pop()

            # grab vertex from the end of the path
            # check if its been visited
            endvertex = path[-1]

            # if it hasn't been visited.....
            if endvertex not in visited:
                # Mark it as visited
                visited.add(endvertex)
                # check if its the destination
                # push a path to all it's neighbors
                for neighbor in self.get_neighbors(endvertex):
                    if neighbor == destination_vertex:
                        path.append(neighbor)
                        return path

                    # Make a copy to the path
                    # push the copy
                    n_path = path.copy()
                    n_path.append(neighbor)
                    s.push(n_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path == None:
            path = []
        # print(path)

        # Check if the node has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            # print(starting_vertex)
            visited.add(starting_vertex)
            n_path = path.copy()
            n_path.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return n_path

            # Call dfs_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, n_path)

                if new_path != None:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
