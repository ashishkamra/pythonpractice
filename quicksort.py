import random

# partition implementation
# ref: https://www.cs.auckland.ac.nz/software/AlgAnim/qsort1a.html 
def partition(nlist, lo, hi):
  pivot_index = random.randint(lo,hi)  
  pivot = nlist[pivot_index]
  left = lo
  right = hi
  while left < right:
    while nlist[left] <= pivot:
      if left < len(nlist) - 1:
        left += 1
      else:
        break;
    while nlist[right] > pivot:
      right -= 1
    
    if left < right:
      tmp = nlist[left]
      nlist[left] = nlist[right]
      nlist[right] = tmp
  
  # right reprsents the new pivot to be used
  if pivot_index != right:
    nlist[pivot_index] = nlist[right]
    nlist[right] = pivot

  return right

def quicksort(nlist, lo, hi):
  if lo < hi:
    #print(p)

    # iterative quick sort
      
    # recursive quick sort
    p = partition(nlist, lo, hi)
    quicksort(nlist, lo, p-1)
    quicksort(nlist, p+1, hi)

def main():

  try:
    f = open("numbers.dat","r")
  except(IOError):
    print("file does not exist")
    return -1
  
  # list comprehension to read the numbers in a list
  num_list = [int(num) for num in f]

  random.shuffle(num_list)

  print("Unsorted list")
  print(num_list)

  quicksort(num_list, 0, len(num_list) - 1)

  print("sorted list")
  print(num_list)  

if __name__ == '__main__':
  main()
