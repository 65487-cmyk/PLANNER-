import random



print('who are you? ')
 #ask the user to input name
name=input().lower()
if name == 'vee':
    print(f'welcome {name}, whats the password?')

elif name!='vee':
    print('unidentified username')
    
#number of turns to input correct password
max_trial=3
turn_trial=0
while turn_trial <max_trial:
    password=input().capitalize().strip()
    if password == 'Bananas':

        print('acccess granted')
        break
    else:
        print('wrong password!Try again')
    turn_trial +=1
    if turn_trial == max_trial:
        print('access denied!')
#outlay of financial planner
#finacial calculator
#testing git
#ask vee to input the total income to be budgeted for
total_income=()
def c_income(total_income):
    x=(input('enter your average income'))
    total_income=int(x)
    value=c_income(total_income)
    return'your average income is {value} kes'
