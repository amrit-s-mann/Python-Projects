def create_strings_from_characters(database, str1, str2):
    char_count = 0
    final_output = 0
    output_string1 = 0
    output_string2 = 0
    database1 = database.copy()
    database2 = database.copy()

    for idx in range(len(str1)):
        char_count = database1.get(str1[idx])
        if int(char_count) > 0:
            database1[str1[idx]] = char_count - 1
            output_string1 = 1
        else:
            output_string1 = 0
            break

    char_count = 0

    for idx in range(len(str2)):
        char_count = database2.get(str2[idx])
        if int(char_count) > 0:
            database2[str2[idx]] = char_count - 1
            output_string2 = 1
        else:
            output_string2 = 0
            break

    final_output = output_string1 + output_string2
    return final_output

frequencies = {"h": 2, "e": 1, "l": 1, "r": 4, "a": 3, "o": 2, "d": 1, "w": 0}

string1 = input("Enter the first string: ")
while string1.isdigit():
    string1 = input("Enter the first string again: ")

string2 = input("Enter the second string: ")
while string2.isdigit():
    string2 = input("Enter the second string again: ")

result = create_strings_from_characters(frequencies, string1, string2)
print(result)
    
