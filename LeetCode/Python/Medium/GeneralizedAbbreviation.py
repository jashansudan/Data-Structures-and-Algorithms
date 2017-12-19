class Solution(object):
    def generateAbbreviations(self, word):
        result = []
        self.abbreviationsHelper(word, 0, "", result)
        return result

    def abbreviationsHelper(self, word, count, curr_string, result):
        if word == "":
            if count > 0:
                curr_string += str(count)
            result.append(curr_string)
        else:
            self.abbreviationsHelper(word[1:], count + 1, curr_string, result)
            if count == 0:
                self.abbreviationsHelper(word[1:], 0, curr_string + word[0], result)
            else:
                self.abbreviationsHelper(word[1:], 0, curr_string + str(count) + word[0], result)
