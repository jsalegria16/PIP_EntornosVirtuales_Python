options = ("stone", "paper", "scisors")
import random 
rounds = 1
userWins = 0
pcWins = 0

while True:
    print('*'*10)
    print('round',rounds)
    print('*'*10)
    print('Pc: ', pcWins, 'You: ', userWins)
    UserOption = input("Type Stone, paper or scisors: >>").lower()
    PcOption = random.choice(options).lower()
    rounds +=1
    
    if(UserOption in options):
        
        
        #print(random.randrange(1, 10))
        print(f"You selected {UserOption} and Pc selected {PcOption}")

        if UserOption == PcOption :
            print("There is not winner.")
        elif (UserOption == "stone" and PcOption == "scisors") or \
            (UserOption == "paper" and PcOption == "stone") or \
            (UserOption == "scisors" and PcOption == "paper"):
            #print("User is winner.")
            userWins+=1
            if userWins == 2:
                print('User wins with ', userWins, 'points')
                break
        else:
            #print("Pc is winner.")
            pcWins +=1
            if pcWins == 2:
                print('Pc is winner with ', pcWins, 'points')
                break
    else:
        print("Please select a correct option!.")