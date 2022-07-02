
# 1 arb_args
def arb_args (*movies):
    print(movies)

arb_args("Apple", "Orange", "Pineapple")

# 2 inner_function
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


# 3 default args
def lunch_lady(name, meal_pref="Mystery Meat"):
    print (name, meal_pref)

# leaving default value
lunch_lady("John")
# overriting default with second argument
lunch_lady("Amy", "Pizza")

# 4 Multiple returns
def sum_n_product(num1, num2):
    new_sum = num1 + num2
    new_prod = num1 * num2
    return new_sum, new_prod

print(sum_n_product(4,6))

# 5 alias_args






#recursion

def find_fact(num):

    #base case
    if num ==1:
        return 1


    else:
        return (num * find_fact(num-1))

n=5

print(find_fact(n))


