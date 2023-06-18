from discipline import Discipline
from discipline_type import DisciplineType

if __name__ == "__main__":
    long_jump = Discipline("Long jump", DisciplineType.JUMPING, 2)
    print(long_jump.find_winner())
    sprint = Discipline("100 m", DisciplineType.RUNNING, 2)
    print(sprint.find_winner())