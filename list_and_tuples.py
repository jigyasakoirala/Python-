#==========>>>>LIST AND TUPLES<<<<==============
#............LIST..................(Mutable= value change hunxa), always used '[]' bracket
# marks=[10.3,70.5,55.6,78.0] # List 
# print(marks)
# print(type(marks))
# print(marks[0])  # Indicing
# print(marks[1])
# print(len(marks))

# student=["karan",10,59.0, "Kolkata"]
# print(student)
# print(len(student))
# print(type(student))
# print(student[0])
# student[0]="Ram"  #replace
# print(student)

# marks=[10,20,30,40,50]  
# print(marks[1:4])     # # Slicing => syntax= list_name[starting_idx:ending_idx]
# print(marks[-4:-2])     # Slicing

# list=[10,26,1,75,22,84,17,1,40,50]
# list.append(7)  # add one element at the end
# list.append(100)
# print(list)

# print(list.sort())  # sorts in ascending order.......................................
# print(list)
# print(list.sort(reverse=True))  # sorts in decending order
# print(list)

# list.insert(5,77)  # insert element at index, syntax =>> list.insert(idx,el) ...>>> idx means index & el means elements.
# print(list)

# list.remove(1)   # list.remove le euta bhako element or element 2 ota same xa bhani tya maddhe kun 1st ma aako tes laii remove garxa 
# print(list)              # OR, remove 1st occurence of element

# list.pop(3)   # pop le kun (removes elements at idx)
# print(list)


#...............TUPLES...................(Immutable = ek chotii value tuple bhaisakyo bhani change hudaina, na add milxa , nata delete hunxa)
# tup=(1,3,6,4,3,8,5)       # Tuples lai sahai small bracket ma use hunxa'()'
# print(type(tup))
# print(tup)

# tup=(1)    # TUPLES ma sadhai single element lekhda (... ,) dinxa , =>>> comma is compulsory 
# print(tup)

##tup=(1)  => yo matrai lekhem bhani computer le integer bujhxa
##tup=(1,) =>  yo (1,) garem bhani tuple ho bujhxa

# tup=(1,3,6,4,3,8,5)  # SLICING
# print(tup[2:5])

#......METHOD........
# tup=(9,4,7,2,6)
# print(tup[0])
# print(tup[3])
# # tup[3]=55   # tuples ma replace garna mildaina , it is immutable

# tup=()  # empty tuple
# print(tup)
# print(type(tup))

# tup1=(5)  # python le normal integer sochxa so hamile, tup=(1,) lekhnu parxa
# tup2=(5,6,7,8,)
# # print(type(tup1))  # yo integer bujhxa python le
# print(type(tup2))  # yo tuple
# print(tup2[1:3])    # esma no. count gareko 
# print(type(tup1))

# tup=(2,5,3,4,5,6,3,7,1)
# print(tup.index(3))   # esma 1st ma 3 no. kun thauma pugda aayo check garxa

# tup=(1,3,4,2,6,4,8,9,5,3,2,3,51,41,1,2,3)
# print(tup.count(2))   # kati choti tyo num. aayo count garxa

# #.........PRACTICE...........
# Q.No.1.  WAP to ask the user to enter the name of their 3 favourite movies & store them in a list.
# movie = []   # 1 method
# movie1= input("enter favourite movie:")
# movie2= input("enter favourite movie:")
# movie3= input("enter favourite movie:")

# movie.append(movie1)
# movie.append(movie2)
# movie.append(movie3)
# print(movie)   

#...OR 2nd method
# movie=[]
# movie.append(input("enter 1st favourite movie:"))
# movie.append(input("enetr 2nd favourite movie:"))
# movie.append(input("enter 3rd favourite movie:"))
# print(movie)

# Q.No.2.  WAP to check if a list contains a palindrome of elements.(Hint: Use copy method)
# num=["e,y,e"]   # palindrome list ( agadi paxadi bata same padna milni)

# copy_list=num.copy()    #copy of list 
# copy_list.reverse()     #reverse the copy

# if num==copy_list:
#     print("The list is palindrome")
# else:
#     print("The list is not pallindrome")

# # Q.No.3.  WAP to count the number of students with the "A" grade in the following tuple.  ["C","D","A","A","B","B","A"]
# tup=["C","D","A","A","B","B","A"]
# print(tup.count("A"))

# # Q.No.4.  Store the above(q.no.3) values in a list & sort them from "A" to "D".
# list=["C","D","A","A","B","B","A"]
# (list.sort())
# print(list)   # This is in ascending order

# lst = ["C", "D", "A", "A", "B", "B", "A"]
# lst.sort(reverse=True)
# print(lst)     # This is in decending order
