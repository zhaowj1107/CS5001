'''
   CS5001
   Lab 4
   Spring 2025
   Sia Xuan
'''


def take_input() -> str:
    sentence = input("Enter a sentence ")
    return sentence
        

def separate_words(sentence: str) -> list[str]:
    '''
    >>> separate_words("This is a test")
    ['this', 'is', 'a', 'test']
    '''
    '''
    This function takes a sentence
    returns a list of words
    in lowercase without punctuation marks
    '''
    words = ""
    for letter in sentence:
        if letter.isspace() or letter.isalnum():
            words += letter
    return words.lower().split()
    

def get_unique_words(separate_words: list[str]) -> list[str]:
    '''
    >>> get_unique_words(['this', 'is', 'this', 'a', 'test'])
    ['this', 'is', 'a', 'test']
    '''
    unique_words = []
    for word in separate_words:
        if not word in unique_words:
            unique_words.append(word)
    return unique_words


def get_frequency(separate_words: list[str], unique_words: list[str]) -> list[int]:
    '''
    >>> get_frequency(['this', 'is', 'this', 'a', 'test'], ['this', 'is', 'a', 'test'])
    [2, 1, 1, 1]
    '''
    frequency = []
    for standard_word in unique_words:
        count = 0
        for word in separate_words:
            if word == standard_word:
                count += 1
                print(f"{word}:{count}")
            frequency.append(count)
    return frequency

def get_frequency_new(separate_words: list[str], unique_words: list[str]) -> list[int]:
    '''
    >>> get_frequency(['this', 'is', 'this', 'a', 'test'], ['this', 'is', 'a', 'test'])
    [2, 1, 1, 1]
    '''
    frequency = []
    for standard_word in unique_words:
        count = 0
        for word in separate_words:
            if word == standard_word:
                count += 1
                print(f"{word}:{count}")
        frequency.append(count)
    return frequency

def output_result(word_list: list[str],
                  unique_words: list[str],
                  frequency: list[int]):
    '''
    # don't test this
    >> output_result(['this', 'is', 'a', 'test'], ['this', 'is', 'a', 'test'], [1, 1, 1, 1])
    0.	this
    1.	is
    2.	a
    3.	test
    this : 1
    is : 1
    a : 1
    test : 1
    '''
    index = 0
    print("You types 10 words in that sentence.")
    print("Here are the individual words:")
    for word in word_list:
        print(str(index) + ".\t" + word_list[index])
        index += 1
    i_frequency = 0
    print("The frequency of each word is:")
    for uniword in unique_words:
        print(uniword, ":", frequency[i_frequency])
    


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    get_frequency_new(['this', 'is', 'this', 'a', 'test'], ['this', 'is', 'a', 'test'])
