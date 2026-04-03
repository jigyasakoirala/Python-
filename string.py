
#....STRINGS......
#Key points:   \t  ... le ali kati gap dinxa sentence ma

# str1="Jig"
# str2="yasa"
# finalstr=str1+str2
# print(finalstr)     
# print(len(str1))    #=> Yo line ma length check gareko

#.........===>>>>INDEXING of STRING...............
# str= "apna_college"
# ch= str[5] 
# print(ch)
# #...OR
# str="apna_college"
# print(str[2])

#...........===>>>SLICING of STRING..............
# str="apna college"    
# print(str[0:4])  #....Ending index should not be included it's a rulee.....

# str="Jigyasa Koirala"
# print(str[1:6]) #output..>>>igyasa 
# print(str[3: ]) #Output..>>>yasa Koirala   # [3:len(str)]
# print(str[ :5]) #output...>>>Jigya

#.........>>>>negative slicing<<<<<.......
# str="apple"
# print(str[-3:-1])  #output= pl

#===========>>>>STRING FUNCTION<<<<===========
# str="jigyasakoirala is my name"
# print(str.endswith("is my name"))   # .endswith le last ko correct xa ki xaina check garxa...xa bhani True otherwise False

# str="my name is jigyasa koirala"
# print(str.endswith("ala"))  # str.endswith le last ko letter true xa ki xaina check garxa
# print(str.capitalize())  # str.capitalize le 1st ko letter capital banauxa
# print(str.replace("a","e"))  # str.replace le kunai alphabet kita word repalce garne kam garxa
# print(str.replace("name","neem"))  # output= my neem is jigyasa koirala
# print(str.find("a"))  # str.replace le khojne kam garxa, 1st time kun thauma tyo word or alphabet kata start bhayo ta check garera 
# ch ma output dinxa
# str="my name is jigyasa koirala. She is beautiful."
# print(str.count("a"))  # str.count le kati choti word, alphabet use bhako xa patta lagauxa

#================>>>>>Practice<<<<==========================
# Q.N.1. WAP to input user's first name & print it's length.
# name=input("enter your name: ")
# print(len(name))

#Q.N.2.  WAP to find the occurance of'$' in a string.
# str= "My name is $. And she earn $ dheraii :)"
# print(str.count("$"))

