def select_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    b = arr[::1]
    for i in range(n+1):
        try:
            arr.insert(i,'|')
            print(*arr)
            arr.pop(i)
            if i > 0:
                b.pop(0)
            index = b.index(min(b))
            b[0],b[index] = b[index],b[0]
            arr[i:] = b
        except ValueError:
            break


def insertion_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    b = []
    count = 0
    for i in range(len(arr)):
        b += [arr[i]]
        b[i] =
        print(b + arr[i+1:])
        if i>0:
            while b[i-count] < b[i-count-1]:
                if b[i-count-1] > b[i-count]:
                    b[i-count-1],b[i-count] = b[i-count],b[i-count-1]
                    count+=1
                    print(b + arr[i+1:])

        count = 0
        print()






insertion_sort()