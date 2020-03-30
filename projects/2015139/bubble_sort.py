import sys

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
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

bubble_sort(int_list)

