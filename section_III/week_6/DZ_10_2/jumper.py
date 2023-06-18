from athlete import Athlete

class Jumper(Athlete):
    def __init__(self):
        self.load_data()
        
    def compare_results(self, other: "Athlete"):
        return self.get_result() > other.get_result()    
   
