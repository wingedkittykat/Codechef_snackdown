def findWeight(l):
    w = 0.2
    if l[0]=='d' or l[0]=='f':
        phand = 'l'
    elif l[0]=='j' or l[0]=='k':
        phand = 'r'
    else:
        exit()
    for i in range(1,len(l)):
        if l[i]=='d' or l[i]== 'f':
            if phand == 'l':
                w = w+0.4
            else:
                w = w+0.2
            phand = 'l'
        elif l[i]=='j' or l[i]=='k':
            if phand == 'l':
                w = w+0.2
            else:
                w = w+0.4
            phand = 'r'
        else:
            exit()
    return(w)

t = int(input())
if t<1 or t>100:
    exit()
for i in range(t):
    n = int(input())
    if n<1 or t>100:
        exit()
    word = []
    weight = 0
    for j in range (n):
        a = input()
        if len(a)>20:
            exit()
        let = list(a)
        #findWeight(let)
        #print(let)
        if a not in word:
            weight = weight + findWeight(let)
        else:
            weight = weight + ((findWeight(let))/2)
        word.append(a)
    weight = weight*10
    print(int(weight))
    