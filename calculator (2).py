#vera bandura
#Create a program that prompts users to enter two numbers, an operator, and prints the result of the operation
#init
#Functions
def main():
    print("Welcome to simple calculator!")
    print("Can do addition, subtraction, division, multiplication")
    num1 = int(input("Please enter number: "))
    num2 = int(input("Please enter number: "))
    operator = input("Please enter an operator (+, -, *, /): ")
    if operator == "+":
        print(calc_sum(num1,num2))
    if operator == "-":
        print(calc_dif(num1,num2))
    if operator == "*":
        print(calc_mult(num1,num2))
    if operator == "/":
        print(calc_div(num1,num2))
def calc_sum(x,y):
    return x + y
def calc_dif(x,y):
    return x - y
def calc_mult(x,y):
    return x * y
def calc_div(x,y):
    return x / y
#main
main()
