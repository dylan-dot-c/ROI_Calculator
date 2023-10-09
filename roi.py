# python program to calculate ROI
# FIRST IS INCOME,
#Then calculate Expenses
# Then calculate Investments
# finally return cashflow*12/investments
from roicalculator import ROICalculator

def main():
    print("Welcome To BIGGER POCKETS!")
    name = input("Enter your name to get started: ").strip().title()
    property = input("Enter name of the property: ").strip().title()
    location = input("Enter location of property: ").strip().title()
    calculator = ROICalculator(name, property, location)
    print("This is a 3-step process where you must first enter your incomes from this property\nThen enter your expenses for the said property and\nfinally enter whatever inital investments you have made.")
    print("Once that is done, we can give you your estimated ROI(Return On Investment)!")
    calculator.getIncomes()
    calculator.getExpenses()
    calculator.getInvestments()
    calculator.getROI()

main()