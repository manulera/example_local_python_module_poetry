# Works in poetry and when installing with pip,
# Not recognised by VSCode when installing with pip only
from mymodule.functions import print_hello

# Works only in poetry, error with pip
# Recognised by VSCode when installing with poetry only
from mymodule.mymodule.functions import print_hello as print_hello2

print_hello()
print_hello2()
