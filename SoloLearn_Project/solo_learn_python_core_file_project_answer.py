file = open("/usercode/files/books.txt", "r")
try:
    each_lines=file.readlines()
    for each_line in each_lines:
        first_letter=each_line[0]
        length=len(each_line)
        if each_lines.index(each_line)!=len(each_lines)-1:
            length=len(each_line)-1
        print(first_letter+str(length))
except:
    print("Error Occured")
file.close()
