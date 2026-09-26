####=================>>>>> FILE I/0 IN PYTHON <<<<===================
### Python can be used to perform operations on a file. (read & write data)
### Types of all files:
###       1. Text Files: .txt, .docx, .log etc. ( character ko form ma store gareko hunxa ) 
###       2. Binary Files: .mp4, .mov, .png, .jpeg etc.

###====== OPEN, READ & CLOSE FILE =====
#### syntax =>>> f = open("file_name")

# f= open("demo.txt","r")
# data= f.read()
# print(data)
# print(type(data))
# f.close()


### data = f.read()       # reads entire file
###  data = f.readline()  # reads one line at a time

# f= open("demo.txt","r")
# line1= f.read()         # reads one line at a time
# print(line1)

# line2= f.read()         # reads one line at a time
# print(line2)
# f.close()
##......................................

# f= open("demo.txt","r")
# data = f.read()
# print(data)              # esari surumai data print garda,suru mai read gari sakeko hunxa ra,ani line1,line2 print garda tyo thauma khali thau/ blank print gardinxa
                              
# line1= f.read()         
# print(line1)

# line2= f.read()         
# print(line2)
# f.close()

##====================== Writing to a file =======================
## syntax =>> f = open("demo.text","w")
##            f.write("this is a new line")     # overwrites the entire files

##            f= open("demo.txt,"a")          # a means append mode, write at the end
##            f.write("thos is a new line")      # adds to the file

# f= open("demo.txt","w")
# f.write("Hi.. My name is Jigyasa Koirala.")
# f.close()
  
# f= open("demo.txt","a")     # append => add new line at the end
# f.write(" I want to learn Python tomorrow.")
# f.close()
    
# f= open("demo.txt","a")     # append => add new line at the end
# f.write(" \nThen I'll move to ReactJS.")    # \n => next line
# f.close()

# f=open("sample.txt", "w")    # esari new file banxa
# f.close()

# f= open("demo.txt","r+")    # "r+" mode ma lekheko kura haru overwrite hunxa,starting of the file ma
# f.write("abc")              # 
# print(f.read())              # esle read garyo lekheko kura haru "terminal" ma
# f.close()

# f= open("demo.txt","w+")      ## Truncated =>> means cut short or incomplete /cut-off display, sabai kura delete hune,blank          
# print(f.read())           
# f.close()

# f= open("demo.txt","a+")      ## apend mode        
# print(f.read()) 
# f.write("abc")             
# f.close()

#### sumarize:- r+ =>  read + overwrite (pointer start ma hunxa)  ----> no truncate
##              w+ =>  read + overwrite                           ----> truncate
##              a+ =>  read + append ( pointer end ma hunxa)     ------> no truncate

###============>>>> with Syntax <<<<<====================
###Syntax =>>  with open("demo.txt","a") as f:
###            data= f.read()

# with open("demo.txt","r") as f:
#     data= f.read()
#     print(data)

# with open("demo.txt","w") as f:   
#     f.write("new data")             # naya data write garera show gareko

##====================>>> Deleting a File <<<==================
## using the os module
## Module(like a code library) is a file written by another programmer that generally has a functions we can use.
### Syntax =>> import os
###            os.remove(filename)
##             kunai aaru nai module chaieko xa bhani pre install garnu parxa , aahile os xa re tara paxi kunai aaru chaiyo bhani install
            
# import tensorflow  # No module named 'tensorflow', so we have to download it
# pip( package installer for python)install 

# import os
# os.remove("sample.txt")   # delete 

## ==========>>> LET'S PRACTICE <<<<===============
## Q.N.1. Create a new file "practice.txt" using python. Add the following data in it:
## Hi everyone
## we are learning File I/O
## using Java
## I like programming in Java.
## Ans =>>

# f=open("practice.txt","w")
# f.write("Hi everyone:)\nWe are learning File I/O\nusing Java.\nI like programming in Java.") 
# f.close()

### Q.N.2. WAF that replaces all occurrences of "Java" with "Python" in above file.
##ANS=>>
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data=data.replace("Java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

### Q.N.3. Search if the word "learning" exists in the file or not.
##ANS=>>
# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found")
# check_for_word()

### Q.N.4. WAF to find in which line of the file does the word"learning" occur first. Print -1 if word not found.
##ANS=>>
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no += 1
#     return -1
# check_for_line()               # Output: 2
# # print(check_for_line())       # yo print garda if ko case print hunxa/ return -1

### Q.N.5. From a file containing numbers separated by comma, print the count of even numbers.
###ANS =>
## Normal Code:
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)       # data aahile sabai string format ma xa

## data odd xa ki even xa sabai individual number nikalnu parxa ra integer ko value ma convert garnu parxa
## 1st ma = individual numbers
## 2nd ma = parse/casting(type cast to integer value)data lai convert garne, cast garne

## =>> this is basic method
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data) 

#     num =""             # empty string
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]

### =>> split method
# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data) 

#     nums = data.split(",")
#     print(nums)

## =>> Final = now we add "loop" in answer
# count = 0
# with open("practice.txt","r") as f:
#     data=f.read()

#     nums = data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
#     print(count)              # output is 5
