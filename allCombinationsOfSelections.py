# either I can give only 1 team delivery
# Or 2 teams
# Or 3 teams, etc., of all the teams
# and, in these teams, 
# There can be plenty of ways to pick which pizza is going to them.
# That is the ultimate bruteforce
import itertools
from CSVConverter import CSVConverter
def allCombinationsOfSelections(File):
    # set data.csv file
    CSVConverter(File)
    File.seek(0,0)
    allLines = File.readlines()
    totalTeams = sum([int(i) for i in allLines[0].split()[1:]])
    for i in range(1,totalTeams+1):
        allSelectionsOfTeams = (itertools.combinations(list('2'*int(allLines[0].split()[1:][0])+'3'*int(allLines[0].split()[1:][1])+'4'*int(allLines[0].split()[1:][2])),i))
        yield(allSelectionsOfTeams)

if __name__ == "__main__":
    with open('a_example',newline='') as File:#b_little_bit_of_everything.in
        output = allCombinationsOfSelections(File)
        for i in output:
            print('*new-*')
            for j in set(i):
                print(j)
            