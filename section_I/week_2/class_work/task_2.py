# Write a program for the well-known game "paper, rock, scissors".
#  At the beginning, the user enters his name and the name of the opponent, 
# as well as the score that needs to be achieved in order to achieve the final victory (eg play to 10). 
# The game starts by asking each user to enter their choice (paper, rock, scissors). 
# The function counts which user won the current round. 
# After each game, the corresponding user's score increases until one of them wins.
# P.S. The final victory must be achieved with at least a 2-point difference (the game is played on the difference).

name_of_the_first_player = input("Insert the name of the first player: ")
name_of_the_second_player = input("Insert the name of the second player: ")
points_needed = int(input("Insert the the points needed for the victory: "))

number_of_points_of_first_player = 0
number_of_points_of_second_player = 0

def rock_paper_scissors(first_choice, second_choice):
    if first_choice == second_choice:
        return "same"
    if (first_choice == "rock" and second_choice == "scissors") or (first_choice == "paper" and second_choice == "rock")\
            or (first_choice == "scissors" and second_choice == "paper"):
        return True
    return False

while abs(number_of_points_of_second_player - number_of_points_of_first_player) <2:
    while number_of_points_of_second_player < points_needed and number_of_points_of_first_player < points_needed:
        first_choice = input("Insert the choice of the first player: ")
        while first_choice not in ("rock", "paper", "scissors"):
            first_choice = input("Insert the choice of the first player: ")
        second_choice = input("Insert the choice of the second player: ")
        while second_choice not in ("rock", "paper", "scissors"):
            second_choice = input("Insert the choice of the second player: ")
        result = rock_paper_scissors(first_choice, second_choice)
        if result == "same":
            continue
        elif rock_paper_scissors(first_choice, second_choice):
            number_of_points_of_first_player+=1
        else:
            number_of_points_of_second_player+=1
        print(number_of_points_of_first_player)
        print(number_of_points_of_second_player)


