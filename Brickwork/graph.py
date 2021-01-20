from collections import defaultdict


class Graph:
    def __init__(self, env):
        self._env = env
        self._rows = len(env)
        self._columns = len(env[0])
        self._adj = self.generate_adj()

    # generate a graph where:
    # - each node represents a side of a certain brick
    # - two nodes are connected only if they represent two different bricks
    # e.g. [[1, 1, 2, 2],[3, 3, 4, 4]] would look like:
    #   1 1--2 2
    #   | |  | |
    #   3 3--4 4
    def generate_adj(self):
        adj = defaultdict(list)
        for y in range(self._rows):
            for x in range(self._columns):
                for neighbour in self.get_neighbours(x, y):
                    current = self._env[y][x]
                    if neighbour.val != current.val:
                        adj[current].append(neighbour)
        return adj

    def get_neighbours(self, x, y):
        neighbours = []
        for row in range(-1, 2):
            for column in range(-1, 2):
                neighbour_x = column + x
                neighbour_y = row + y
                # skip when the neighbour is the node itself and don't get diagonal neighbours
                if neighbour_x == x and neighbour_y == y or abs(row) == abs(column):
                    continue
                elif neighbour_x < 0 or neighbour_x >= self._columns:
                    continue
                elif neighbour_y < 0 or neighbour_y >= self._rows:
                    continue
                else:
                    neighbours.append(self._env[neighbour_y][neighbour_x])
        return neighbours

    def get_size(self):
        return len(self._adj.items())

    def remove_node(self, target):
        for node in list(self._adj):
            neighbours = self._adj[node]
            if node == target:
                self._adj.pop(node)
            elif target in neighbours:
                neighbours.remove(target)

    def get_adj(self):
        return self._adj
