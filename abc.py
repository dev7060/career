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

############################################

num = int(input())
i=2
while(i<=num):
    temp = i
    j = 2
    flag = 1
    while(j<=(temp//2)):
        if(temp%j == 0):
            flag=0
            break
        j = j+1
    if(flag==1):
        print(temp, end=" ")
    i = i+1
    
 ############################################
