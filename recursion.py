###  When a function calls itself repeadly. 
### loop & recursion are similar
### simple code:
# def show(n):
#     if(n == 0):        # base case
#         return 
#     print(n)
#     show(n-1)
# show(5)    # Output:5,4,3,2,1 

### Factorial
# def fact(n):
#     if(n==1 or n ==0):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

####============== LET'S PRACTICE ================
### Write a recursive function to calculate the sum of first n natural numbers.

## 1st step: 1st we print normal value ,print the value 5 to 1.
# def calc_sum(n):
#     if(n==0):
#         return 
#     print(n)
#     calc_sum(n-1)
# print(calc_sum(5))

## 2nd step: Now we add +n in calc_sum(n-1) +n because question ask to sum of 1st natural number.
# def calc_sum(n):        ##### don't run this code . It may occur error
#     if(n==0):
#         return 
#     print(n)
#     calc_sum(n-1) + n
# print(calc_sum(5))

## 3rd step: 
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n    # final sum
# sum = calc_sum(5)
# print(sum)

#### Q.N.2. Write a recursive function to print all elements in a list. Hint: use list & index as parameter.
### practice 1:

# nums=[1,2,3,4,5]
# def cal_fun(nums, index):
#     if index == len(nums):   #base case
#         return 
#     print(nums[index])
#     cal_fun(nums,index + 1)    # recursive call
# print(cal_fun(nums, 0))

### practice 2:
# def print_list(list,idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["mango","litchi","apple","banana"]
# print_list(fruits)

