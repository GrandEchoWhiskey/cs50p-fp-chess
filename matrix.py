class matrix2d:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__matrix = self.mkmatrix(width, height)
        self.__history = []

    @staticmethod
    def mkmatrix(width, height):
        res = []
        for x in range(width):
            tmp = []
            for y in range(height):
                tmp.append(None)
            res.append(tmp)
        return res

    def history_add(self, f_xy, t_xy):
        self.__history.append((f_xy, t_xy))

    def move(self, from_xy:tuple, to_xy:tuple):
        self.set(to_xy, self.get(from_xy))
        self.set(from_xy, None)

    def set(self, xy:tuple, obj:any=None):
        self.__matrix[xy[0]][xy[1]] = obj

    def get(self, xy:tuple):
        return self.__matrix[xy[0]][xy[1]]

m = matrix2d(8, 8)
m.set((2,4), 'cda')
m.move((2,4), (5,4))
print(m._matrix2d__matrix)