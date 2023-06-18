from abc import ABC, abstractmethod

class Athlete(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__result = None
    
    @abstractmethod
    def compare_results(self, other):
        pass
    
    def load_data(self):
        name = input("Input athlete name: ")
        while True:
            try:
                result = float(input("Input result: "))
                break
            except:
                print("invalid result, try again")
        self.name = name
        self.__result = result

    def get_result(self):
        return self.__result

    def __repr__(self) -> str:
        return f"The athlete's name is {self.name} and his score is {self.__result}"    