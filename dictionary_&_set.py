#...............>>>>DICTIONARY & SET<<<<<................................
# ===============>>>>>DICTIONARY<<<<===============================#
#  dictionary add,remove ,change garna ni milxa paxi. It is mutable.
#Tuple is not change ,so we can also make tuple in float.

# dic={                           # dictionary bhaneko data store garne ra kam lagda use garne.......
#     "name":"jigyasa",
#     "class": 7,
#     "subjects": ("math", "java" , "python"),    # this is tuple ()
#     "marks":[92.3,55.7,60],                     #this is string but it is in list form []
#     "topics":("list","dictionary","tuples"),
#     "student": "Just wow",
#     12.99: 56.8                                 # this is float 
# }
# print(dic)
# print(type("topics"))
# print(type( 12.99))
# dic["name"]="Pragya"              # assign gareko, name ko thauma aarunai name replace gareko 
# dic["surname"]="koirala"          # new name ni add bhayo , dictionary ma pani kai kura haru add garna milxa
# print(dic)

#..................................NULL dictonary.......................................
# null_dic={}                         # null dictionary ni garna sakxam
# null_dic["age"]=45                  # ra null dictionary ma paxi data enter gardai jana ni sakxam
# print(null_dic)

#..................................NESTED DICTIONARY........................................
#dictionary bhitra ni dictionary add garna milxa bhane tyo nested dictionary ho..for eg:

# student={
#     "name":"Rahul Kumar",      # name, class & subjects are "Keys" in dictionary
#     "class": 7,
#     "subjects":{
#         "phy": 57,
#         "chem":97,
#         "DSA":99
#     }
# }
# Nested Dictionary (dictionary ko bhitra aarko dictionary add garxam bhani nested)

# print(student)              
# print(student["subjects"])
# print(student["subjects"]["DSA"])

#....................>>>>>>>>>>>>> Dictionary methods<<<<<<<<.........................
# 1.> Method====>>>>>     myDict.keys()  # return all keys

# print(student.keys())            # nested bala chai aaudaina matrai outer bala chai print hunxa
# print(list(student.keys()))      # list ma nikaleko
#print(tuple(student.keys()))      # tuple ma
# print(len(list(student.keys())))  # OR ..............

# print(len(student))               # yo ni mathiko jastai same ho tara xitta xutai garya xa esma 

# 2.=> Method ======>>>>   myDict.values()   # return all values

# print(student.values())     # OR.....
# print(list(student.values()))                # esma list add gareko 

# 3.=> Method =========>>>>  myDict.items()    # returns all(keys,val) pairs as tuples

# print(student.items())
# print(list(student.items()))

# 4. => Method =========>>>> myDict.get("key")   # returns the key according to value

# print(student["class"])
# print(list(student.get("name")))
# print((student.get("name")))

#But.........
# print((student["name2"]))    # error return garxa
# print(student.get("name2"))   # no error, but gives the output => NONE
# print(list(student.get("name")))

# 5. => Method ==========>>>>>> myDict.update(newDict)
# new_dic={"city":"nepal","gender":"female"}
# student.update(new_dic)
# print(student)

#.....................................................Sets In Python...................................
# Set accepts => boolean,int,float,string,tuple but,,,,,,,
# set donot accepts => list,dictionary 

# collection={1,3,4,5,6,4,7,5,8,9,0}     # set ma ek choti matrai show garxa
# print(collection)
# print(type(collection))
# print(len(collection))

# collection={}  # this the sntax of dictionary
# collection=set()   # empty set

#=============>>>> Methods OF Sets <<<<<<<<=============================

# collection=set()
# collection.add(7)
# collection.add(25)
# collection.add('apnacollege')
# collection.add((1,2,3,3,4,5))        # 1=>  set.add(el) = (all of the above sets are added)............
# collection.clear()                   # 2=>  set.clear() method......................
# print(collection)
# print(len(collection))           #length of collection
#.......................................................
# collection.remove("apnacollege")      # 3 => set.remove(el)...........................
# print(collection)

#.......................>>>> 4 => POP Method <<<<.....................................

# collection={"hello","jigyasa","java","python"}
# print(collection.pop())        # random choose garera output dinxa
# print(collection.pop())         #random values pop bhaera aauxa

#.......................>>>>> 5 => set.union(set2) Method <<<<<......................
#.......................>>>>> 6 => set.intersection(set2) Method <<<<<...............
# set1={1,2,3,4,5}
# set2={3,4,5,6,7}
# print(set1.union(set2))   # Output => 1,2,3,4,5,6,7   
# print(set1.intersection(set2))   # Output => 3,4,5

#=========================== PRACTICE =============================================
# Q.N.1. Store following word meanings in a python dictionary.
#        table : "a piece of furniture","list of facts & figures"
#        cat : "a small animal"
# ....Ans =>>>
# dictionary={
#     "cat" : "a small animal",
#     "table":{
#         "dic1":"a piece of furniture",
#         "dic2":"list of facts & figures"
#     }
# }
# print(dictionary["cat"])
# print(dictionary["table"])
# print(dictionary["table"]["dic1"])
# print(dictionary["table"]["dic2"])

# Q.N.2. You are given a list of subjects for students. 
# Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
#   "python","java","C++","python","javascript","java","python","java","C++","C"

#....Ans =>>> 
# subjects={ "python","java","C++","python","javascript","java","python","java","C++","C"}
# print(subjects)
# print(len(subjects))

# Q.N.3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

#...Mine .Ans =>>> But this is wrong hehehehehehe :)))) 
# marks={}
# subjects={
#     "key": 'values',
#     "physics": 78,
#     "chemistry": 96,
#     "DSA": 99
# }
# print(subjects)
# print(len(subjects))


#....videos answer......>>>>
# marks={}
# x=int(input("enter phy : "))
# marks.update({"phy" :x})

# x=int(input("enter chem : "))
# marks.update({"chem" :x})

# x=int(input("enter math : "))
# marks.update({"math" :x})
# print(marks)

 # Q.N.4. Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built in data types)
# Ans =>>>
# values={9, 9.0}
# print(values)   # output= python ma 9, 9.0 lai 9 nai bujhxa

# values={9, "9.0"}
# print(values)    # output= aba chai {9,"9.0"} aauxa

# values={9, 8.7, 4.7}
# print(values)      # output= esma ({8.7, 9, 4.7}) auxa 

#.......2nd method......
# values={
#     ("float",9.0),
#     ("int",9)
# }
# print(values)