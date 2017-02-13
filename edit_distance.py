#!$HOME/anaconda3/bin/python3 -tt

# costs of operations

def delete():
  return 1

def insert():
  return 1

def sub():
  return 1

def ed(str1,str2):
  m = len(str1)
  n = len(str2)

  # matrix of distances for strings of all length
  Dist_m = [[0 for i in range(n+1)] for j in range(m+1)]

  #print(Dist_m)

  # fill in the first row
  # cost to to reduce any length of string in str1 to 0 length
  for i in range(m+1):
    for k in range(i):
      Dist_m[i][0] = Dist_m[i][0] + delete()

  # fill in the first column
  # cost to create length of strings 0 to n 
  for j in range(n+1):
    for k in range(j):
      Dist_m[0][j] = Dist_m[0][j] + insert()

  # start filling in the rest of the costs
  for i in range(1, m+1):
    for j in range(1, n+1):

      if str1[i-1] == str2[j-1]:    
        Dist_m[i][j] = Dist_m[i-1][j-1]   # cost is same
      else:
        # minimum of the following three conditions
        # Dist_m[i][j-1] + insert a char at the jth position
        # Dist_m[i-1][j] + delete a char from the ith position
        # Dist_m[i-1][j-1] + substitute the char at the ith and jth position
        Dist_m[i][j] = min(min(Dist_m[i][j-1] + insert(), Dist_m[i-1][j] + delete()), Dist_m[i-1][j-1] + sub())
    
  print(Dist_m)
  return Dist_m[m][n]

def main():

  f_h = open("strings.dat","r")
  
  str_list = [s[:-1] for s in f_h]  # get rid of the -1 while reading

  edit_distance = ed(str_list[0], str_list[1])

  print("edit distance between -"+str_list[0]+"- and - "+str_list[1]+" = "+str(edit_distance)) 
 
if __name__ == '__main__':
  main()
