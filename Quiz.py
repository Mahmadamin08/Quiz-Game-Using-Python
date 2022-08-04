print('\n')
print("Welcome to My Computer quiz!")

plying = input("Do you want to play?? \n")

if plying.lower() !="yes":
    print('Ok! WE HOPE YOU THIS IN FUTERE!')
    quit()

print("Okay! Let's play :)")
score = 0
print('\n')
ans= input("Who Is Ms Dhoni? \n")
if ans.lower() == "most successfull captain":
    print('Yeahhhh !!! Your anshwer is Correct!')
    score+=1
else:
    print('Oopps! Your Answer is Wrong!')
    print('Correct! Answer is Most Successfull Captain')
print('\n')

ans=input("What does CPU stands for? \n")
if ans.lower()=='central processing unit':
    print("Yeahhhh !!! Your anshwer is Correct!") 
    score=score+1
else:
    print('Oopps! Your Answer is Wrong!')
    print('Correct! Answer is Central Processing Unit')
print('\n')

ans=input("What does GPU stand for? \n")
if ans.lower()=='graphics processing unit':
    print("Yeahhhh !!! Your anshwer is Correct!")
    score=score+1
else:
    print('Oopps! Your Answer is Wrong!')
    print('Correct! Answer is Graphics Processing Unit')
print('\n')

ans=input("What does RAM stand for? \n")
if ans.lower()=='random access memory':
    print("Yeahhhh !!! Your anshwer is Correct!")
    score=score+1
else:
    print('Oopps! Your Answer is Wrong!')
    print('Correct! Answer is Random Access Memory')
print('\n')

ans=input("What does PSU stand for? \n")
if ans.lower()=='power supply':
    print("yay!Your anshwer is Correct!")
    score=score+1
else:
    print('Oopps! Your Answer is Wrong!')
    print('Correct! Answer is Power Supply')
print('\n')

print("Your got"+ str(score)+ "Correct!")
pr=(score/5)*100
print("Your percentage score is "+ str(pr))