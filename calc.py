#!/usr/bin/python3

action_sign = ['+', '-', '*', '/']

def main():
    while True:
        action = input("Action: + - * / : ")
        if str(action) not in action_sign:
            break
        num1 = input("Num1: ")
        num2 = input("Num2: ")
        
        if action == '+':
            try:
                result = int(num1) + int(num2)
                print("answer: ", result)
            except:
                print("Not a number")
        elif action == '-':
            try:
                result = int(num1) - int(num2)
                print("answer: ", result)
            except:
                print("Not a number")
        elif action == '*':
            try:
                result = int(num1) * int(num2)
                print("answer: ", result)
            except:
                print("Not a number") 
        elif action == '/':
            try:
                result = int(num1) / int(num2)
                print("answer: ", result)
            except:
                print("Not a number")

main()
