if __name__ == '__main__':
    student_score={}
    names=''
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score[name]=score
    sorted_value=sorted(list(student_score.values()))
    min_=min(sorted_value)
    for i in sorted_value:
        if i>min_:
            min_=i
            break
    for key,value in student_score.items():
        if value==min_:
            names+=key+" "
    alphabetic_name=sorted(names.split(" "))[1:]
    print('\n'.join(alphabetic_name))
