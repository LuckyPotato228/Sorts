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
    n = 11#int(input())
    arr = [int(i) for i in "1 10 2 9 3 8 4 7 5 6 7".split()]
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
                    print(*b, "|" ,*arr[i+1:])
        print(*b[:i - count], target_num, *b[i - count + 1:], "|", *arr[i + 1:])
        count = 0
        print()


def merge_sort():
    pass



insertion_sort()