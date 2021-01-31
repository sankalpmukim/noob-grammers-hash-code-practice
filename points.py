import csv
def points(line):
    pizzas = line.split()[1:]
    selectedPizzas = [int(i) for i in pizzas]
    with open('data.csv',newline='') as dataFile:
        setOfIngredients = set()
        listOfIngredients = list(csv.reader(dataFile))[0][1:]
        print("All ingredients:->",listOfIngredients)
        dataFile.seek(0,0)
        pizzas = list(csv.reader(dataFile))[1:]
        for i in range(len(pizzas)):
            if i in selectedPizzas:
                pizzaLine=pizzas[i][1:]
                for ingredientIndex in range(len(pizzaLine)):
                    if int(pizzaLine[ingredientIndex]) == 1:
                        setOfIngredients.add(ingredientIndex)
        points = len(setOfIngredients)**2
        print(setOfIngredients)
        print("points = ",points)


if __name__ == "__main__":
    points('2 1 4')