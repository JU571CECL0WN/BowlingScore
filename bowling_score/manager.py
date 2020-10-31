from bowling_score.file_manager import FileManager
from bowling_score.calculate_score import CalculateScore


class Manager:
    def __init__(self):
        self.file_manager = FileManager()
        self.calculate_score = None

    def run(self):
        scores = self.file_manager.read_json()
        self.calculate_score = CalculateScore(scores)
        self.calculate_score.generate_frames()
        self.calculate_score.calculate_points()
        print(self.calculate_score.total)
