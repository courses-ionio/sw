import sys

def insertion_sort(arr):

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr

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

#print (int_list)
insertion_sort(int_list)
