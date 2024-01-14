def caesar_cipher(str, offset):
    new_str = ""
    new_char = ""
    for idx in range(len(str)):
        if ord(str[idx])-int(offset) < 97:
            new_char = chr(ord(str[idx])-int(offset)+26)
        else:
            new_char = chr(ord(str[idx])-int(offset))
        new_str = new_str + new_char
    return new_str

word = input("Enter a string: ")
for idx in range(len(word)):
    while ord(word[idx]) < 97 or ord(word[idx]) > 122:
        word = input("Enter a string: ")

offset = input("Enter the offset: ")
while not offset.isdigit() or int(offset) > 26:
    offset = input("Enter the offset: ")

result = caesar_cipher(word, offset)
print(result)
