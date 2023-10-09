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
    calculator.runCalculator()

main()