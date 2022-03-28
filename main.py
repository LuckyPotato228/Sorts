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


def bubble_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(*arr,'|')
    print("------------")
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


def show(lst, l, r, cur):
    for j in range(len(lst)):
        print(f'{"| " if j == l else ""}{"<" if j == cur else ""}{lst[j]}{">" if j == cur else ""}{" |" if j == r else ""}', end = ' ')
    print("")


def shaker_sort():
    n = int(input())
    arr = [int(i) for i in input().split()]





def merge_sort():
    pass
    """
    n = int(input())
    arr_1 = [int(i) for i in input().split()]
    k = int(input())
    arr_2 = [int(i) for i in input().split()]
    result = []
    for i in range(n+k):
        target_num_1 = str(arr_1[i])
        target_num_1 = ("<" + target_num_1 + ">")
        target_num_2 = str(arr_2[i])
        target_num_2 = ("<" + target_num_2 + ">")
        print(arr_1[:i],target_num_1,*arr_1[i+1:])
        print(arr_2[:i],target_num_2, *arr_2[i + 1:])
    """



