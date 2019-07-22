import collections

"""
Eulerian traversal using Hierholzer’s Algorithm for directed graph
"""


def findItinerary(tickets):
    tickets.sort()
    targets = collections.defaultdict(list)
    # create dict of start: [loc1, loc2] where [] is reverse alphabetical
    for a, b in tickets[::-1]:
        targets[a] += (b,)
    route, stack = [], ["JFK"]
    while stack:
        while targets[stack[-1]]:
            # take last from destinations from location
            stack.append(targets[stack[-1]].pop())
        # add as next in route
        route.append(stack.pop())
    return route[::-1]


print(
    findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
)
