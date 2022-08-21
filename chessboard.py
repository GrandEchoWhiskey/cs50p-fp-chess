class chessboard:

    __width = 8
    __height = 8

    def __init__(self):
        self.__matrix = [[None for _ in range(self.__width)] for _ in range(self.__height)]

    @classmethod
    def from_fen(cls, fen="rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR"):
        

    def set(self, xy:tuple, obj:any):
        self.__matrix[xy[0]][xy[1]] = obj

    def rm(self, xy:tuple):
        self.set(xy, None)

    def get(self, xy:tuple):
        return self.__matrix[xy[0]][xy[1]]

    def move(self, f_xy:tuple, t_xy:tuple):
        self.set(t_xy, self.get(f_xy))
        self.rm(f_xy)