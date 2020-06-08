import sys

def merge_sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L)  
        merge_sort(R)  
  
        i = j = k = 0
          
         
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1



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
merge_sort(int_list)

