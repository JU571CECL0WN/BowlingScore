from bowling_score.frame import Frame


class CalculateScore:
    def __init__(self, scores):
        self.scores = scores
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
        temp = []
        for f in self.frames:
            while f.add != 0:
                for add in range(f.position + 1, len(self.frames) + 1):
                    if add == "X":
                        f.points += 10
                    elif add == "/":
                        f.points += 20 - f.points
                    elif add == "-":
                        pass
                    else:
                        f.points += int(add)
                    f.add -= 1
            temp.append(f)
        self.frames = temp


