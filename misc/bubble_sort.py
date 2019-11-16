
import timeit
import random

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 
  
# Driver Code 
num = 5000
start = 0
#end = 1000000000000
end = num*10
alist1 = Rand(start, end, num)
alist2 = alist1.copy()

#print(alist1)
#print(alist2)

def bubbleSort(alist1):
    for passnum in range(len(alist1)-1,0,-1):
        for i in range(passnum):
            if alist1[i]>alist1[i+1]:
                temp = alist1[i]
                alist1[i] = alist1[i+1]
                alist1[i+1] = temp

def bubbleSort2(alist2):
    for passnum in range(len(alist2)-1,0,-1):
        for i in range(passnum):
            if alist2[i]>alist2[i+1]:
                alist2[i],alist2[i+1]=alist2[i+1],alist2[i]

#alist1 = [54,26,93,17,77,31,44,55,20]
#alist2 = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)

print(timeit.timeit("bubbleSort(alist1)", number=100, globals=globals()))
#print(alist1)

print(timeit.timeit("bubbleSort2(alist2)", number=100, globals=globals()))
#print(alist2)

