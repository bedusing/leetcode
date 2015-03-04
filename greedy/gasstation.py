# coding:utf-8
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to\
its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
Note:
The solution is guaranteed to be unique.
"""


def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start_index = 0
    count = len(gas)
    sum_gas = 0
    index = 0
    while index < count:
        sum_gas += gas[index] - cost[index]
        index += 1
        if sum_gas < 0:
            sum_gas = 0
            start_index = index % count
    return start_index
