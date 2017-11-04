class Solution:
    def isOneEditDistance(self, s, t):
        if abs(len(s) - len(t)) > 1:
            return False
        diff = 0
        s_ptr = 0
        t_ptr = 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] != t[t_ptr]:
                diff += 1
                if diff > 1:
                    return False
                if len(s) != len(t):
                    if len(s) > len(t):
                        s_ptr += 1
                    else:
                        t_ptr += 1
                    continue
            t_ptr += 1
            s_ptr += 1
            
        if abs(len(s) - s_ptr) + abs(len(t) - t_ptr) + diff > 1:
            return False
        if diff == 0 and s_ptr == len(s) and t_ptr == len(t):
            return False
        return True
