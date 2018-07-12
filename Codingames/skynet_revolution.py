# -*- coding: utf-8 -*-

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
Links = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    Links.append((n1, n2))
for i in range(e):
    ei = int(input())  # the index of a gateway node

# game loop
while Links:
    sorted(Links)
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if (ei, si) in Links:
        print(' '.join((ei, si)))
        Links.pop(Links.index((ei, si)))
    else:
        for s in range(n):
            if (ei, s) in Links:
                print(' '.join((ei,s)))
                Links.pop(Links.index((ei, s)))
            else:
                continue
