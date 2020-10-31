from bowling_score.frame import Frame


class CalculateScore:
    def __init__(self, scores):
        self.scores = scores
        self.total = 0
        self.frames = []

    def generate_frames(self):
        keys = []
        for k in self.scores:
            keys.append(int(k))
        keys.sort()

        for k in keys:
            self.frames.append(
                Frame(k, self.scores[str(k)])
            )

    def calculate_points(self):
        for f in self.frames:
            if f.add > 0:
                if f.position == 10:
                    break
                next_throws = self.get_next_throws(f.add, f.position)
                for throw in next_throws:
                    if throw == "X":
                        f.points += 10
                    elif throw == "/":
                        f.points += 20 - f.points
                    elif throw.isdigit():
                        f.points += int(throw)

            self.total += f.points

    def get_next_throws(self, number, position):
        pass
