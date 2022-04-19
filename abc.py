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

num = int(input())
def fun(num):
    if(num<=3):
        return
    first = 1
    second = 1
    i=1
    while(i<=num):
        third = first + second
        k=2
        flag = 1
        while(k<=(third//2)):
            if(third%k==0):
                flag = 0
                break
            k = k+1
        if(flag == 1):    
            print(third, end=" ")
        first = second
        second = third
        i = i+1
fun(num)

##############################################

num = int(input())
temp = num
rev = 0
while (temp>0):
    digit = temp%10
    rev = digit + rev*10
    temp = temp // 10
a=0 
b=0 
if num == rev:
    pass
elif num > rev:
    a = rev
    b = num
else:
    a = num
    b = rev
while (a<b+1):
    print(a, end=" ")
    a = a+1
    
    
########################################################

