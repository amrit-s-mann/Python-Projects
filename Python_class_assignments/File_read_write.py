with open("Video_Practice/Sample_data/new_file.txt", "r+") as file:
    
    lines = file.read()
    print(lines)

    escape_chars_removed = lines.replace("\n", " ").replace("\t", " ")
    spl_chars_removed = escape_chars_removed.replace(".", "").replace(",", "").replace("-", "").replace("!", "")

    word_count = 0
    words = spl_chars_removed.split(" ")
    for word in words:
        if word != "":
            word_count += 1
    print(word_count)

with open("Video_Practice/Sample_data/write_num_squares.txt", "w") as file:
    for i in range(1, 51):
        file.write(str(i*i)+"\n")