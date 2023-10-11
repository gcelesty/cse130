import json

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['array']
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return []

def advanced_search(word_list, search_word):
    start_page = 0
    end_page = len(word_list) - 1

    while start_page <= end_page:
        middle_page = (start_page + end_page) // 2
        middle_word = word_list[middle_page]

        if middle_word == search_word:
            return True
        elif middle_word < search_word:
            start_page = middle_page + 1
        else:
            end_page = middle_page - 1

    return False

def main():
    filename = input("What is the name of the file? ")
    word_list = read_file(filename)

    if not word_list:
        return

    search_word = input("What name are we looking for? ")
    found = advanced_search(word_list, search_word)

    if found:
        print(f"We found {search_word} in {filename}.")
    else:
        print(f"{search_word} was not found in {filename}.")

if __name__ == "__main__":
    main()
