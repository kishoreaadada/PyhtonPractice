# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from practiceScenarios import practiceFunctions


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(practiceFunctions.calculator(12, 13))
    print(practiceFunctions.calculator(24, 13, 'add'))
    print(practiceFunctions.calculator('12', 45, 'subtract'))
    print(practiceFunctions.calculator(34, 56, 'multiply'))
    print(practiceFunctions.calculator(39, '13', 'divide'))
    print(practiceFunctions.calculator(12, 13, 'all'))
    print(practiceFunctions.calculator('12', '13', 'percent'))
    print(practiceFunctions.greatestnumber(23, 45, 89, 93, 20, 10, 109, 0, 89))
    print(practiceFunctions.greatestnumber(*range(100, 1000)))
    practiceFunctions.stringactions("inceptez technologies")
