# chutiye=["Aakash", "Ankit", "Aditya", "Vishu", "Hoshang", "Tannu"]
# print(len(chutiye))


# row1=["🤌","🤌","🤌"]
# row2=["🤌","🤌","🤌"]
# row3=["🤌","🤌","🤌"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# #☠️
# enter_position=input("Enter the position: ")
# row=int(enter_position[0])
# column=int(enter_position[1])
# map[row-1][column-1]='☠️'
# print(map)

#👊1 ✊0 ✌️2
import random
enter_choice=int(input("0.Paper 1.Rock 2.Scisors: \n"))
if enter_choice==0:
    print('✊')
if enter_choice==1:
    print('👊')
if enter_choice==2:
    print('✌️')
computer_choice=random.randint(0,2)
if computer_choice==0:
    print('✊')
if computer_choice==1:
    print('👊')
if computer_choice==2:
    print('✌️')

if enter_choice==0 & computer_choice==1:
    print('You win')
elif enter_choice==1 & computer_choice==2:
    print('You win')
elif enter_choice==2 & computer_choice==0:
    print('You win')
elif enter_choice==computer_choice:
    print('Draw')
else:
    print('You Lose')




