#https://www.liaoxuefeng.com/wiki/1016959663602400/1017268131039072

#递归实现汉诺塔
#https://baijiahao.baidu.com/s?id=1630034809552470725&wfr=spider&for=pc

'''
A,B,C三个柱子, A柱上n个盘子

	1. A柱上前n-1个盘子从A移动到B
	2. 第n个盘子从A移动到C
	3. B柱上的n-1个盘子从B移动到C
'''


#fuction
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
#call fuction
move(8,a,b,c)
