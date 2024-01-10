"""Python code for Calculator where using Dictonary to store the Operations and directing the Key = operator and
Value = function, Also calculate continueously with the previous answer and when the user don't want to continue
with the previous calculation then reset the calculator."""

from replit import clear
from art import cal
import random

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


# creating an dictonary to store the functions as value and the operator as key.
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  print(random.choice(cal))

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)       # It will direct to dictonary and the parameter are assigned to n1 and n2.
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()      # This is recurssion where, when the user don't want to continue with the previous calculation then it will start with new calculation.

calculator()
