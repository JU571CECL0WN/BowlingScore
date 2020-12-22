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
        for frame in self.frames:
            for throw in frame.throws:
                next_throws = self.get_next_throws(throw.add, frame.position, throw.position)
                points = throw.points + sum(next_throws)
                self.total += points

    def get_next_throws(self, number, position_frame, position_throw):  # caso del decimo frame
        next_throws = []
        if number > 0:
            for frame in range(position_frame, len(self.frames)):
                for throw in self.frames[frame].throws:
                    next_throws.append(throw.points)
                    if len(next_throws) == number:
                        return next_throws
            if position_frame == 10:
                for throw in range(position_throw + 1, len(self.frames[position_throw].throws) + 1):
                    next_throws.append(self.frames[position_frame - 1].throws[throw - 1].points)
        return next_throws
