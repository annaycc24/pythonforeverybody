#file = input("Enter file name:")
import re
lst = list()
#fh = open('regex_sum_262502.txt')
#r = fh.read()
#y = re.findall("[0-9]+",open('regex_sum_262502.txt').read())
for num in re.findall("[0-9]+",open('regex_sum_262502.txt').read()):
    n = int(num)
#    print(n)
#    print(type(n))
    lst.append(n)
    #print(lst)
print(sum(lst))
