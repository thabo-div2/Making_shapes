# Making shapes
def hollow_triangle(n):
    for i in range(1, n+1):
        for j in range(1, 2*n):
            if i == n or i+j == n+1 or j-i == n-1:
                print("*", end="")
            else:
                print(end=" ")
        print()

hollow_triangle(8)