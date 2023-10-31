# Works in poetry and when installing with pip,
# Not recognised by VSCode when installing with pip
try:
    from mymodule.functions import print_hello
    from mymodule import print_bye
    print_hello()
    print_bye()
except ModuleNotFoundError:
    print("Module not found when importing as mymodule.functions")


# Works only in poetry, error with pip
# Recognised by VSCode when installing with poetry
try:
    from mymodule.mymodule.functions import print_hello as print_hello2
    from mymodule.mymodule import print_bye as print_bye2
    print_hello2()
    print_bye2()
except ModuleNotFoundError:
    print("Module not found when importing as mymodule.mymodule.functions")
