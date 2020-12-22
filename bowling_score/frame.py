from bowling_score.throw import Throw


class Frame:
    def __init__(self, position, throws):
        self.throws = throws
        self.position = position
        self.calculate_points()

    def calculate_points(self):
        final_throws = []
        keys = [letter for letter in range(0, len(self.throws))]
        for t in keys:
            if self.throws[t] == "X":
                points = 10
                add = 2
                if self.position == 10:
                    add = len(self.throws) - t - 1
            elif self.throws[t] == "/":
                points = 10 - int(self.throws[t - 1])
                add = 1
            else:
                points = int(self.throws[t])
                add = 0

            final_throws.append(Throw(t, points, add))
        self.throws = final_throws
