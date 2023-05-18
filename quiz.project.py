print("Welcome to mu quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay,glad you said that,lets play!:)")  
score=0 

answer = input ("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score+=1
else:
    print('sorry,its not correct , try again')    

answer = input ("How do you insert COMMENTS in Python code? ")
if answer.lower() == "#this is comment":
    print('Correct')
    score+=1
else:
    print('sorry,its not correct , try again') 

answer = input (" Which method can be used to remove any whitespace from both the beginning and the end of a string? ")
if answer.lower() == "strip()":
    print('Correct')
    score+=1
else:
    print('sorry,its not correct , try again') 

answer = input (" Which method can be used to return a string in upper case letters? ")
if answer.lower() == "upper()":
    print('Correct')
    score+=1
else:
    print('sorry,its not correct , try again')     

print("you got" + str(score)  + "question correct"  )
    

