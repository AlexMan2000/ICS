def get_anagrams(word,vocabulary):
    pass

if __name__ == "__main__":
    # Read english.txt, create list of words
    all_words = open("anagrams_english.txt","r").read().split("\n")
    # Read input.txt, get list of test cases
    input_list = open("anagrams_input.txt","r").read().split("\n")

    for word in input_list:
        result = get_anagrams(word, all_words)
        print(word,":",result)


"""
TEST set answers:

cater : ['carte', 'caret', 'crate', 'trace', 'recta', 'react']
race : ['acre', 'care']
pants : []
tea : ['eta', 'eat', 'ate']
sound : ['nodus']
ring : ['grin']
road : []
"""
