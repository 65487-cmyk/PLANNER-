import random



print('who are you? ')
 #ask the user to input name
name=input().lower()
if name == 'vee':
    print(f'welcome {name}')

elif name!='vee':
    print('unidentified username try again')

    
    
#number of turns to input correct password
max_trial=3
turn_trial=0
while turn_trial < max_trial:
    password=input('what is the password?: ').capitalize().strip()
    if password == 'Bananas':
        print('acccess granted')
        break
    else:
        print('wrong password')
    turn_trial +=1
    continue
if turn_trial == max_trial:
    print('access denied!')
    exit()

#outlay of financial planner
#finacial calculator
#testing git
#ask vee to input the total income
def total_income():
    x=input('enter your total income \n')
    cash=int(x)
    return cash

def expense():
    t_expense=(50/100 * total_income())
    print (f'Your total budget for expenses is {t_expense}')
expense()
d={}
numbers=int(input('enter the total number of categories: '))
for number in range(numbers):
    expenditure=input('enter the expenditure category: ')
    amount=int(input('enter the amount to cater for the specific expenditure: '))
    d[expenditure]=amount
print(d)
print(f'The total amount spent on expenses is equal to {sum(d.values())}')

if sum(d.values()) <= expense():
    print('you are within the suitable range')









   
    
