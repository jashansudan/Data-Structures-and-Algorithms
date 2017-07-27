Class Solution(object):
	def longestCommonPrefix(self, strs):
		if strs is None or len(strs) == 0:
			return ''
		longestPrefix = strs[0]
		for i in range(1, len(strs)):
			while(strs[i].find(longestPrefix) != 0):
				longestPrefix = longestPrefix[:-1]
		return longestPrefix
