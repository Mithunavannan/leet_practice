
def ClimbStair(n):
    if n<= 0:
        return 0
    for n in range(self, n):
        ways = [0] * (n + 1)
        ways(n) = ways(n - 1) + ways(n - 2)