if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_set=sorted(list(set(arr)))
    print(sorted_set[-2])
