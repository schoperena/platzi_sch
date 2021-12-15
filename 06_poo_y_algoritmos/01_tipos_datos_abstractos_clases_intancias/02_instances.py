
class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordinate):
        x_diff = (self.x - other_coordinate.x)**2
        y_diff = (self.y - other_coordinate.y)**2
        return (x_diff + y_diff)**0.56


def main():

    coor_1 = Coordinate(3, 30)
    coor_2 = Coordinate(4, 8)

    print(coor_1.distance(coor_2))
    print(isinstance(coor_2, Coordinate))


if __name__ == '__main__':
    main()
