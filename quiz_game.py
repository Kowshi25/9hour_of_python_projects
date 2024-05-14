print("Hey! Do you wanna play some math quiz ?")
response = input()
if response.lower() == "yes":
    print("OK, then let's play some quiz.")
else:
    quit()
score =0
ans = input("Q1. ((25/5)*5 - 5) - 20? ")
if ans == "0" :
    print("Correct!")
    score +=1
else:
    print("Wrong")

ans = input("(100 - 100) + 25? " )
if ans!= "25":
    print("Wrong")
else:
    print("Correct!")
    score += 1

ans = input("4 * 4 * 4? ")
if ans != "64":
    print("Wrong")
else:
    print("Correct!")
    score += 1

print("Your total score is " + str(score)+ " marks")

