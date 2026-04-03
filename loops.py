##===================>>>>>>>> LOOPS <<<<<<<<<<<=================================
# count=1
# while count<=10:
#     print("yah it's me :) ")
#     count+=1

# i=1
# while i<= 10:
#     print("apna college",i)
#     i+=1

## ........print numbers 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1
# print("Loop ended")

## ........print numbers 5 to 1
# i=5
# while i>=1:
#     print(i)
#     i-=1
# print("Loop ended")

##.............PRACTICE............
## Q.N.1. Print numbers from 1 to 100.

# i=1
# while i<=100:
#     print(i)
#     i+=1
# print("Loop ended")

## Q.N.2. Print numbers from 100 to 1.

# i=100
# while i>=1:
#     print(i)
#     i-=1
# print("Loop ended")

## Q.N.3. Print the multiplication table of a number n.

# i=1
# while i<=10:
#     print(3*i)
#     i+=1

##....aba malai code batai jun man lagxa tai ko table herna man xa bhani yo lata ko code garne

# n= int(input("enter the number : "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

## Q.N.4 Print the elements of the following list using a loop:
##       [1,4,9,16,25,36,49,64,81,100]

# list=[1,4,9,16,25,36,49,64,81,100]
# print(list)                # yo normal print bhayoo haii hehehe:)

##.......traverse ( kunai list, tuples, dictionary...kunai ma travel gardai ek ek gari janu lai traverse bhaninxa)
# nums=[1,4,9,16,25,36,49,64,81,100]
# index=0                      # index always 0 hunxa
# while index < len(nums):
#     print(nums[index])
#     index += 1

##.........Yo tesai try garya hihihihihi :)
# series=["queen of tears","lovely runner","when i fly towards you","big mouth"]
# idx=0
# while idx < len(series):
#     print(series[idx])
#     idx += 1

## Q.N.4 Search for a number x in this tuple using loop:
##       nums=(1,4,9,16,25,36,49,64,81,100)   

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i< len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#     else:
#         print("Finding...")
#     i += 1

##========================>>>>> BREAK & CONTINUE <<<<<<===========================
## BREAK...............................
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i< len(nums):
#     if(nums[i] == x):
#         print("Found at idx", i)
#         break                    # break bhaneko jata answer bhaettio tai break hune roki ne, aagadi na badne
#     else:
#         print("Finding...")
#     i += 1

## CONTINUE.............................
# i=0
# while i <= 5:
#     if( i== 3):
#         i+= 1
#         continue
#     print(i)
#     i += 1

## esmai aba odd ra even number nikalnu xa bhani
## ......For odd number nikalna 
# i=0
# while i <= 10:
#     if( i%2==0):
#         i+= 1
#         continue  # skip
#     print(i)
#     i += 1

## ......For even number nikalna 
# i=0
# while i <= 10:
#     if( i % 2!= 0):
#         i+= 1
#         continue
#     print(i)
#     i += 1

##=============== LOOPS ==========================
##========== 1.>>>> for loop <<<<===================
# list = [1,2,3,4,5]
# for val in list:
#     print(val)

# veggies = ["potato","cauliflower","tomato","capsicum"]
# for val in veggies:
#     print(veggies)         # esari veggies lai print garda 4 ota chizz lai 4 4 choti nai print garxa 

# tup=(1,2,3,4,4,5,6,7,8)
# for value in tup:
#     print(value)            # esari value lai nai print garyo bhane tai tup ma bhako chiz sarrr print hunxa

## iterator ma kam garda (eg: variable ko value lai update, stoping condition garnu paryo bhane ==>>>>while loop )
## data type ma traverse garnu paryo bhani( eg: tuples, strings, ...) ===>>> for loop

# str= "apnacollege"
# for char in str:
#     print(char)

# str= "apnacollege"
# for char in str:
#     print(char)
# else:
#     print("End")

## aba mero tala ko code ma "o" khojnu xa hai
# str= "apnacollege"
# for char in str:
#     if(char =='o'):
#         print("o found")
#         break
#     print(char)
# else:
#     print("End")

##=========== LET'S PRACTICE ====================
## ========== using for loop ==========

## Q.N.1. Print the elements of the following list using a loop:
##        [1,4,9,16,25,36,49,64,81,100]
## linear search =>>> euta single line ma search garne, euta euta garera value chaeck garne, euta na bhae arko, nabhae aarko...thisprocess of searching is calld linear search.
## Ans =>
# num= [1,4,9,16,25,36,49,64,81,100]
# for list in num:
#     print(list)

## Q.N.2. Search for a number x in this tuple using loop:
#        (1,4,9,16,25,36,49,64,81,100,49)

# tup =(1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0 
# for el in tup:
#     if(el == x):
#         print("Number found at idx", idx)
#     idx += 1

##............ if ek choti nai number bhetio bhani quit garna ni sakxam "break" use garera     
# tup =(1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0 
# for el in tup:
#     if(el == x):
#         print("Number found at idx", idx)
#         break
#     idx += 1

##======================= range() =================================
## sequence of number return garxa
## Defination : Range functions returns a sequence of numvers, starting from 0 by default, and increments
#              by 1(by default), and stops before a specified number.

# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])

## aba mathi ko code ma loop chalaunu xa bhani 
# seq = range(5)
# for i in seq:
#     print(i)

# 2nd method ( esari lekhna ni milxa python ma )
# for i in range(5):         # range(stop)
#     print(i)

# for i in range(2,10):        # range(start,stop)
#     print(i)

# for i in range(2,10,2):      # range(start,stop,step)
#     print(i)

# 1 to 10 samma even number print garnu xa re..
# for i in range(2,100,2):
#     print(i)

# 1 to 10 samma odd number print garnu xa re bhani.
# for i in range(1,100,2):
#     print(i)


##==================== PRACTICE =================
##============ using for & range() ================
 
##Q.N.1. Print numbers from 1 to 100.

# for i in range(1,101):
#     print(i)

##Q.N.2. Print numbers from 100 to 1.

# for i in range(100,0,-1):
#     print(i)


##Q.N.3. Print the multiplication table of a number n.

# n = int(input("Enter number: "))
# for i in range(1,11):
#     print(n*i)

##=========================== pass Statement =============================
## Pass is a null statement that does nothing. It is used as a placeholder for future code.

# for i in range(5):
#     pass            # loop ko bhitra kai kam garnu xaina bhani pass use hunxa paxi future ma kai code rakhna/ add garna man lagyo bhani Pass use hunxa
# print("some useful work")

## pass if else ma ni use hunxa
# for i in range(5):
#     pass               # pass lai python ma exceptional bhitra , try catch ko bhitra use garxam
# if i > 5:
#     pass
# print("some useful work")        

##================ LET'S PRACTICE ==============================
### WAP to find the sum of first n natural numbers. (using while)
## Ans>>>
# n = 5
# sum = 0
# for i in range(1, n+1):    # for loop ma use garera esari aauxa
#     sum += i
# print("total sum=", sum)  

## while loop

# n = 5
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum=", sum)


### WAP to find the factorial of first n numbers. (using for)
## ANS =>> ( while loop)
# n = 7
# fact = 1        # factorial lai sadhai 1 sanga variable initialize garxam , 0 sanga garyo bhane sabai le "0" sanga multiply hunxa ra answer sadhai "0" nai aauxa fheri
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("factorial =", fact)

## ( for loop )
# n = 5
# fact =1
# for i in range(1, n+1):
#     fact *= i
# print("factorial =", fact)