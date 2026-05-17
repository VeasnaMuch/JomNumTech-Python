def factorial(n):
    # Base case: 0! or 1! is 1
    if n <= 1:
        return 1
    # Recursive case: n * (n-1)!
    else:
        return n * factorial(n - 1)
    
def callMe(param_1, param_2):
    print(f"{param_1}, {param_2}")


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def sum_numbers(*args):
    return sum(args)

# Pass any number of arguments
print(sum_numbers(10, 20, 30, 40)) # Output: 100

# Pass multiple named arguments
print_info(name="Bob", age=25, city="New York")


callMe(param_2="Hello", param_1="Digital")
#print(factorial(5))  # Output: 120