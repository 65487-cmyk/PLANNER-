class User:

    def __innit__(self,total_income, savings, expenses, aob):
        self.total_income=()
        self.savings=()
        self.expenses={}
        self.aob=()
    #total income
    def calculate_income(self):
        self.total_income=(input('enter your total average income /n'))
        self=int(self.total_income)
    value=calculate_income('self')
        
    print(f'your average income is {value}')

    #condition for savings
    def calculate_savings(self):
        self.savings=(50/100 * self.total_income) #kes 
        self=self.savings
        self()

        
        print('self')

        #expenses
    def calculate_expenses(self):
        self.expenses={}
        num_entries=int(input('enter total number of entries'))
        for i in range(num_entries):
            expenditure=input("enter expense category i.e rent")
            amount=int(input()) #kes
            self.expenses[expenditure]=amount
           
        print('self.expenses')
        print(sum(self.expenses.values()))

        #Condition
        if sum(self.expenses.values()) ==(30/100 * self.total_income):
            print('your expenditure obeys the spending rule')
        
        else:
            print('it doesnt meet required formula')
        

        #aob
    def calculate_aob(self,avrg_aob):
        self.aob=(20/100 * self.total_income)
        self.aob=avrg_aob
        print(self.aob)


def main():
    planner= User()
    planner.calculate_income()
    planner.calculate_savings()
    planner.calculate_expenses()
    planner.calculate_aob()


main()