import math

class Coord: # X e Y
    def __init__(self, x, y): #Quando criado esse objeto precisa de x e y.
        self.x = x
        self.y = y

    @staticmethod
    def dist(p1, p2):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)  # Calcula a distancia entre dois pontos utilizando a formula d = ✓(x1-x2)^2 + (y1-y2)^2

    def __str__(self):
        return f"({self.x}, {self.y})"