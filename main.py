def Select_sort():
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


def Insertion_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    b = []
    count = 0
    for i in range(len(arr)):
        b += [arr[i]]
        target_num = str(arr[i])
        target_num = ("<" +target_num+">")
        if i > 0:
            print(*b[:i],"|", target_num, *arr[i + 1:])
        else:
            print("|",target_num, *arr[i+1:])
        if i>0:
            while b[i-count] < b[i-count-1]:
                if b[i-count-1] > b[i-count]:
                    b[i-count-1],b[i-count] = b[i-count],b[i-count-1]
                    count+=1
                    print(*b[:i-count],b[i+1-count],*b[i+1-count:], "|" ,*arr[i+1:])
                    if count == i:
                        break

        print(*b[:i - count], target_num, *b[i - count + 1:], "|", *arr[i + 1:])
        count = 0
        print()
    print(*b)


def Bubble_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(*arr,'|')
    print("------------")
    count = int(1)
    for i in range(n-1):
        for j, val in enumerate(arr):
            target_num = str(arr[j])
            target_num = ("<" +target_num+">")
            print(*arr[:j], target_num, *arr[j + 1:n-i], '|',*arr[n-i:])
            if j == n-i-1:
                break
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("------------")
    print(*arr)


def Shaker_sort():
    pass

def Merge_Sort():
    pass

