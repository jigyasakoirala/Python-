#=============>>>>CONDITIONAL STATEMENTS<<<<<==============
#......if else statements.........
# light="yellow"
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# elif(light=="green"):
#     print("go")
# print("code is completed")

#in (if statement)==>> if matrai garda sabai if if lekheko thau print hudai janxa ra,,,
#in (if else statements)==>>esma if check garxa, tya if ma result correct bhayo bhani else ma jadaina ra,,
#                          jata gaera bhetio tai pugera stop hunxa sabai bhae bhar ko code print hudaina 
# in (else statement)==>>esma sabai if, elif sabai check garda ni true condition bhaetiena bhani last ma else ma puera output dinxa

# num=10

# if(num>=8):
#     print("greater than 8")
# elif(num>=2):
#     print("greater than 3")


# light="blue"
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# elif(light=="green"):
#     print("go")
# else:
#     print("The light might be broken")

# print("code is completed")


#......if & else....
# traffic_light="green"
# if(traffic_light=="blue"):
#     print("Color")
# else:
#     print("Blue is not a traffic_light")


# age=17

# if(age>=18):
#     print("you can vote")  ## yo enter garda print samma aali kati gap aauxa ni teslai indentation bhaninxa (proper spacing)
# elif(age<=10):
#     print("you cannot eligible for vote")
# else:
#     print("Vote is only eligible for greater than 18 year old person.")


# marks= int(input('enter the student marks: '))

# if(marks >=90):
#     grade='A'
# elif(marks >=80 and marks<90):  # logical operator is used "AND"
#     grade='B'
# elif(marks >=70 and marks<80):
#     grade='C'
# else:
#     grade='D'

# print("grade of the student ->",grade)

#===============>>>>NESTING<<<<====================euta statement ko bhitra aarko statement lehni lai nesting bhaninxa
# age = 91

# # Nesting
# if(age>=18):
#     if(age<=80):
#         print("Can drive")
#     else:
#         print("Cannot drive")
# else:
#     print("Not eligible for drive")


# if(age>=18):
#     if(age<=80):


#===============PRACTICE======================
#1. WAP to check if a number entered by the user is odd or even.
# num=int(input("enter the number: "))

# if(num % 2==0 ):
#     print("It is even")
# else:
#     print("It is odd")

# 2.WAP to find the greatest of 3 numbers entered by the user.
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))

# if(a>=b and b>=c):
#     print("First number is largest",a)
# elif(a>=c and c>=b):
#     print("Second number is largest",b)
# else:
#     print("Third number is largest",c)    

#........for 4 number........

# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))
# d=int(input("enter forth number"))

# if(a>=b and b>=c):
#     print("The first number is largest",a)
# elif(a>=c and c>=d):
#     print("The second number is largest",b)
# elif(a>=b and b>=a):
#     print("The third number is largest",c)
# else:
#     print("The forth number is largest",d)

# 3. WAP to check if a number is a multiple of 7 or not.
# num=int(input("enter the number: "))

# if(num % 7 == 0 ):
#     print("Yes.It is multiple.")
# else:
#     print("No.It is not multiple")