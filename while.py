#the program calculates the average of the numbers entered excluding the -1
sum=0
n=0
user_input=int(input("Please enter a number (-1 to exit):"))
while user_input!=-1:    #loop will execute unless user enters -1
    n+=1
    sum+=user_input
    user_input=int(input("Please enter a number (-1 to exit):"))

if user_input==-1:     #if the user enters -1 loop will end and the average of the entered numbers will be calculated
    average=sum/n
    print(f"average: {average}")