# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for i in s:
            s_hash[i] = s_hash.get(i, 0) + 1
        for j in t:
            t_hash[j] = t_hash.get(j, 0) + 1

        return s_hash == t_hash
