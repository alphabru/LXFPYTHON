#https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128

#杨辉三角
#https://blog.csdn.net/qq_37701443/article/details/82707526

'''
重点是这句：
 p = [1] + [p[i]+p[i+1] for i in range(len(p)-1)] +[1]

每一个新的list中间的部分，都等于上一行list的：第0个元素+第1个元素，第1个元素+第2个元素，第2个元素+第3个元素,.......
'''


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
