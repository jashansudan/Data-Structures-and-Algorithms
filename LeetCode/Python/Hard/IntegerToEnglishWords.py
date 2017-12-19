class Solution:
    below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        return self.helper(num)

    def helper(self, num):
        result = ""
        if num < 10:
            result = self.below_ten[num]
        elif num < 20:
            result = self.below_twenty[num - 10]
        elif num < 100:
            result = self.tens[num / 10] + " " + self.helper(num % 10)
        elif num < 1000:
            result = self.helper(num / 100) + " Hundred " + self.helper(num % 100)
        elif num < 1000000:
            result = self.helper(num / 1000) + " Thousand " + self.helper(num % 1000)
        elif num < 1000000000:
            result = self.helper(num / 1000000) + " Million " + self.helper(num % 1000000)
        else:
            result = self.helper(num / 1000000000) + " Billion " + self.helper(num % 1000000000)
        return result.strip()