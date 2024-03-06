if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    legth =len(student_marks[query_name])
    
    summ=float(0)
    
    for i in range (0,legth):
        summ+=student_marks[query_name][i]
        
    avg=float(summ/legth)
    k=f"{avg:.2f}"
    print(k)
        
