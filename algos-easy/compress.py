# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
    if len(s) == 0:
        return ""

    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result

# TEST CASE
print(compress('aabcccccaaa'))  # a2b1c5a3

    




# TEST CASES
print(compress('ccaaatsss')) # -> '2c3at3s'
print(compress('ssssbbz')) # -> '4s2bz'
print(compress('ppoppppp')) # -> '2po5p'
print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));  # -> '127y'


"""
Approche N2:
s+= '.' #this will account the last letter
we use a 2 pointer solution
 i = 0 -> end   (trachs the letter)
 j = 0 -> end   (trakcs occurrences)
 
# Initialize a list the stote result
result = []
i, j = 0, 0

# while loop to iterate thru string
while j < len(S):
    if s[i] == s[j]:
        j== 1
    else:
        letter_count = j - i
        if letter_count ==1:
            result.append(s[i])
        else:
            result.apppend(str(letter_count))
            result.append(s[i]
        i = j 
return ''.join(result)
"""