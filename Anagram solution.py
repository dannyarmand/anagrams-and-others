#Checking if two strings are an anagram

def check(s1,s2):

    #we sort the strings and check them
    if(sorted(s1) == sorted(s2)):
        print ("The strings are anagrams.")
    else:
        print ("The strings aren't anagrams.")

#driver code
s1 = "listen"
s2 = "silent"
check(s1,s2)