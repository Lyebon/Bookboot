import string

#Finding the most frequent letter
#Sorting the results
#Calculating letter frequencies as percentages

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = num_words(text)
    leters = count_chars(text)
    return show_mesages(book_path, words, leters)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_chars(text):
    lower_words = text.lower()
    char_count = { }
    alphabet = string.ascii_lowercase
    for char in lower_words:
        if char in alphabet:
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count


def num_words(text):
    words = text.split()
    return len (words)


def show_mesages(book, number, dic):
    print (f"--- Begin report of {book} ---")
    print (f"{number} words found in the document\n")
    print (f"The {dic} character was found {dic} times")
    print ("--- End report ---")



main()