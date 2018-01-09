class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        letter_count = collections.Counter(''.join([i.lower() for i in licensePlate if i.isalpha()]))
        min_length = float('inf')
        min_word = ""
        for word in words:
            curr_count = collections.Counter(word.lower())
            contains_all_characters = True
            for char in letter_count:
                if curr_count[char] < letter_count[char]:
                    contains_all_characters = False
                    break
            if contains_all_characters and len(word) < min_length:
                min_length = len(word)
                min_word = word
        return min_word
