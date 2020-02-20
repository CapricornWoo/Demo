# jump int with 7 between 1 and 100
__author__ = 'vic'

for i in range(1,101):
    if i%7 == 0:
        continue
    elif i//10 ==7:
        continue
    elif i%10 == 7:
        continue
    else:
        print(i)
