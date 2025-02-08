'''
   CS5001
   Lab 4
   Spring 2025
   Sia Xuan
'''
from words_in_sentence import take_input, separate_words, \
     get_unique_words, get_frequency, output_result


def main():
    sentence = take_input()
    word_list = separate_words(sentence)
    unique_words = get_unique_words(word_list)
    frequency = get_frequency(word_list, unique_words)
    output_result(word_list, unique_words, frequency)
    

if __name__ == "__main__":
    main()

