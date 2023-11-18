# 1. Name:
#      Celeste George
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      Python program which will prompt the user for a positive integer n 
#      and then display the nth Francois number.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part would be error handling, espically the assertions and
#      exceptions. Understanding and implementing 'assert' and 'try/except' effectively
#      in order to flow with the code and make it clear of bugs, but also readable.
# 5. How long did it take for you to complete the assignment?
#      5 hours


def francois(num):
    assert isinstance(num, int) and num > 0, "Input must be a positive integer"
    
    if num == 1:
        return 2
    elif num == 2:
        return 1
    
    # Initialize a list to store computed values
    memo = [0] * (num + 1)
    memo[1] = 2
    memo[2] = 1
    
    # Use memoization to avoid redundant computations
    for i in range(3, num + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[num]

def main():
    try:
        n = int(input("Which Francois number would you like to see? "))
        assert n > 0, "Input must be a positive integer"
        result = francois(n)
        print(f"Francois number {n} is {result}.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except AssertionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
