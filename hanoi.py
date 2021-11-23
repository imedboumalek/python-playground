# a function that solves the hanoi problem
def hanoi(n, start, end, helper):
    if n == 1:
        print("Move disk 1 from source", start, "to destination", end)
        return
    hanoi(n-1, start, helper, end)
    print("Move disk", n, "from source", start, "to destination")
    hanoi(n-1, helper, end, start)


hanoi(5, "A", "C", "B")
