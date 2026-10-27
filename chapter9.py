a = 1
while a != 20:
    print(a)
    a = a + 1

#Question1

a = int(input("please tell you number :-"))

while a > 0:
    print(a%10)
    a = a //10

#Question2

a = int(input("please tell you number :-"))

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(rev) 


#Question3

a = int(input("please tell you number :-"))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10 

if rev == copy:
    print("palindorome")
else:
    print("not a palindrome")    
    



