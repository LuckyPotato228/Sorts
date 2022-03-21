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
    b = arr[::1]
    for i in range(n + 1):
        b = list(map(str,arr))
        index = arr.index(min(arr))
        num = str(arr[index])
        b[index] = str('<' + num + '>')
        b.insert(i,'|')
        print(b)



insertion_sort()
