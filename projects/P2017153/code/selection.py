import sys

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

def read_ints(n):
	int_list=[]
	with open(n+".txt") as f:
		for line in f:
			ints = line.split()
			for i in ints:
				int_list.append(int(i))
	return int_list


n = sys.argv[1]

int_list = read_ints(n)

#print (int_list)
selection_sort(int_list)
