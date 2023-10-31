# Works in poetry and when installing with pip,
# Not recognised by VSCode when installing with pip
try:
    from mymodule.functions import print_hello
    print_hello()
except ModuleNotFoundError:
    print("Module not found when importing as mymodule.functions")

try:
    from mymodule import print_bye
    print_bye()
except ImportError:
    print("'from mymodule import print_bye' did not work")


# Works only in poetry, error with pip
# Recognised by VSCode when installing with poetry
try:
    from mymodule.mymodule.functions import print_hello as print_hello2
    print_hello2()
except ModuleNotFoundError:
    print("Module not found when importing as mymodule.mymodule.functions")

try:
    from mymodule.mymodule import print_bye as print_bye2
    print_bye2()
except ImportError:
    print("'from mymodule.mymodule import print_bye' did not work")
