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
        pass

