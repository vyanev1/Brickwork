from brick import create_brick
from graph import Graph
import sys


class BrickLayer:
    def __init__(self, rows, cols, matrix):
        self._rows = rows
        self._columns = cols
        self._env = self.generate_env(matrix)
        self._graph = Graph(self._env)

    # generate a list similar to the <int>list from the input
    # where each int is replaced by a brick that has the following props:
    # { val, coords, size, side }
    # e.g. [[1, 1, 2, 2],[3, 3, 4, 4]] would look like:
    # [[Brick(1,(0,0),2,'start'), Brick(1,(1,0),2,'end'), Brick(2,(2,0),2,'start'), Brick(2,(3,0),2,'end')],
    #  [Brick(3,(0,1),2,'start'), Brick(3,(1,1),2,'end'), Brick(4,(2,1),2,'start'), Brick(4,(3,1),2,'end')]]
    @staticmethod
    def generate_env(matrix):
        visited = set()
        env = []
        for y in range(len(matrix)):
            env.append([])
            for x in range(len(matrix[y])):
                if matrix[y][x] not in visited:
                    brick = create_brick(matrix, (x, y))
                else:
                    brick = create_brick(matrix, (x, y), 'end')
                if brick.get_size() != 2:
                    raise Exception(f'Invalid brick size at coordinates {(x, y)}')
                visited.add(matrix[y][x])
                env[y].append(brick)
        return env

    # pick the node with the minimum degree (number of edges)
    def get_mindegree_node(self):
        min_edges = sys.maxsize
        min_node = None
        for node in list(self._graph.get_adj()):
            neighbours = self._graph.get_adj()[node]
            if len(neighbours) < min_edges:
                min_edges = len(neighbours)
                min_node = node
        return min_node

    # Get the next layer of bricks by running a perfect matching algorithm:
    # - pick a node from the graph with the lowest degree (least connections)
    # - get one of its neighbours
    # - get their coords and remove them both from the graph
    # - put a brick in the new layer (next_layer) on their place
    # NOTE: Because there is edges only between adj bricks we ensure the next layer won't have any overlapping bricks
    def get_next(self):
        adj = self._graph.get_adj()
        next_layer = [[None for _ in range(self._columns)] for _ in range(self._rows)]
        brick_val = 1
        while self._graph.get_size() > 0:
            node = self.get_mindegree_node()
            if not(adj[node]):
                return -1
            neighbour = adj[node][0]

            self._graph.remove_node(node)
            self._graph.remove_node(neighbour)

            node_x, node_y = node.get_coords()
            neighbour_x, neighbour_y = neighbour.get_coords()

            next_layer[node_y][node_x] = brick_val
            next_layer[neighbour_y][neighbour_x] = brick_val

            brick_val += 1
        return next_layer

    def print_env(self):
        print([[(node.val, node.side) for node in row] for row in self._env])

    def print_adj(self):
        [print(f'{key}: {[str(neigh) for neigh in value]}') for key, value in self._graph.get_adj().items()]
