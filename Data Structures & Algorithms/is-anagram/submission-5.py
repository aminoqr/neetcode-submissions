from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_map = defaultdict(int)

        for c in s:
            letter_map[c] += 1
        
        for c in t:
            if c not in letter_map:
                return False
            
            letter_map[c] -= 1
            if letter_map[c] == 0:
                del letter_map[c]
        
        return True if letter_map == {} else False
        