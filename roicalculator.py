import time
class ROICalculator():
    def __init__(self, name, property, location):
        self.name = name
        self.property = property
        self.location = location

    def getIncomes(self):
        incomes = {} #dict of {'income': revenue}
        defaultIncomes = ["RENTAL", "LAUNDRY", "STORAGE"]
        print("="*20)
        print(f"Step 1 -> Enter Income Streams of {self.property}\n")
        # print("Here you will enter all your income streams from this rental property:")
        for income in defaultIncomes:
            # print()
            while True:
                value = input(f"What is your {income} income? (float/int): ")
                if value.isdigit():
                    incomes[income] = float(value)
                    break
            
        miscell = input("Do you have any miscellanous income? y - yes | n - no: ").lower().strip()
        if miscell == 'y':
            while True:
                name = input("Enter name of income please or type stop to stop: ").lower().strip()
                if name == "stop":
                    break
                while True:
                    value = input(f"What is your income of {name.title()}? (float/int): ")
                    if value.isdigit():
                        incomes[name] = int(value)
                        break
            
        print(f"INCOME STREAMS of {self.property}")
        for key, value in incomes.items():
            print(f"\t{key} : {value}")
        print(f"\tTotal income is {sum(incomes.values())}")
        print("="*20)

        self.incomes = incomes

    def getExpenses(self):
        expenses = {}
        defaultExpenses = ["Tax", "Insurance", "Utilities", "HOA", "Lawn/Snow", "Vacancy", "CapEX", "Repairs", "Property Management", "Mortgage"]
        defaultUtilities = ["Electricity", "Gas", "Water", "Garbage", "Sewer"]
        print("="*20)
        print(f"Step 2 -> Enter Monthly Expenses of {self.property}\n")
        for expense in defaultExpenses:
            if expense == "Utilities":
                utilExpense = input("Do you pay for utilities? y-yes n-no: ").lower().strip()
                if utilExpense == 'y':
                    print()
                    for utility in defaultUtilities:
                        while True:
                            value = input(f"Enter value for {utility} utility (float/int): ")
                            if value.isdigit():
                                expenses[utility] = float(value)
                                break
            else:
                while True:
                    value = input(f"Enter expense for {expense} (float/int): ")
                    if value.isdigit():
                        expenses[expense] = float(value)
                        break

        print(f"EXPENSES FOR {self.property}")
        print("="*20)
        for key, value in expenses.items():
            print(f"\t{key} : {value}")

        print(f"Total EXPENSES are {sum(expenses.values())}")
        self.expenses = expenses

    def getCashFlow(self):
        expenses = self.expenses.values()
        income = self.incomes.values()
        return sum(income) - sum(expenses)

    def getInvestments(self):
        
        defaultPayments = ["Down Payments", "Closing Costs", "Repairs", "Miscellanous"]
        investments = {}
        print("="*20)
        print("Step 3 -> Now its time to enter your INVESTMENTS!")
        for payment in defaultPayments:
            while True:
                value = input(f"Enter value for {payment} (float/int): ")
                if value.isdigit():
                    investments[payment] = float(value)
                    break

        print("="*20)   
        for key, value in investments.items():
            print(f"{key} : {value}")

        print(f"Total investments: {sum(investments.values())}")
        self.investments = investments

    def getROI(self):
        print("Calculating ROI...")
        time.sleep(3)
        investments = sum(self.investments.values())
        cashFlow = self.getCashFlow() * 12
        print(f"Total investments: {investments}\nTotal cashFlow: {cashFlow}")
        ROI = cashFlow / investments
        print(f"ROI is {round(ROI*100,5)}%")
        print("Thanks for using our ROICalculator, have a nice day")

    def runCalculator(self):
        print("\n\nThis is a 3-step process where you must first enter your incomes from this property\nThen enter your expenses for the said property and\nfinally enter whatever inital investments you have made.")
        print("Once that is done, we can give you your estimated ROI(Return On Investment)!")
        self.getIncomes()
        self.getExpenses()
        self.getInvestments()
        self.getROI()