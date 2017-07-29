#Statements and answers for the quiz
statement=["Domino's Pizza is an _1_ pizza restaurant chain and international franchise pizza delivery corporation headquartered at the _2_, United States. Founded in _3_ by _4_ Monaghan.",
           "India, is a country in _1_ Asia. It is the seventh-largest country by area, the second-most populous country with over 1.2 _2_ people, and the most populous _3_ in the world. Its national languages is _4_.",
           "Udacity is a organization founded by _1_ Thrun, _2_ Stavens and _3_ Sokolsky offering massive open online courses .According to Thrun the origin of the name Udacity comes from the company's desire to be _4_ for you the student."]
answer=[["american","michigan","1960","james"],["south","billion","democracy","hindi"],["sebastian","david","mike","audacious"]]

#Function which is called for the first time
#Behavious : Welcomes the user to the Quiz game
#Calls funtion level which drives the program further
def mad_lib():
        print("Welcome to Mad-Lib ")
        level()
#To prompt user to select levels and enter them
def level():
        user_input=raw_input("Enter the level you want to select from\n1.Beginner\n2.Intermediate\n3.Expert\n").lower()
        level_select=["beginner","intermediate","expert"]
        index=0
        flag=0
        #Levels define the number of levels in the game
        levels = 3
        while index<levels:
                if(user_input==level_select[index]):
                           print(statement[index])
                           flag=1
                           break
                index+=1
        if(flag==0):
                print("Wrong selection!!! Please try again \n ")
                level()
        #Calls the replace function and passes the argument of the index which is selected.
        replace(index)
#To ask user for the answer and if the user enters correct answer then it replace with the blank else prompt answer once again
def replace(index):
        place=1
        temp=["","",""]
        temp[index]=statement[index]
        #maximum variable saves the number of answers. It tells how many times to reun the loop
        maximum = 4
        while place<=maximum:
                user_answer=raw_input("Enter "+str(place)+" :- ").lower()
                #Checks the condition if the answer entered by the user is correct or not
                if(user_answer==answer[index][place-1]):
                        #The below statement replaces the answer with the desired index if the answer is coorect
                        statement[index]=statement[index].replace(("_"+str(place)+"_"),answer[index][place-1])
                        print(statement[index])
                        place=place+1
                else:
                        #If the answer is wrong the 
                        print("Wrong Answer!!! Please try again \n")
        statement[index]=temp[index]
        further()
#Prompts user that if he/she wants to play the game again
def further():
        forward=raw_input("If you wish to continue forward then enter yes else enter no :- ")
        if(forward=="yes"):
                mad_lib()
        elif(forward=="no"):
                print("Thank You!!!")
        else:
                print("Wrong input!!! Please try again \n")
                further()
mad_lib()
