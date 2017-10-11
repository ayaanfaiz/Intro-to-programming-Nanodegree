statement=["Domino's Pizza is an _1_ pizza restaurant chain and international franchise pizza delivery corporation headquartered at the _2_, United States. Founded in _3_",
           "India, is a country in _1_ Asia. It is the seventh-largest country by area, the second-most populous country with over 1.2 _2_ people, and the most populous _3_ in the world.",
           "Udacity is a organization founded by _1_ Thrun David Stavens and Mike Sokolsky offering massive open _2_ courses .According to Thrun the origin of the name Udacity comes from the company's desire to be _3_ for you the student."]
answer=[["american","michigan","1960"],["south","billion","democracy"],["sebastian","online","audacious"]]
        
def mad_lib():
        print("Welcome to Mad-Lib ")
        level()
def level():
        user_input=input("Enter the level you want to select from\n1.Beginner\n2.Intermediate\n3.Expert\n").lower()
        level_select=["beginner","intermediate","expert"]
        index=0
        flag=0
        while index<3:
                if(user_input==level_select[index]):
                           print(statement[index])
                           flag=1
                           break
                index+=1
        if(flag==0):
                print("Wrong selection!!! Please try again \n ")
                level()
        replace(index)
def replace(index):
        place=1
        temp=["","",""]
        temp[index]=statement[index]
        while place<4:
                user_answer=input("Enter "+str(place)+" :- ").lower()
                if(user_answer==answer[index][place-1]):
                        statement[index]=statement[index].replace(("_"+str(place)+"_"),answer[index][place-1])
                        print(statement[index])
                        place=place+1
                else:
                        print("Wrong Answer!!! Please try again \n")
        statement[index]=temp[index]
        further()
def further():
        forward=input("If you wish to continue forward then enter yes else enter no :- ")
        if(forward=="yes"):
                mad_lib()
        elif(forward=="no"):
                print("Thank You!!!")
        else:
                print("Wrong input!!! Please try again \n")
                further()
mad_lib()
