start = "Welcome to STEM Quiz app"
print(start)
name = input("Please type your name: ")
print(name)
Question1 = "What is 2+2?"
Question2 = "What is  the SI unit of force?"
Question3 = "What is the chemical symbol of Oxygen"
Question4 = "Which planet is known as the Red Planet"
Question5 = "Which cell provides energy"
Score = 0
print(Question1)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans == str(4):
    print("correct")
    Score += 1
    print("currentscore:",Score)
else:
    print("incorrect")
    print("currentscore:",Score)
print(Question2)
Ans = input("Please give ur ans: ")
print(Ans)
if Ans.lower() == "newton":
    print("correct")
    Score += 1
    print("currentscore:",Score)
else:
    print("incorrect")
    print("currentscore:",Score)
print(Question3)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "o":
    print("correct")
    Score += 1
    print("currentscore:",Score)
else:
    print("incorrect")
    print("currentscore:",Score)        
print(Question4)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "mars":
    print("correct")
    Score += 1
    print("currentscore:",Score)
else:
    print("incorrect")
    print("currentscore:",Score)
print(Question5)
Ans = input("Please give ur ans: ")
print(Ans)
if  Ans.lower() == "mitochondria":
    print("correct")
    Score += 1
    print("currentscore:",Score)
else:
    print("incorrect")
    print("currentscore:",Score)
if Score > 3:
    print("Overall score:",(Score/5*100))
    print("Excellent")
elif Score == 3:
    print("Overall score:",(Score/5*100))
    print("Good")
else:
    print("Overall score:",(Score/5*100))
    print("Try again")
print("Thank you")
