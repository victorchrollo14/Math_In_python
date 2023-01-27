# giving the users chapter names to select from


chapter_name = {
    1: "calculus",
}

print(f"The chapters are:\n{chapter_name}")
option = input(f"enter the chapter number: ")


if (int(option) == 1):
    from Basic_calculation import calculus
