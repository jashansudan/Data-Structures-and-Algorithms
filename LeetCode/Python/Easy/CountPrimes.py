class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        is_prime = [True] * (n)
        is_prime[0], is_prime[1] = False, False
        for num in range(2, int(n ** 0.5) + 1):
            for multiple in range(num + num, n, num):
                is_prime[multiple] = False
        return sum(is_prime)
