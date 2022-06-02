import random
 
#Dictionary for game choices
gameOptions = {"R":"Rock","P":"Paper","S":"Scissors"}

#User's input function
def userInput():
  print("Enter your choice: R, P or S")
  userChoice = str(input())
  return userChoice

#flag to loop in case of a tie condition
flag="t"
userChoice = userInput()

while flag=="t":
    #"in" operator look for keys in dictionaries and not values. 
    while userChoice not in gameOptions:
        print("Error: Not a valid choice")
        userChoice = userInput()
    
    #choose at random from the dict for CPU
    cpuChoice = str(random.choice(list(gameOptions.keys())))
    
    #Get the value corresponding to the key chosen & print them
    print("Player (%s)" % gameOptions.get(userChoice) + " : CPU (%s)" % gameOptions.get(cpuChoice))

    #Making a list of user and CPU choices
    userCPUChoice = [userChoice, cpuChoice]
    
#The if block below could be optimized    
    if userCPUChoice == ["R","S"]:
        print("Player Wins")
        flag="p"
    elif userCPUChoice == ["P","R"]:
        print("Player Wins")
        flag="p"
    elif userCPUChoice == ["S","P"]:
        print("Player Wins")
        flag="p"
    
    if userCPUChoice == ["S","R"]:
        print("CPU Wins")
        flag="c"
    elif userCPUChoice == ["R","P"]:
        print("CPU Wins")
        flag="c"
    elif userCPUChoice == ["P","S"]:
        print("CPU Wins")
        flag="c"
    
    if userCPUChoice == ["S","S"]:
        print("It's a tie. Let's play again")
        flag="t"
        userChoice = userInput()
    elif userCPUChoice == ["R","R"]:
        print("It's a tie. Let's play again")
        flag="t"
        userChoice = userInput()
    elif userCPUChoice == ["P","P"]:
        print("It's a tie")
        flag="t"
        userChoice = userInput()
    
    #To Zuri Mentor - WHY is the below block not working?
    # if (userCPUChoice == ["R","S"] or ["P","R"] or ["S","P"]):
    #     print("Player Wins")
      
    # if (userCPUChoice == ["S","R"] or ["R","P"] or ["P","S"]):
    #     print("CPU Wins")
    
    # if (userCPUChoice == ["S","S"] or ["R","R"] or ["P","P"]):
    #     print("It's a tie")
