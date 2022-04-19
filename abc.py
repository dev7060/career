num = int(input())
i = 1
counter = 0
while(i<=num):
    temp = i
    while(temp>0):
        digit = temp%10
        if digit == 0:
            counter = counter + 1
        temp = int(temp / 10)
    i = i+1
print(counter)
