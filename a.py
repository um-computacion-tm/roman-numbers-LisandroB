def staircase(n):
    for i in range(n+1):
        print(("#" * i).rjust(n))


staircase(5)