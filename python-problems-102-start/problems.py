import random
# to pass the test function, please return a string of 'string' from then function
# eg: test() => 'string'
def test():
    return "string"

# write a function to remove all empty values (False, [], {}, (), "", None) EXCEPT 0 from an array.
# It should handle complex data types eg: {}, [] etc.
# eg: [0, False, "", [], {}, 1, 'Kevin'] => [0, 1, 'Kevin'];
def remove_blank(list):
    new_list = []
    
    for item in list:
        
        if item or ((type(item) == type(3)) and item == 0):
            new_list.append(item)

    return new_list

# write a function to return a random element from an list
# eg: [1,"elephant", "apple", 67] => "elephant"
def random_element(list):
    
    random_index = random.randrange(0, len(list))

    return list[random_index]

# write a function that returns the second lowest and second highest number in an list
# eg: [1,2,3,4,5,6,7,8] => [2,7]
def second_lowest_second_highest(list):

    list.sort()
    required_list = [list[1], list[-2]]

    return required_list

# write a function that will convert a price into coins needed to make up that price
# the coins available are 1, 2, 5, 10, 20, 50, 100
# the function should use the smallest number of coins possible
# eg: coins(1.99) => [100, 50, 20, 20, 5, 2, 2]
def coins(price):

    coins = [100, 50, 20, 10, 5, 2, 1]
    coins_needed = []
    price *= 100

    while price > 0:

        for coin in coins:
            
            if price >= coin:
                coins_needed.append(coin)
                price -= coin
                break

    return coins_needed

# write a function to merge two lists and remove duplicates
# eg: mergeUnique([9,8,8,9], [7,8,8,7]) => [9,8,7]
def merge_unique(list1, list2):
    
    list1.extend(list2)
    
    for index, item in enumerate(list1):
        if list1.count(item) >= 2:
            list1.remove(list1[index])

    return list1

# write a function to find the first n fibonacci numbers
# the fibonacci sequence is a series of numbers, each number is the sum of the last two
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 etc...
# eg: fibonacci(4) => [0,1,1,2]; fibonacci(8) => [0, 1, 1, 2, 3, 5, 8, 13];

def fibonacci(n):
    
    fibonacci_list = [0, 1]
    accumulator = n

    if n == 1:
        fibonacci_list = [0]
    
    elif n <= 0:
        fibonacci_list = []
    
    else:
        while accumulator > 2:
            
            num_to_append = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(num_to_append)
            accumulator -= 1

    return fibonacci_list