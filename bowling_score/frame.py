class Frame:
    def __init__(self, position, throws):
        self.throws = throws
        self.position = position
        self.points = 0
        self.add = 0
        self.calculate_points()

    def calculate_points(self):
        for t in self.throws:
            if t == "X":
                self.points = 10
                self.add = 2
            elif t == "/":
                self.points = 10
                self.add = 1
            else:
                self.points += t
