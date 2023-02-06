"""
    Used to select the chapter name and run the package based on user's choice.

"""


if __name__ == '__main__':
    chapter_name = {
        1: "calculus",
        2: "fourier Series",
        3: "Fourier Transform",
        4: "second order PDE's",
        5: "Calculus of variation"
    }

    print(f"The chapters are:")
    for chapter in chapter_name:
        print(chapter, chapter_name[chapter])

    option = int(input(f"enter the chapter number: "))

    if (option == 1):
        from Basic_calculation import calculus

    elif (option == 2):
        from Fourier_series import fourier_series
    
    elif (option == 4):
        from Module4 import mod4
    
    else:
        print("wrong option")


