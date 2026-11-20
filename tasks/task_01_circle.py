def solve():
    radius = 42
    pi = 3.1415926
    area = pi * (radius ** 2)
    print(round(area, 4))
    
    point_1 = (23, 34)
    dist_1 = (point_1[0]**2 + point_1[1]**2) ** 0.5
    print(dist_1 < radius)
    
    point_2 = (30, 30)
    dist_2 = (point_2[0]**2 + point_2[1]**2) ** 0.5
    print(dist_2 < radius)

if __name__ == "__main__":
    solve()