a = int(input())
if a % 4 == 0 or a % 400 == 0:
    print('год' , a,'високосный')
else:
    print('этот год не високосный')