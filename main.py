# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pyparsing import Word

# function to check if two strings are anagram or not
def find_anagram(word, anagram):

    # ask user to input words they want to check
    #word = input("Enter first word: ")
    #anagram = input("Enter second word: ")
    
    # the sorted strings are checked
    if (sorted(word)) == sorted(anagram):
        return True

    return False

# code to test function
Word = "silent"
anagram = "listen"
print (find_anagram(Word,anagram))
