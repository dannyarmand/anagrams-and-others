
def count_vowels_consonants(text):
    count_vowels=0
    count_consonants=0
    
    vowels = ["a","e","i","o","u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z"]
    for i in text:
        if i in vowels:
            count_vowels +=1
        elif i in consonants:            
            count_consonants +=1
        
    return (count_vowels,count_consonants)

print(count_vowels_consonants("a2#$%^&33rrrwe"))



            
        