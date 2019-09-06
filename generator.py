#by function
def tri(r):
    p = [1]
    while True:
        print(p)
        p = [1] + [p[i]+p[i+1] for i in range(len(p)-1)] +[1] 
        if len(p)-1 == r:
            break

#call fuction
tri(5)



#by generator
def trig(r):
    p = [1]
    while True:
        yield p
        p = [1] + [p[i]+p[i+1] for i in range(len(p)-1)] +[1]
        if len(p)-1 == r:
            break

#call generator
for n in trig(4):
    print(n)
