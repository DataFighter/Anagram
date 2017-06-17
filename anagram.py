import json
import argparse

# A map of each let to a prime number
# This is stored as a json that is also provided
prime_map = json.load(open('prime_map.json','r'))

def is_anagram(word_1 = None, word_2 = None):
    # Check to make sure the inputs are strings
    if type(word_1) != str or type(word_2) != str:
        raise Exception ('Incorrect parameter type. Plesase input strings')

    # multiply every letter's prime number
    def m (word):
        product = 1
        for w in word:
            prime = prime_map[w]
            product = product*prime
        return product

    # Check that each word was given
    if word_1 is not None and word_2 is not None:
            # Return true if the products are equal
            # Otherwise return false
            if m(word_1) == m(word_2):
                return True
            else:
                return False

    # Handle incorrect parameters
    else:
        raise Exception ('Not enough words inputed. Please input two words to check.')

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("word_1",type=str, help="The first word to be compared")
    parser.add_argument("word_2",type=str,  help="The second word to be compared")
    args = parser.parse_args()

    # Run anamgram function and print results
    if is_anagram(args.word_1,args.word_2):
        print ('Found two anagrams!')
    else:
        print ('Have not found anagrams.')
