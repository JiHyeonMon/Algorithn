#2439
#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제(오른쪽 기준)

num = int(input())

for i in range(1,num+1):
    print("{}{}".format(" "*(num-i), "*"*i))

