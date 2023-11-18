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
