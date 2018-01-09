class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1], is_prime[2] = False, False, False
        for num in range(2, n + 1):
            for multiple in range(num + num, n + 1):
                is_prime[multiple] = False
        return sum(is_prime)
