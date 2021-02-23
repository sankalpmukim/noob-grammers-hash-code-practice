from points import points
File=open('submissionstally.txt')
allData=File.readlines()
maxscore=0
indexOfMaxScore=None
i=0
while(i<len(allData)):
    score=0
    if len(allData[i])==2:
        rows=int(allData[i][0])
        j=i+1
        while j<=rows+i:
            score+=points(allData[j])
            # print(i,points(allData[j]),score,j)
            j+=1
    if score>maxscore:
        maxscore=score
        indexOfMaxScore=i
    i+=1
print(indexOfMaxScore,maxscore)
newFile=open('final.txt','w')
for i in range(rows+1):
    newFile.write(allData[i+indexOfMaxScore])