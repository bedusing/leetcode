# coding:utf-8

"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(steps):
    ways = {}

    def _climb(steps):
        if steps in ways:
            return ways[steps]
        if steps in (1, 2):
            ways[steps] = steps
            return steps
        ways[steps] = _climb(steps - 1) + _climb(steps - 2)
        return ways[steps]
    _climb(steps)
    return ways[steps]

print climb_stairs(300)
 