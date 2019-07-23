def find_circle_num(M):
    friend_zone = set([])
    circles = 0
    for i in range(len(M)):
        if i not in friend_zone:
            stack = [i]
            print(stack)
            while stack:
                cur = stack.pop()
                if cur not in friend_zone:
                    friend_zone.add(cur)
                    stack.extend([j for j,v in enumerate(M[cur]) if v and j not in friend_zone])
            circles += 1
    return circles


print(find_circle_num([[1,1,0],[1,1,0],[0,0,1]]))