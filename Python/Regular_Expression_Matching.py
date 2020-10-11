# Problem link: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str, cache = {}) -> bool:
        if not p:
            return not s
        
        key = "{0}#{1}".format(s, p)
        
        if key in cache:
            return cache[key]
        
        if p[-1] == "*":
            if self.isMatch(s, p[:-2], cache): # no match
                cache[key] = True
                return True
            
            if s and len(p) >1 and (s[-1] == p[-2] or p[-2] == "."): # no match
                if self.isMatch(s[:-1], p, cache):
                    cache[key] = True
                    return True
        else:
            if s and (s[-1] == p[-1] or p[-1] == "."):
                if self.isMatch(s[:-1], p[:-1], cache):
                    cache[key] = True
                    return True
        cache[key] = False
        return False
