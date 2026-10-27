#ranges
# 10 - 100
# 23 - 56
# 0 - 45

range(10,101,1)
range(23,57,1)
range(46)

for i in range(10,101,10):
    print(i)

n = int(input("please tell your number :-"))

for i in range(n,(n*10)+1,n):
    print(i)

a = "Students"

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

for i in range(len(a)):
    print(f"{i} : {a[i]}")

for i in range(1,11):
    if i ==4:
        break
    print(i)

for i in range(1,11):
    if i ==4 or i==5 or i ==6:
        continue
    print(i)

for i in range(1,11):
    if i ==5:
        break
    print(i)
else:
    print("no break was encountered")

#Question1

n = int (input("tell your number :-"))

for i in range(n):
    print("hello world")

#Question2

n = int (input("tell your number :-"))

for i in range(1,n+1):
    print(i)
#Question3

n = int (input("tell your number :-"))

for i in range(n,0,-1):
    print(i)

#Question4

n = int (input("which table you want :-"))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#Question5

s = 0
n = int (input("till where you want you sum :-"))
for i in range(1,n+1):
    s = s + i

    print(s)

#Question6 

n = int(input("tell your number :-"))

f = 1

for i in range(1,n+1):
    f = f*i
     
print(f) 

#Question7

n = int(input("please tell your number:"))

oddsum = 0
evensum = 0

for i in range(1,n+1):
    if i %2 ==0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i
print(f"your even sum is {evensum} and odd sum is{oddsum}")

#Question8

n = int(input("tell your number :-"))

for i in range(1,n+1):
    if n % i ==0:
        print(i)

#Question9

n = int(input("tell your number :-"))

s = 0

for i in range(1,n+1):
    if n%i ==0:
        s == s + i

if s == n:
    print("prerfect number")
else:
    print("not a prefect number")   

#Question10

n = int(input("please tell your number :-"))
count = 0

for i in range(1,n+1):
    if n % i ==0:
        count = count + 1

if count == 2:
    print("prime number")
else:
    print("composite number")    

#Question11

a = "python"

print(a[::-1])

a = "python"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

print(rev)    

#Question12

a = input("tell your string")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

if rev ==a:
    print("yes palindrome")
else:
    print("no not a palindrome")    

#Question13

a = "P@#yn26at^&i5ve"

char = 0
spchar = 0
digits = 0

for i in a :
    if (ord(i) >= 65 and ord(i) <= 90) or (ord (i)>=97 and ord (i) <= 122):
        char +=1
    elif ord(i) >= 48 and ord(i) <= 90:
        digits += 1
    else:
        spchar = spchar + 1

print(f"characters {char}, special characters - {spchar}, digits - {digits}")
 
# print(ord("Z"))

