if __name__ == '__main__':
    record=[]
    n_And_record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        n_And_record.append([name,score])
        record.append(score)
        
    record.sort()
    second=record[1]
    names=[]
    for name,score in n_And_record:
        if (score==second):
            names.append(name)
    
    names.sort()
    for i in range (len(names)):
        print(names[i])
