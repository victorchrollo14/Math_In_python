

# giving the users chapter names to select from


chapter_name = {

    0: "Sympy_features",
    1: "calculus",
    2: "numerical methods",
    4: "Partial differential Equations"
}

print(f"The chapters are:\n{chapter_name}")
option = input(f"enter the chapter number: ")

# if (int(option) == 0):
#     from OtherChapters import sympy_feat

if (int(option) == 1):
    from Basic_calculation import calculus

# if (int(option) == 2):
#     from OtherChapters import numerical_methods

# if (int(option) == 4):
#     from Basic_calculation import pde
