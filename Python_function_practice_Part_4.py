# 1 Write a Python function called max_num()to find the maximum of three numbers.
from audioop import mul


def max_num(x, y, z):
    #using max() built-in function
    return max([x,y,z])    


print(max_num(5,6,435))

# 2 Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(my_list):
    
    if len(my_list) == 0:
        return 0

    product = my_list[0]

    if len(my_list) > 1:
        #array slice syntax [1:]
        for i in my_list[1:]:
            product = product * i
    return product

print(mult_list([35]))
print(mult_list([3, 6, 7]))
print(mult_list([]))

# 3 Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    print(string[::-1])


rev_string("reversed")
rev_string("yvan eht nioJ")

# 4 Write a Python function called num_within() to check whether a number falls in a 
#given range.
#   The function accepts the number, beginning of range, and end of range (inclusive) 
#   as arguments.
#   Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, 
#   num_within(10,2,5) returns False.

def num_within(num, start, end):
    # +1 to include theh number in the range
    return num in range(start, end+1)

print(num_within(4,1,5))
print(num_within(5,3,5))
print(num_within(15,2,7))

# 5 Write a Python function called pascal() that prints out the first n rows of 
# Pascal's triangle
#   The function accepts the number n, the number of rows to print
#   Note : Pascal's triangle is an arithmetic and geometric figure first imagined by 
#   Blaise Pascal. Each number is the two numbers above it added together.

triangle = [[1],[1,1]]
def pascal(n):
    #base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        #fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            #create correct row, then add to triangle
            #(this row will be 1 larger thhan row before it)
            length = len(row_prev)+1
            for i in range(length):
                #first number is 1
                if i == 0:
                    row.append(1)
                    #intermediate numbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1] + triangle[row_number-1][i])
                    # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1 

    #print triangle
    for row in triangle:
        print(row)

pascal(2)
pascal(5)




  
     
