from athlete import Athlete
from discipline_type import DisciplineType
from typing import List
from runner import Runner
from jumper import Jumper


class Discipline:
    name: str
    dis_type: DisciplineType
    number_of_competitors: int
    athlets_list: List[Athlete]

    def __init__(self, name: str, dis_type: DisciplineType, number_of_competitors: int) -> None:
        self.name = name
        self.dis_type = dis_type
        self.number_of_competitors = number_of_competitors
        self.athlets_list = []
        self.__load_all_athlets()

    def __load_all_athlets(self):
        for _ in range(0, self.number_of_competitors):
            if self.dis_type == DisciplineType.JUMPING:
                self.athlets_list.append(Jumper())

            elif self.dis_type == DisciplineType.RUNNING:
                self.athlets_list.append(Runner())

    def find_winner(self) -> Athlete:
        winner = self.athlets_list[0]
        for athlet in self.athlets_list:
            if athlet.compare_results(winner):
                winner = athlet
        return winner
