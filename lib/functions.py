#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Guido"):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return(num1+num2)

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
    else:
        raise TypeError("Input must be an integer or float")

