import csv
with open("data.csv") as f:
  reader=csv.reader(f)
  filedata=list(reader)
data=filedata[0]

sum=0
for x in data:
  sum=sum+int(x)
meanval=sum/len(data)
print("step 1:"+str(meanval))
print("step 2:"+str(sum))
squareddata=[]
sum2=0
for y in data:
  devbefore=(int(y)-meanval)*(int(y)-meanval)
  squareddata.append(devbefore)
print("step 3:"+str(squareddata))  
print("step 4:"+str(sum2))  
for r in squareddata:
  sum2=sum2+float(r)
devafter=sum2/len(squareddata)
print("step 5:"+str(devafter))
print(len("step 6:"+str(squareddata)))
import math
finaldev=math.sqrt(devafter)
print("step 7:"+str(finaldev))