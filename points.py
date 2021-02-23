import csv
def points(line):
    selectedPizzas = line.split()[1:]
    selectedPizzas = [int(i) for i in selectedPizzas]
    with open('data.csv',newline='') as dataFile:
        setOfIngredients = set()
        # print("All ingredients:->",listOfIngredients)
        dataFile.seek(0,0)
        allPizzas = list(csv.reader(dataFile))[1:]
        for currentPizzaIndex in selectedPizzas:
            currentPizza = allPizzas[currentPizzaIndex][1:]
            for ingredientIndex in range(len(currentPizza)):
                if currentPizza[ingredientIndex] == '1':
                    setOfIngredients.add(ingredientIndex)
        points = len(setOfIngredients)**2
        # print(setOfIngredients)
        # print("points = ",points)
        return points


if __name__ == "__main__":
    print(points('3 0 2 3'))