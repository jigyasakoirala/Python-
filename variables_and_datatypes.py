#.........................CHAPTER ONE.................
## ================== >> VARIABLES & DATA TYPES <<<< ============================
#a=2
#b=5
#sum= a+b
#print(sum)

#...........Type conversion........

# a=2
# b=4.5
# sum=a+b
# print(sum)

# a="2"          #//.......esma hami le kunai variable ko ya input gareko chizz ko kun type ho patta lagaune kam garxa "type" le
# b=4.5
# print(type(a))  # esma a ko type patta lageko xa =>"string"

#.........Type caste conversion........

# a=int("2")
# b=4.5
# print(type(a))
# print(a+b)

# a=3.14
# a=str(a)
# print(type(a))

#....................................................................
# ....TOPICS......input in Python......
# intput()......esle string dinxa always
# int(intput())........integer dinxa
# float(input()).........float dinxa 

#....EXAMPLES...
# name=input("enter my name:")
# print("you entered is", name)

# val=(input("enter some value: "))
# print(type(val),val)

#......in intteger...
# int("5")
# val=int(input("enter the value: "))
# print(type(val),val)

#......in float...
# val=float(input("enter the value: "))
# print(type(val),val)


#.....EXAMPLE INPUT (NAME,AGE, MARKS)
# name=input("my name is: ")
# age=int(input("my age is: "))
# marks=float(input("my marks is: "))
#.....//sabai ko type thapaunu xa bhani type ....down steps
# print(type(name),name)
# print(type(age),age)
# print(type(marks),marks)
#.......//type tha napani sidai input nikalnu xa bhani....down steps
# print("name=",name)
# print("age=",age)
# print("marks=",marks)

#......PRACTICE.....
#Q.No.1...WAP to input two number and print their sum.
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# sum=num1 + num2
# print("The sum of two number is: ",sum)

#Q.No.2...WAP to input side of square & print it's area.
# length=int(input("enter the side of square: "))
# area=length * length
# print("The area of square is: ",area)

#Q.No.3....WAP to input 2 floating point numbers & print their average.
# num1=float(input("enter first number"))
# num2=float(input("enter second number"))
# average= (num1+num2)/2
# print("the sum of two floating point number: ",average)

#Q.No.4....WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b.If not print False.
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# print(a>=b)

