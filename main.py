import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:
    def __init__(self, points):
        #points ex.
        #[(5, 6), (9, 9)]
        self.points = points
        self.a = 0
        self.b = 0

    def solve(self):
        xy = 0
        x_2 = 0
        y_2 = 0
        x = 0
        y = 0
        n = len(self.points)

        for point in self.points:
            x += point[0]
            y += point[1]
            xy += point[0] * point[1]
            x_2 += point[0] ** 2
            y_2 += point[1] ** 2

        a = ((y * x_2) - (x * xy)) / ((n * x_2) - x**2)
        b = ((n * xy) - (x * y)) / ((n * x_2) - x**2)
        
        self.a = a
        self.b = b

class QuadraticRegression:
    def __init__(self, points):
        self.points = points
        self.a = 0
        self.b = 0
        self.c = 0

    def solve(self):
        x = 0
        y = 0
        x_2 = 0
        x_3 = 0
        x_4 = 0
        xy = 0
        x_2y = 0
        n = len(self.points)

        for point in self.points:
            x += point[0] * 10
            y += point[1] * 10
            x_2 += (point[0] * 10) ** 2
            x_3 += (point[0] * 10) ** 3
            x_4 += (point[0] * 10) ** 4
            xy += (point[0] * 10) * (point[1] * 10)
            x_2y += ((point[0] * 10) ** 2) * (point[1] * 10)
        
        a = ((x ** 2) * x_2y - n * x_2 * x_2y - x * x_2 * xy + n * x_3 * xy + ((x_2) ** 2) * y - x * x_3 * y ) / (((x_2) ** 3) - 2 * x * x_2 * x_3 + n * ((x_3) ** 2) + (x ** 2) * x_4 - n * x_2 * x_4)
        b = (n * x_2y * x_3 - x * x_2 * x_2y + (x_2) ** 2 * xy + x * x_4 * y - n * x_4 * xy - x_2 * x_3 * y) / ((x_2) ** 3 - 2 * x * x_2 * x_3 + n * (x_3) ** 2 + (x) ** 2 * x_4 - n * x_2 * x_4)
        c = ((x_2) ** 2 * x_2y - x * x_2y * x_3 + x * x_4 * xy + (x_3) ** 2 * y - x_2 * x_4 * y - x_2 * x_3 * xy) / ((x_2) ** 3 - 2 * x * x_2 * x_3 + n * (x_3) ** 2 + (x) ** 2 * x_4 - n * x_2 * x_4)

        self.a = a
        self.b = b
        self.c = c

def quadraticRegTest():
    points = [(-5, 12.51), (-4, 15.28), (-3, 12.73), (-2, 12.69), (-1, 8.03), (0, 8.14), (1, 9.12), (2, 10.40), (3, 11.80), (4, 13.12)]
    test = QuadraticRegression(points)
    test.solve()
    x = np.linspace(-500,500,100)
    y = (test.a * x ** 2) + (test.b * x) + test.c
    plt.plot(x, y, '-r', label='y=2x+1')
    for point in points:
        plt.plot(point[0] * 10, point[1] * 10, 'bo')

    #plt.title("Graph of y=2x+1")
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


def linearRegTest():
    points = [(1, 30), (2, 45), (3, 51), (4, 57), (5, 60), (6, 65), (7, 70), (8, 71)]
    test = LinearRegression(points)
    test.solve()

    x = np.linspace(-500,500,100)
    y = test.b * x + test.a
    plt.plot(x, y, '-r', label='y=2x+1')
    for point in points:
        plt.plot(point[0], point[1], 'bo')

    #plt.title("Graph of y=2x+1")
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

linearRegTest()
quadraticRegTest()
