file = input("Enter file name:")
import re
fh = open(file)
sum = 0
for line in fh:
    y = re.findall("[0-9]+",line)
    if y == []:
        continue
    #print(y)
    for n in y:
        #print(n)
        n = int(n)
        sum = sum + n
        #print(sum)
print(sum)
