def select_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    b = []
    for i in range(n+1):
        b = arr
        b.insert(i, "|")
        print(b)
        b.pop(i)
        for i in range(len(arr)):
            pass
select_sort()