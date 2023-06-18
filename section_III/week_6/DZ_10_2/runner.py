from athlete import Athlete


class Runner(Athlete):
    def __init__(self):
        self.load_data()

    def compare_results(self, other):
        return self.get_result() < other.get_result() 
