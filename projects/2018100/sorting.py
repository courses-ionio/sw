import os
import getopt, sys
import numpy as np

# ---------- Partition ----------
def partition(arr, low, high):
  i = (low-1)
  pivot = arr[high]
  
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return (i+1)

# ---------- Quick Sort ----------
def quickSort(arr, low, high):
  if len(arr) == 1:
    return arr
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)

# ---------- Merge ----------
def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m
  
  L = [0] * (n1)
  R = [0] * (n2)
  
  for i in range(0 , n1):
    L[i] = arr[l + i]
  
  for j in range(0 , n2):
    R[j] = arr[m + 1 + j]
  
  i = 0
  j = 0
  k = l
  
  while i < n1 and j < n2 :
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

# ---------- Merge Sort ----------
def mergeSort(arr,l,r):
  if l < r:
  
    m = (l+(r-1))//2
  
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

# ---------- ShellSort ----------
def shellSort(arr):
  n = len(arr)
  interval = n // 2
  while interval > 0:
    for i in range(interval, n):
      temp = arr[i]
      j = i
      while j >= interval and arr[j - interval] > temp:
        arr[j] = arr[j - interval]
        j -= interval
      arr[j] = temp
    interval //= 2

# ---------- Sorting Algorithms ----------
def run_sorting_algorithm(algorithm, file_name, def_name, path):

  arr = np.random.randint(1000000, size=(100))
  np.savetxt('{}/{}-random.txt'.format(path, file_name), np.around(arr),fmt='%.0f',delimiter='\t')

  if file_name == 'quickSort' or file_name == 'mergeSort':
    k = len(arr)
    '{}'.format(def_name(arr, 0, k-1))
  else:
    '{}'.format(def_name(arr))
  np.savetxt('{}/{}-order.txt'.format(path, file_name), np.around(arr), fmt='%.0f',delimiter='\t')

# ---------- Main Code ----------
l = 100
path = str(l)
if not os.path.exists(path):
  os.mkdir(path)

full_cmd_arguments = sys.argv

argument_list = full_cmd_arguments[1:]

print (argument_list)

short_options = "qms"
long_options = ["quick_sort", "merge_sort", "shell_sort"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-q", "--quick_sort"):
      print ("----- Quick Sort -----")
      run_sorting_algorithm('Quick Sort', 'quickSort', quickSort, path)
    elif current_argument in ("-m", "--merge_sort"):
      print ("----- Merge Sort -----")
      run_sorting_algorithm('Merge Sort', 'mergeSort', mergeSort, path)
    elif current_argument in ("-s", "--shell_sort"):
      print ("----- Shell Sort -----")
      run_sorting_algorithm('Shell Sort', 'shellSort', shellSort, path)