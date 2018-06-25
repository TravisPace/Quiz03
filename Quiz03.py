#1
def dot(vector01,vector02):
  '''
  This function calculates the dot product of the two vectors.
  '''
  C = [ ]
  #C is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
  #If the lengths of the vectors are not equal to each other, then the algorithim does not compute and returns none.
  for i in range(len(vector01)):
   #For the length of the vector i.
    C.append(vector01[i] * vector02[i])
    #multiplies each element together and creates a list C.
  D = 0
  #A new integer D is made.
  for i in range(len(C)):
    D = D + C[i]
  return D
  #The function then adds the elements in C toghether to get a single integer, D.
  
vector01 = [1,2]
vector02 = [3,4]
print(dot(vector01,vector02))

vector010 = [2,3,4]
vector020 = [1,2]
print(dot(vector010,vector020))

#2
def vecSubtraction(vector01,vector02):
  '''
  This function adds to vectors together.
  '''
  A = [ ]
  #A is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
  #If the lengths of the lists vector01 and vector02 do not equal each other, then this prints an error and returns none.
  for i in range(len(vector01)):
    A.append(vector01[i] - vector02[i])
    #This subtracts the lengths of vector01 and vector02 and adds each element of the list together.
  return A
  #This returns the list A.

vector01 = [1,2]
vector02 = [3,4]
print(vecSubtraction(vector01,vector02))

vector010 = [2,3,4]
vector020 = [1,2]
print(vecSubtraction(vector010,vector020))

#3
def scalarMultVec(scalar,vector):
  '''
  This function takes a scalar and a vector and multiplies them together.
  '''
  if type(scalar) == list:
    print('error')
    return None
  #If the scalar is a list, then the algorithim will print error and return none.
  A = [ ]
  #A is an empty list.
  for i in range(len(vector)):
    #For the length of the vector.
    A.append(vector[i] * scalar)
    #For each element in length i, multiply by the scalar.
  return A
  #This creates a new list for A and returns A.

scalar = 2
vector = [1,2]
print(scalarMultVec(scalar,vector))
      
scalar01 = [1,2]
vector01 = [3,4]
print(scalarMultVec(scalar01,vector01))

#4
def infNorm(vector):
  '''
  This takes the infinity norm of the vector.
  '''
  result = 0
  #Result is equal to no integer.
  for i in range(len(vector)):
  #For every element in the vector.
    if result <= abs(vector[i]):
    #This takes each element of the vector and sees if it greater than or equal to the previous element in the vector list.
      result = abs(vector[i])
      #If the result is greater than or equal to than the previous element, then the element becomes the result.
  return result
  #This returns the integer as the result.
  
vector = [3,-4]
print(infNorm(vector))

vector1 = 9
print(infNorm(vector1))

#5
def normalize(vector):
  '''
  This function normalizes the vector
  '''
  result = infNorm(vector)
  if result == 1 or result == 0:
    return vector
  #If the result is equal to 1 or zero from the infinity norm function, then this will return the vector.
  scalar = 1/result
  B = scalarMultVec(scalar,vector)
  #This takes the scalar multiplication vector function and runs it to get B, B is the vector and scalar is scalar.
  return B
  #This returns the vector B.

vector = [0,2,-6]
print(normalize(vector))

vector1 = -18
print(normalize(vector1))
