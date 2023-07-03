# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    list1 = sorted(s1)
    list2 = sorted(s2)
    return list1 == list2


# # TEST CASES
print(anagrams('restful', 'fluster')) # -> True
print(anagrams('cats', 'tocs')) # -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('po', 'popp')) # -> False
print(anagrams('pp', 'oo')) # -> False
