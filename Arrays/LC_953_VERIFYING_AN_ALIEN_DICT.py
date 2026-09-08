# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        u_hash = {}
        for i, j in enumerate(order, start=1):
            u_hash[j] = i

        p = 0
        while p < len(words) - 1:
            flag = False
            word1 = words[p]
            word2 = words[p + 1]
            i = 0
            j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    pos1 = u_hash.get(word1[i])
                    pos2 = u_hash.get(word2[j])
                    if pos1 > pos2:
                        return False
                    else:
                        i += 1
                        j += 1
                        flag = True
                        break
                i += 1
                j += 1

            if not flag and len(word1) > len(word2):
                print(i)
                print(j)
                return False
            p += 1
        return True
