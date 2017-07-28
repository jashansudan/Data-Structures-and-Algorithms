class Solution(object):
    def isPalindrome(self, s):
        valid = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]
        if s == None or len(s) < 2:
        	return True
        start = 0
        end = len(s) - 1
        while (start < end):
        	while (s[start].lower() not in valid and start < end):
        		start += 1
        	while(s[end].lower() not in valid and start < end):
        		end -= 1
        	if(s[start].lower() != s[end].lower()):
        		return False
        	start += 1
        	end -= 1

        return True
