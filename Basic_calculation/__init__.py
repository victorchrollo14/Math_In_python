
chapter_name = {'1 : calculus','2 : numerical Methods 1','3 : numerical Methods2','4 : Partial Differential Equations','5 : Vector calculus'}
print(f"The chapters are:\n{chapter_name}")
option = input("Enter the Chapter number: ")

if (option == '1'):
     from Basic_calculation import calculus

if (option == '2'):
     from Basic_calculation import numerical_methods

