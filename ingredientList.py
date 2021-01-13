def ingredientList(File):
    File.__next__()
    setOfIngredients = set()
    lines = File.readlines()
    for line in lines:
        temp = line.split()
        for i in temp[1:]:
            setOfIngredients.add(i)
    return sorted(list(setOfIngredients))

if(__name__ == "__main__"):  #testing
    with open('a_example') as File:
        print(ingredientList(File))