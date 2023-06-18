# Athletic Competition Application

This application allows you to organize and manage athletic competitions. It includes an abstract class called `Athlete`, with public attributes for first name and last name, and a private attribute for the athlete's result in the competition. The class provides methods for result comparison, inputting athlete data from the console, and displaying athlete information.

## Class Hierarchy

- `Athlete`: An abstract class representing an athlete
  - Public attributes:
    - `first_name`: The first name of the athlete
    - `last_name`: The last name of the athlete
  - Private attributes:
    - `result`: The result achieved by the athlete in the competition
  - Abstract methods:
    - `is_better_than(other)`: Checks if the athlete's result is better than another athlete's result
  - Methods:
    - `read_data_from_console()`: Reads the athlete's data from the console
    - `display_data()`: Displays the athlete's data in the console

- `Runner`: A subclass of `Athlete` representing a runner
  - Inherits all attributes and methods from `Athlete`
  - Result comparison: Lower result is considered better

- `Jumper`: A subclass of `Athlete` representing a jumper
  - Inherits all attributes and methods from `Athlete`
  - Result comparison: Higher result is considered better

- `Discipline`: A class representing an athletic discipline
  - Private attributes:
    - `name`: The name of the discipline
    - `type`: The type of the discipline (enum: RUNNING, JUMPING)
    - `participants`: An array of athlete data representing the participants in the discipline
  - Methods:
    - `__init__(name, type, num_participants)`: Initializes the discipline with its name, type, and number of participants
    - `read_participant_data()`: Reads the participant data from the console
    - `display_winner_data()`: Displays the data of the winner in the discipline
