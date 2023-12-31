# 1. Name:
#      Celeste George
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Implement the advanced search algorithm described in Lab 05. It will prompt
#      the user for a filname. We will read the contents of the file into a list.
#      The program will then prompt the user for a word to search for in the file.
#      And ultimately telling the user if the word was found.
# 4. Algorithmic Efficiency
#      The algorithmic efficiency of binary search is O(log n) where 'n' is the number
#      of elements in the list being searched. It is especially useful when dealing with
#      with large datasets or when you need to perfrom repeated searches.
# 5. What was the hardest part? Be as specific as possible.
#      Trying to get the program to read the files and to find a way to store it.
#      After figuring that out I had to figure out a way for the code to search through
#      the array to find the word the user was looking for.
# 6. How long did it take for you to complete the assignment?
#      2.5 hours

import json

def read_file(filename):
    try:
        # open the file from input, read the contents, close the file, return contents in an array
        with open(filename, 'r') as file:
            data = json.load(file)
            if 'array' in data and data['array']:
                return data['array']
            else:
                print("The file you are searching is empty.")
                return []
    except FileNotFoundError:
        # print error code and return empty list
        print("File not found. Please check the filename and try again.")
        return []

def advanced_search(word_list, search_word):
    start_page = 0
    end_page = len(word_list) - 1

    while start_page <= end_page:
        # calculate middle page as int, retrive middle word from int array
        middle_page = (start_page + end_page) // 2
        middle_word = word_list[middle_page]

        if middle_word == search_word:
            return True
        elif middle_word < search_word:
            # narrowing the search to the upper half
            start_page = middle_page + 1
        else:
            # narrowing the search to the lower half
            end_page = middle_page - 1

    return False

def main():
    # prompt for the json filename
    filename = input("What is the name of the file? ")
    word_list = read_file(filename)

    # if file not found end program
    if not word_list:
        return

    # prompt for word to look for
    search_word = input("What name are we looking for? ")
    found = advanced_search(word_list, search_word)

    # if success print found statement, else show error code for no word in file
    if found:
        print(f"We found {search_word} in {filename}.")
    else:
        print(f"{search_word} was not found in {filename}.")

if __name__ == "__main__":
    main()
