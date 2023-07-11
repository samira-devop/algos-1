# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    return sorted(s1) == sorted(s2) and not any(s1.count(char) != s2.count(char) for char in set(s1))


  
"""
aother solution will be to use a dictionary:
looking things up requires key(instant) O(1)
initialize a dict to hold the letters present in first string
loop thru second string and check each letter with the dict

if len(s1) != len(s2):
return False

count ={} here we initialsed our dictionary.
for char in s1:
  if char not in count:
    count[char] = 1
  else:
    count[char] =+ 1
#Loop thru seconds stirng and ckeck each letter with the dict  
  for char in s2:
    if char not in count:
      return False
    else:
      count[char] -= 1
      if cont[char] < 0:
      retun False  
  return True
  
"""


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
