#!/usr/bin/python3
"""Prime Game in Python."""


def isWinner(x, nums):
    """Determine the winner of the game."""
    if not nums or x < 1:
        return None

    n = max(nums)

    primes = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, n + 1, i):
            primes[j] = False
    primes[0] = primes[1] = False
    y = 0
    for i in range(len(primes)):
        if primes[i]:
            y += 1
        primes[i] = y
    player1 = 0
    for x in nums:
        player1 += primes[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
