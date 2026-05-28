class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []  # Initialize visited as a list
        while n != 1 and n not in visited:
            visited.append(n)  # Append n to the visited list
            n = self.getSumOfSquares(n)
        return n == 1

    def getSumOfSquares(self, n: int) -> int:
        sum_of_squares = 0
        while n > 0:
            digit = n % 10
            sum_of_squares += digit ** 2
            n //= 10
        return sum_of_squares