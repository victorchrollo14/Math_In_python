import re
import Basic_calculation


print("The chapters are:\ncalculus\tnumerical Methods")
option = input("Enter the Chapter name: ")

if (re.search('^cal', option)):
     from Basic_calculation import calculus

if (re.search('^num', option)):
     from Basic_calculation import num_methods

