from itertools import combinations,permutations
from allCombinationsOfSelections import allCombinationsOfSelections
File = open('a_example', newline='')
output = [list(i) for i in allCombinationsOfSelections(File)]
file = open('data.csv', newline='')
numberOfPizzas = len(file.readlines())-1
listSubtraction=lambda lst1,lst2: [item for item in lst1 if item not in lst2]
# print(output)
for r in range(len(output)):
    tup=0
    while tup<len(output[r]):#for tup in range(len(output[r])):
        temp=[]
        for ele in range(len(output[r][tup])):
            temp.append(int(output[r][tup][ele]))
        if sum(temp)<=numberOfPizzas:
            output[r][tup]=temp #hehe
        else:
            output[r].remove(output[r][tup])
            tup-=1
        tup+=1
print(output)

# arrayOfOneDelivery/two/three/fourdeliverysubmissions->kindOfSubmission(single/double delivery) 2->submission(actual deliveries)->n-person team
# [[[2], [4], [3]], [[2, 3]], [], []]->                   [[2], [4], [3]]/[[2, 3]]->                [2]/[3]/[2,3]//basically in this submission at least 1 2 person and 1 3 person team gets
i=0
while i<len(output):
    if len(output[i])==0:
        output.remove(output[i])
        i-=1
    i+=1
print(output)
# perms=permutations(list(range(numberOfPizzas)),totalPizzasBeingDelivered)
# print(list(perms))
# if only 1 delivery then C(availablePizzas,numOfPeopleInThatTeam)
# if 2 teams, then C(availablePizzas, members-in-first-team)*C(availablePizzas,members-in-second-team)
# if 3 teams, then so on.... here availablePizzas is changing based on which pizzas get selected
def singleTeamPizzas(availablePizzas,members):
    print('singleTeamPizzas')
    return list(combinations(availablePizzas,members[0])) 
# print(singleTeamPizzas(list(range(5)),[2]))
def multipleTeamPizzas(availablePizzas,members):
    if len(members)==2:
        print('multipleTeamPizzas')
        orderCombinations = combinations(availablePizzas,members[0])
        return [[order,singleTeamPizzas(listSubtraction(availablePizzas,order),members[1:])] for order in orderCombinations]
    else:
        orderCombinations = combinations(availablePizzas,members[0])
        return [[order,multipleTeamPizzas(listSubtraction(availablePizzas,order),members[1:])] for order in orderCombinations]
# print(multipleTeamPizzas(list(range(5)),[2,3]))
submissionData=lambda tupl:str(len(tupl))+' '+str(tupl)[1:-1].replace(',','')+'\n'
submissionObj=open('submissionstally.txt','a')
# lst=[(0, 1), [(2, 3, 4)]],''
def makeMultipleSubmission(lst,strng=''):
    strng+=submissionData(lst[0])
    for element in lst[1:]:
        if len(element)>1:
            makeMultipleSubmission(lst[1:],submissionData(lst[0]))
            print(lst[1:])
        else:
            submissionObj.write(str(len(strng.split('\n')))+'\n'+strng+submissionData(element[0]))
            print(str(len(strng.split('\n')))+'\n'+strng+submissionData(element[0]))
def makeSingleSubmission(lst):
    strng='1\n'+submissionData(lst)
    submissionObj.write(strng)
# for i in multipleTeamPizzas(list(range(5)),[2,3]):
#     makeMultipleSubmission(i)
arrayOfKindOfSubmissions=output
for kindOfSubmission in arrayOfKindOfSubmissions:
    for submission in kindOfSubmission:
        # totalPizzasBeingDelivered=sum(submission)
        # print('totalPizzasInSubmission:>',totalPizzasBeingDelivered)
        if len(submission)==1:
            for i in singleTeamPizzas(list(range(numberOfPizzas)),submission):
                makeSingleSubmission(i)
        else:
            for i in multipleTeamPizzas(list(range(numberOfPizzas)),submission):
                makeMultipleSubmission(i)