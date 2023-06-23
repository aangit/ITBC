# A baker makes bread. He needs 400 grams of flour for one loaf of bread. 
# n kg of flour is available in the bakery (entered by the user). 
# The baker makes bread as long as he has flour or until he has made 200 loaves of bread. 
# Calculate how many days it takes the baker to use up all the flour, as well as how many loaves of bread he baked on the last day.
# Solve using loops

flour_per_loaf = 400
loaves_per_day = 200

flour_available = float(input("Enter the amount of flour available in kg: "))

total_loaves = 0
days = 0

while flour_available >= (flour_per_loaf / 1000) and total_loaves < loaves_per_day:
    total_loaves+=1
    flour_available-= (flour_per_loaf / 1000)

    if total_loaves == loaves_per_day:
        days+=1
        total_loaves = 0

loaves_last_day = total_loaves

if loaves_last_day ==0:
    days-=1

print("It took the baker", days, "days to use up all the flour.")
print("On the last day, the baker baked", loaves_last_day, "loaves of bread.")



    
