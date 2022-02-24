import time
import sys
"""------------------------------------------------------------------------------------------"""
"""---------------------------Bubble--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""

def Bubble(array):

    compara = 0
    swap = 0
    inicio = time.time()
    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            compara += 1
            if array[current] > array[current + 1]:
                swap += 1
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break
    final = time.time()
    tempo = (final - inicio)
    return compara, swap, tempo
    #print(array)

"""------------------------------------------------------------------------------------------"""
"""---------------------------Selection--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""

def Selection(array):
    compara = 0
    swap = 0
    inicio = time.time()
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            compara +=1
            if array[right] < array[min_index]:
                min_index = right
        swap +=1
        array[index], array[min_index] = array[min_index], array[index]
    final = time.time()
    tempo = (final - inicio)
    return compara, swap, tempo
    #print(array)
"""------------------------------------------------------------------------------------------"""
"""---------------------------Insertion--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""
def Insertion(array):
    compara = 0
    swap = 0
    inicio = time.time()
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            compara += 1
            array[p] = array[p - 1]
            swap+=1
            p -= 1

        array[p] = current_element
        swap+=1
    final = time.time()
    tempo = (final - inicio)
    return compara, swap, tempo
    #print(array)
"""------------------------------------------------------------------------------------------"""
"""---------------------------MergeSort--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""

def MergeSort(array):
    swap=0


    inicio = time.time()
    compara = mergeSort(array)
    final = time.time()
    tempo = (final-inicio)
    return compara, swap, tempo
    #print(array)

def mergeSort(arr):
    compara = 0

    if len(arr) >1:
        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        compara = i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                compara+=1
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    return compara

"""------------------------------------------------------------------------------------------"""
"""---------------------------Quick Sort--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""
sys.setrecursionlimit(1500)

def QuickSort(alist):
  swap=0
  compara=0

  inicio = time.time()
  swap, compara = quickSortHelper(alist,0,len(alist)-1)
  final = time.time()
  tempo = (final - inicio)
  return compara, swap, tempo

def quickSortHelper(alist,first,last):
  swap = 0
  compara = 0
  if first<last:
      splitpoint, swap, compara = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)
  return swap, compara

def partition(alist,first,last):

  pivotvalue = alist[int((first+last)/2)]
  leftmark = first+1
  rightmark = last
  done = False
  compara = 0
  swap = 0

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1
          compara += 1
      else:
          compara+=1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1
          compara+=1
      else:
          compara+=1

      if rightmark < leftmark:
          done = True
      else:
          swap+=1
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp
  swap+=1

  return rightmark, swap, compara


"""------------------------------------------------------------------------------------------"""
"""---------------------------Countting Sort--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""


def CountSort(array):
    swap = 0
    compara = 0

    inicio = time.time()
    n = len(array)
    maxval = max(array)
    m = maxval + 1
    count = [0] * m  # init with zeros
    for a in array:
        count[a] += 1  # count occurences
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    final = time.time()
    tempo = (final-inicio)
    return compara, swap, tempo
    #print(array)

"""------------------------------------------------------------------------------------------"""
"""---------------------------Bucket Sort--------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------"""


def Bucket_sort(alist):
    swap = 0
    compara = 0
    inicio = time.time()
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)
        compara+=1
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        mergeSort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    final = time.time()
    tempo = (final-inicio)
    return compara, swap, tempo
    #print(result)
