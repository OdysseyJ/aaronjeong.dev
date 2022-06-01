def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    return v[0] * u[1] - v[1] * u[0]

def convex_hull(positions):
    convex = list()
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            print(p1, p2, p3, ccw(p1, p2, p3) > 0)
            if ccw(p1, p2, p3) > 0:
                break
            convex.pop()
        convex.append(p3)
    return len(convex)

n, answer = int(input()), -2
positions = list()
for i in range(n):
    positions.append(list(map(int, input().split())))

positions = sorted(positions, key=lambda pos:(pos[1], pos[0]))
answer += convex_hull(positions)

positions.reverse()
answer += convex_hull(positions)
print(answer)
