# 1. Name:
#      Celeste George
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program will display all the prime numbers at or below a certain value.
#      It will first prompt the user for an integer. If the integer is less than 2, 
#      then the program will prompt the user for another number. The program will then
#      compute all the prime numbers below (& including) the given number. When finished,
#      the program will display the list of prime numbers.
# 4. What was the hardest part? Be as specific as possible.
#      Understanding the algorithm to find prime numbers was challenging. The logic of
#      checking for prime numbers and creating a list of primes.
# 5. How long did it take for you to complete the assignment?
#      4 hours

import math

def is_prime(num):
    #
    # check if a number is prime
    #
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_below_n(n):
    #
    # find all prime numebrs below (& including) a given number
    #
    assert n >= 2, "Input must be greater than or equal to 2."
    
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    
    return primes

def main():
    #
    # main function to execute the program
    #
    try:
        # prompt user for an integer
        user_input = int(input("This program will find all the prime numbers at or below N. Select that N: "))
        
        # validate user input
        assert user_input >= 2, "Input must be greater than or equal to 2."

        # compute and display prime numbers
        primes = find_primes_below_n(user_input)
        print(f"The prime numbers at or below {user_input} are {primes}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except AssertionError as e:
        print(f"Error: {e}")

# example run 1
main()

# example run 2
main()
