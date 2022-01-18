def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        new_str=''
        for s in string[i:i+k]:
            if s not in new_str:
                new_str+=s
        print(new_str)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
