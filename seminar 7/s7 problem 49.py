orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(lst):
    temp = [lst[0]]
    maxm = 0
    for x in lst:
        if x[0] != x[1]:
            if (x[0])*(x[1]) > maxm:
                maxm = (x[0])*(x[1])
                temp.pop()
                temp.append(x) 
                
    print((temp[0]))

print(find_farthest_orbit(orbits))
    