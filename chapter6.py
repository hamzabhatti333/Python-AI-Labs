if True :
    print("Hello how are you")

if False :
    print("Hello how are you")    

if 12==12 :
    print("hello how are you")

if 23!=23 :
    print("Hello are you")

if print(not (5==5 and 3!=4) or (10>20)) :
    print("Hello how are")   

#you have to take input of age and te;; the
#  preson can vote or not

age = int(input("please tell your age :-"))

if age >= 18:
    print("hello brother you can vote")
else :
     print("hello you can not vote sorry")


rupees = int(input("give money -"))

if rupees  == 10:
    print("I will have a chocobar")

elif rupees == 50:
    print("I will have manchurian")
elif rupees ==100:
    print("mcd")
elif rupees == 500:
    print("5 star dhaba")    

else:  
    print("bhuka rahu ga mai ")    

#question 1
num1 =int(input("please give me first number :-"))
num2 =int(input("please give me first number :-"))


if num1 > num2:
    print(f"{num1} is greater than {num2}")
    
elif num2 > num1:
        print(f"{num1} is greater than {num2}")
else:
    print("both the numbers are equal")
# Questiom 2
# example question 2
print("hello">"HEllo")

print(ord("e"))
print(ord("E"))

gen = input("please tell your gender in (M or F):-")

if gen == "M"or gen =="m":
   print("hello sir")
elif gen == "F" or gen =="f":
    print("hello mam")
else:
    print("others")

# Question 3

a = int(input("please tell your number :-")) 

if a %2 ==0:
    print("even number")
else:
    print("the number is odd")

# Question 4

name = input("please tell your name :-")
age = int(input("please tell your age"))

if age >= 18:
    print(f"hello{name}you are a vaild voter")
else:
    print(f"hello {name}you can vote after {18-age}year")    

# Question 5 

year = int(input("please tell your year"))

if year%100 ==0 and year %400 ==0:
    print("leap year")
elif year%100 !=0 and year %4 ==0:
    print("leap year")
else:
    print("not a leap year")

# Question6

temperature = int(input("please tell the temperature"))

if temperature>=-5 and temperature<=5:
    print("The Wether is very cold")
elif temperature>=6 and temperature<=18:
    print("The Wether is Clod")
elif temperature>=19 and temperature<=30:
    print("The Wether is hot")
else:
    print("The Wether Ver hot")






