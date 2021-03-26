import sys

def selectionSort(alist):
   for i in range(len(alist)):
       minPosition = i
       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                  
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp
   return alist

def read_ints(n):
    int_list=[]
    with open(n+".txt") as f:
        for line in f:
            ints =  line.split()
            for i in ints:
                int_list.append(int(i))
    return int_list


n = sys.argv[1]

int_list = read_ints(n)

selectionSort(int_list)
