print("Welcome to the Quiz")
name=input("What's Your name? ")
choice=input(name+", do you want to play?(yes/no) ")
choice=str(choice)
if choice.lower()!="yes":
    quit()
print("Ok, Let's Get Started! :)")
score=0;
ques=input("What's the Capital of India? ")
if ques.lower()=="new delhi":                          #Here we're making it lower case so that if the user
    print("That's Correct!")                                                #messes up with the input format we can still evaluate that
    score+=1
else:
    print("Incorrect!")
ques=input("What does CPU stand for? ")
if ques.lower()=="central processing unit":
    print("That's Correct!")
    score+=1
else:
    print("Incorrect!")
ques=input("What does GPU stand for? ")
if ques.lower()=="graphics processing unit":
    print("That's Correct!")
    score+=1
else:
    print("Incorrect!")
ques=input("What does IT stand for? ")
if ques.lower()=="information technology":
    print("That's Correct!")
    score+=1
else:
    print("Incorrect!")
print(name+", you got "+str(score)+" questions correct! ")
