#CHECKING IF A STRING IS A PANAGRAM

import string
def ispanagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

        return True

#Driver Code:

string = "the quick brown fox jumps over the lazy dog"
if(ispanagram(string) == True):
    print ("Yes, it is a Panagram!")
else:
    print("No, sorry, not this time!")