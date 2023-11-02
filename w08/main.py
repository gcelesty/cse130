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

# function to read JSON data from a file and return the list
def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            assert 'array' in data, "JSON file must contain 'array' key"
            names = data['array']
            assert isinstance(names, list), "Value under 'array' key must be a list"
            return names
    except FileNotFoundError:
        assert False, f"File '{file_name}' not found"
    except json.JSONDecodeError:
        assert False, "Invalid JSON format in the file"

# function to sort and display the list
def sort_and_display(names):
    names.sort()
    for name in names:
        print("\t" + name)

# fain program
if __name__ == "__main__":
    file_name = input("What is the name of the file? ")
    names = read_json_file(file_name)
    if names:
        print("The values in", file_name, "are:")
        sort_and_display(names)
