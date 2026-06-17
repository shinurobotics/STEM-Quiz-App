import random as r

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
Questions = {"What is 2+2?":"4","What is  the SI unit of force?": "newton","What is the chemical symbol of Oxygen?":"o","Which planet is known as the Red Planet?":"mars","Which organelle provides energy?":"mitochondria"}
#Answers
Answers = ["4","newton","o","Mars","mitochondria"]
Score = 0
for ques in range(0,5):
    Randomques = r.choice(list(Questions))
    print(Randomques)
    ans = input("Please type ur ans: ")
    if ans.lower() == Questions[Randomques]:
        print("Correct")
        Score += 1
    else:
        print("Incorrect")
        Score = 0
    del Questions[Randomques]

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
