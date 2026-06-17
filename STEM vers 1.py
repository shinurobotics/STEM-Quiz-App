#Welcome screen
start = "STEM Quiz app"
print("="*32)
print(start.center(32))
print("="*32)
name = input("Please type your name: ")
print("Welcome"+ "," + name + "!")
print("1,2,3")
print("Lets begin")
#Questions
Question1 = "What is 2+2?"
Question2 = "What is  the SI unit of force?"
Question3 = "What is the chemical symbol of Oxygen?"
Question4 = "Which planet is known as the Red Planet?"
Question5 = "Which organelle provides energy?"
Score = 0

print(Question1)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans == str(4):
    print("Correct")
    Score += 1
    print("Current score:",Score)
else:
    print("Incorrect")
    print("Current score:",Score)
print(Question2)
Ans = input("Please give ur ans: ")
print(Ans)
if Ans.lower() == "newton":
    print("Correct")
    Score += 1
    print("Current score:",Score)
else:
    print("Incorrect")
    print("Current score:",Score)
print(Question3)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "o":
    print("Correct")
    Score += 1
    print("Current score:",Score)
else:
    print("Incorrect")
    print("Current score:",Score)        
print(Question4)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "mars":
    print("Correct")
    Score += 1
    print("Current score:",Score)
else:
    print("Incorrect")
    print("Current score:",Score)
print(Question5)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "mitochondria":
    print("Correct")
    Score += 1
    print("Current score:",Score)
else:
    print("Incorrect")
    print("Current score:",Score)
#Total score update
if Score > 3:
    print("Overall score:",int((Score/5*100)))
    print("Excellent")
elif Score == 3:
    print("Overall score:",int((Score/5*100)))
    print("Good")
else:
    print("Overall score:",int((Score/5*100)))
    print("Try again")
#Thank you message
print("Thank you for using STEM Quiz App!")
