#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  
  # initialize the loop variables
  nums_l = len(nums)
  i = 1
  
  #loop through the list (in whatever state it is now)
  while i < nums_l: 
    if nums[i-1] == nums[i]:
      del nums[i-1]
      
      # reinitialize the loop variables after deleting the element from the list
      i = 1
      nums_l -= 1 # same as len(nums)
    else:
      i +=1
    
  return nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++

  if len(list1) <= len(list2):
    list_small = list1
    list_big = list2
  else:
    list_small = list2
    list_big = list1
  
  j = len(list_big)
  # reverse traverse he smaller list
  for elem_ls in reversed(list(list_small)):
    #print 'testing', elem_ls
    #print 'against', list_big[:j+1]
    # shorten the traversal of list_big to index j after every insertion of elem_s
    for index,elem_lb in reversed(list(enumerate(list_big[:j+1]))):
      if elem_ls <= elem_lb:
        if index == 0: # special case if we reach the begining of the list
          list_big.insert(index, elem_ls)
        continue
      
      #found the right index to insert  
      list_big.insert(index+1, elem_ls)
      list_small.pop(-1) # discard the element just inserted
      j = index # reset the index j to shorten the search space in list_big
      #print 'list big', list_big
      #print 'list small', list_small
      break
    
  return list_big

# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
