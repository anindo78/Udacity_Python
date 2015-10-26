# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

test = [[1,2,3,4], 
        [2,4,1,3], 
        [3,1,4,2], 
        [4,3,2,1]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]


#Creating a helper function to find if a number is repeated twice
def dupl(m):
    dup = 0
    j = 0
    k = len(m)
    while j < k:
        if m[j] in m[j+1:k]:
            dup = dup + 1
        else:
            dup = dup
        j = j + 1
    return dup

#Creating a helper function to find call out invalid entries
def number(q):
    n = 0
    invalid = 0
    while n < len(q):
        if type(q[n]) is str or type(q[n]) is float:
            invalid = 1
        else:
            if q[n] < 1 or q[n] > len(q):
                invalid = 1
            #invalid = 1
        n = n + 1
    return invalid

#Creating a helper function to create n column lists from n lists
def columns(k):
    n = len(k);
    return [[ k[row][col] for row in range(0, n) ] for col in range(0, n) ]
            
     
            
           
def check_sudoku(p):
    n = 0
    x = 0
    q = columns(p)
    while n < len(p):
       if (dupl(p[n]) >= 1 or number(p[n]) >= 1) or (dupl(q[n]) >= 1 or number(q[n]) >= 1):
            x = x + 1
       else:
            x = x
       n = n + 1
    return x == 0
        
         
print check_sudoku(test)
#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False


