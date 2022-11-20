  #This is a simple quiz program for beginners in programming
  #User need to type the exact answer as defined or it will be considered incorrect

print("Welcome to python quiz") #print statement

playing = input("Do you want to play? ")
score = 0 # to calculate the score

if playing.lower() != "yes":  #lower() is a built in fuction that converts the input to lower case
    quit()

print(" okay let's play ")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit": #we can use .lower in this place as well as you see in the below example
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print('correct')
    score += 1
else:
    print('incorrect')

print("your score is " +str(score))
print("you got " +str((score/4)*100)+ "%") #calculate the total percentage "(value/total value)×100%."



