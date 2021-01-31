# either I can give only 1 team delivery
# Or 2 teams
# Or 3 teams, etc., of all the teams
# and, in these teams, 
# There can be plenty of ways to pick which pizza is going to them.
# That is the ultimate bruteforce
import itertools
from CSVConverter import CSVConverter
def allCombinationsOfSelections():
    with open('a_example',newline='') as File:
        # set data.csv file
        CSVConverter(File)
        File.seek(0,0)
        allLines = list(File.readlines())
        totalTeams = sum([int(i) for i in allLines[0].split()[1:]])
        output = []
        for i in range(1,totalTeams+1):
            allSelectionsOfTeams = [i for i in itertools.combinations(list('2'*int(allLines[0].split()[1:][0])+'3'*int(allLines[0].split()[1:][1])+'4'*int(allLines[0].split()[1:][2])),i)]
            allSelectionsOfTeams = set(allSelectionsOfTeams)
            output.append(allSelectionsOfTeams)
    return output

if __name__ == "__main__":
    output = allCombinationsOfSelections()
    for i in output:
        print(i)