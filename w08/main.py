# 1. Name:
#      Celeste George
# 2. Assignment Name:
#      Lab 08: Sort Program
# 3. Assignment Description:
#      Program will read a list of names from a file and sort them.
# 4. What was the hardest part? Be as specific as possible.
#      While the program uses a straightforward sorting algorithm,
#       understanding and implementing more complex sorting algorithms
#       was the most challenging part for me.
# 5. How long did it take for you to complete the assignment?
#      4 hours


import json

def custom_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]

def main():
    file_name = input("What is the name of the file? ")
    
    # Read data from JSON file
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            if 'array' in data and isinstance(data['array'], list):
                names = data['array']
                if not names:
                    print("The 'array' field is empty in the JSON file.")
                    return
                custom_sort(names)  # Sort the list
                print("The values in {} are:".format(file_name))
                for name in names:
                    print("\t" + name)
            else:
                print("The JSON file doesn't contain a valid 'array' field.")
    except FileNotFoundError:
        print("File not found: {}".format(file_name))
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")

if __name__ == "__main__":
    main()