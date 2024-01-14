def add_word(word):
    database.append(word)
    return database

def longest_word(word, count):
    idx = 0
    new_lst = []
    try:
        while len(new_lst) < int(count):
            temp_lst = sorted(word, reverse=True, key=len)
            if temp_lst.count(temp_lst[idx]) == 1:
                new_lst.append(temp_lst[idx])
            idx += 1
    except IndexError:
        print("")
    return new_lst

i = 0
database = []
final_lst = []

total_words = input("Enter the total number of words: ")
while not total_words.isdigit():
    total_words = input("Enter the total number of words again: ")

for i in range(int(total_words)):
    new_word = input("Enter a word: ")
    while new_word.isdigit():
        new_word = input("Enter a word again: ")
    initial_lst = add_word(new_word)
    i += 1

print(initial_lst)

list_count = input("Enter the number of longest unique words in final list: ")
while not list_count.isdigit():
        list_count = input("Enter the number of longest unique words again: ")

final_lst = longest_word(initial_lst, list_count)
print(final_lst)





