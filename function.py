## function => Block of statements that perform a specific task.
## redundant => always repeat
## arguments => means it supply the values.
## parameters => 
## Use of function because of => decrease of redundency( rcode bata edundency kam hoss bhanera)

## Print sum of two numbers.
# def cal_sum(a,b):
#     sum= a+b
#     print(sum)
#     return sum
# cal_sum(5,10)

# ## more code ....
# cal_sum(5,30)

# ## more code blablabla....
# cal_sum(51,12)

##................ same question of another style
##function defination 1st 2 line
# def cal_sum(a,b):    # a,b are parameter
#     return a+b

# sum = cal_sum(2,5)   # cal_sum is function call & 2,5 is a arguments
# print(sum)

## To print hello.
# def print_hello():     # na input leko xa , na parameter use gareko xa , na output value deko xa , na return value deko xa
#     print("hello")  
# output= print_hello()
# print(output)           # jun function le kunai function nai return gardaina bhani usko output ma automatically NONE value aauxa

## Calculate the average of 3 numbers.
# def avg_num(a,b,c):
#     sum = a+b+c
#     avg = sum / 3
#     print(avg)
#     return avg
# avg_num(2,3,4)

##================== TYPES OF FUNCTION ====================
##===>> built-in Function ( already python ma lekheko hunxa)
##eg: print(), len(), type(), range() so on..

# print("JIGYASA","KOIRALA")   # sep =" " maens=> separaters ma automatically space aauxa output ma
# print("JIGYASA")             # end = "\n"

## same line ma print garnu xa bhani, 
# print("JIGYASA","KOIRALA")  # sep = " " , afhai space aauxa   
# print("JIGYASA")  # end = "\n"      # aflai next line ma janxa

# duitai value eutai line ma dui otai value lyaunu xa bhani, next line ma print na hoss bhani
# print("JIGYASA","KOIRALA",end=" ")    # end=" " => esma "$", space nabhaera aarunai kai rakheko bhae tai print hunthyo space ko satta
# print("Jigyasa")       

##===>>> User defined Function <<============
## jun functions programmer le lekhxan teslai user defined function bhanxa

##=====>>>> Default Parameters <<<<=============
## Calculate multiplication of two numbers.
# def cal_prod(a,b):
#     print( a*b )
#     return a*b 
# cal_prod(5,2)

## esari pani milxa
# def cal_prod(a=2,b=5):
#     print( a*b )
#     return a*b 
# cal_prod()

### 1st ma non default argument aaunu parxa ani balla default
# def cal_prod(a,b=5):      #default value dinu xa bhani last bata dina parxa
#     print( a*b )
#     return a*b 
# cal_prod(1)

# def cal_prod(a=5,b):   # easri garna mildaina, a ko milxa tala value dina ,tara b lai value dinai parxa, a lai dekoo xa bhani
#     print( a*b )
#     return a*b 
# cal_prod(1)

### ================ LET'S PRACTICE =================

### Q.No.1.WAP to print the length of a list. (list is the parameter)
## Ans 1st=>>>
# fruits=["apple","mango","grape","banana","litchi"]
# movies=["PK","sitare jameen parr","Dabang","3 idiots"]
# def print_len(list):
#     print(len(list))

# print_len(fruits)
# print_len(movies)

## Ans 2nd.......................
# subjects=["math","social","GK","science","DSA"]

# def print_len(list):
#     print(len(subjects))

# print_len(subjects)

## Ans 3rd...................
# cities=["delhi","pune","mumbai","chennai"]
# def print_len(cities):
#     print(len(cities))
# print_len(cities)

### Q.No. 2. WAF to print the elements of a list in a single line. (list is the parameter)
## Ans =>>................................. 
# heroes=["salman","sarukh","ameer","ranvir","mahesh babu"]
# movies=["PK","sitare jameen parr","Dabang","3 idiots"]

# # print(heroes[0], end="\n")   # esari next line ma ans aauxa
# # print(heroes[0], end=" ")    # esari same line ma 
# # print(heroes[2], end=" ")

# def print_list(list):  # function define gareko ra (list) bhaneko argument pass gareko xa
#     for item in list:    # use for loop in list to iterate
#         print(item,end=" ")
# print_list(movies)

### Q.No.3. WAF to find the factorial of n. ( n is the parameter)
### try (for loop)
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *=i
# print(fact)    

## Ans =>>>
# def cal_fact(n):
#     fact=1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)       # output = 720

### Q.No.4. WAF to convert USD to INR. (American dollar to Indian rupees)
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, " USD =", inr_val, "INR")
# converter(1)

### Q.No.5. WAF to convert INR to NPR. (Indian rupees to Nepali rupees)
# def converter(inr_val):
#     npr_val = inr_val * 1.58
#     print(inr_val, "INR =", npr_val, "NPR")
# converter(8)  

### 2nd method............
# def converter(inr_val):
#     return inr_val * 1.58

# print("8 INR =", converter(8), "NPR")

### Q.N.6 WAF where number can be input in function and when odd gives "ODD" and when even ask give "EVEN" in a string.

# num=int(input("enter the number : "))

# def print_val(num):
#     if num %2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
# print(print_val(num))
