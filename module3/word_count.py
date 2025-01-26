def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False


def main():
    #file_object = open('word.txt')
    #file_object.readline()
    total_line = 0
    total_e_words = 0
    for line in open('word.txt'):
        word = line.strip()
        total_line += 1
        print(word)
        if has_e(word):
            total_e_words += 1
    # strip removes whitespace characters—including 
    # spaces,tabs,and newlines—from the beginning and end of the string.
    print(f"the total line is {total_line}")
    print(f"the total line with e is {total_e_words}")


main()
