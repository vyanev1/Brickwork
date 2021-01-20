class Brick:
    def __init__(self, val, coords, size, side):
        self.val = val
        self.side = side
        self._coords = coords
        self._size = size

    def get_size(self):
        return self._size

    def get_coords(self):
        return self._coords

    # override the __hash__ and __eq__ methods so that you can
    # compare Brick objects and use them as keys and values in the adjacency list
    def __hash__(self):
        return hash((self.val, self.side, self._coords, self._size))

    def __eq__(self, other):
        return (self.val, self.side, self.get_coords(), self.get_size()) \
               == (other.val, other.side, other.get_coords(), other.get_size())

    # used for printing purposes while debugging
    def __str__(self):
        return str({'val': self.val, 'side': self.side})


# create a brick from the <int>list inputMatrix by using its coordinates
def create_brick(matrix, coords: tuple, side='start'):
    x, y = coords
    val = matrix[y][x]
    size = 1
    increment = 1 if side == 'start' else -1
    if 0 <= x + increment < len(matrix[y]) and matrix[y][x + increment] == val:
        while 0 <= x + increment < len(matrix[y]) and matrix[y][x + increment] == val:
            size += 1
            x += increment
    elif 0 <= y + increment < len(matrix) and matrix[y + increment][x] == val:
        while 0 <= y + increment < len(matrix) and matrix[y + increment][x] == val:
            size += 1
            y += increment
    return Brick(val, coords, size, side)
