if __name__ == '__main__':
    N = int(input())
    lst=[]
    for _ in range(N):
        enter=input().split()
        cmd=enter[0]
        if cmd=='insert':
            lst.insert(int(enter[1]),int(enter[2]))
        if cmd=='append':
            lst.append(int(enter[1]))
        if cmd=='remove':
            lst.remove(int(enter[1]))
        if cmd=='sort':
            lst.sort()
        if cmd=='pop':
            lst.pop()
        if cmd=='reverse':
            lst.reverse()        
        if cmd=='print':
            print(lst)
