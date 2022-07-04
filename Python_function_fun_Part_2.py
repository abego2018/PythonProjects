
# 1 arb_args  - Takes in any number of arguments and prints them one 
# at a time.
def arb_args (*movies):
    print(movies)

arb_args("Apple", "Orange", "Pineapple")

# 2 inner_functionTakes in two integers. Two nested functions should 
# perform separate, distinct math operations using the integers. The 
# result of both nested functions should then be added together and 
# printed.
def inner_func(num):

    # inner function definition
    def plus_three (inner_num):
        return inner_num + 3
    # inner function call
    new_num =  plus_three(num) 

    # returned value based on inner
    return new_num
# will print 8
print(inner_func(5))


# 3 lunch_lady - Takes in two strings: a student's name and their lunch
#  preference. The function should print both strings. If a lunch 
# preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, meal_pref="Mystery Meat"):
    print (name, meal_pref)

# leaving default value
lunch_lady("John")
# overriting default with second argument
lunch_lady("Amy", "Pizza")

# 4 Multiple returns sum_n_product - Accepts two integers and returns both 
# the sum and the product.
def sum_n_product(num1, num2):
    new_sum = num1 + num2
    new_prod = num1 * num2
    return new_sum, new_prod

print(sum_n_product(4,6))

# 5 alias_arb_args - Should be arb_args but assigned an alias. Remember, 
# variables can hold functions in Python just like they can in JS. 
# Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

#6 arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum/(len(args))
    

print("The mean for 2,6,8,11 is:")
print(arb_mean(2,6,8,11))

#7 arb_longest_string - Accepts any number of strings and returns the 
# longest one.

def arb_longest_string(*strings):
    longest_string = ""
    for i in strings:
        if len(i)>len(longest_string):
            longest_string = i
    return i   

print("The longest string is:")
print(arb_longest_string("apples", "oranges","bananas", "pineapples"))