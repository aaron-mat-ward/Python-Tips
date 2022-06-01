# -----------------------------------------------------------------------------
#                               VARIABLES:
# -----------------------------------------------------------------------------
#   PURPOSE :   Variables are containers for storing data values.
#               A variable is created when you first assign a value to it.
#               Variable names are case-sensitive.
#               String variables can be declared either by using
#                   single or double quotes:
#
#   NAMING  :   DYNAMIC: A variable whose value changes.
#               Use a lowercase single letter, word, or words.
#               Separate words with underscores to improve readability.
#                   Example: x, var, my_variable
#
#               CONSTANT: A variable whose value cannot be changed.
#               Use a UPPERCASE single letter, word, or words.
#               Separate words with underscores to improve readability.
#                   Example: X, VAR, MY_CONST
#
#               !Variable names cannot start with a number or include spaces!
# -----------------------------------------------------------------------------

# DYNAMIC VARIABLES:
x = 1
var = "hello"
my_variable = 3.14

# CONST VARIABLES:
X = 1
VAR = "hello"
MY_CONST = 3.14


# You can get the data type of a variable with the type() function:
type(x)  # returns   int (Integer)
type(var)  # returns   str (String)
type(my_variable)  # returns   float (Floating Point Decimal)


# You can convert the data types of variables with the casting function:
x = float(1)  # 1 -> 1.0
my_variable = int(3.14)  # 3.14 -> 3


# You can display variables in the terminal with the print() function:
print(my_variable)


# You can assign variables in the terminal with the input() function:
# !! The return value from the input function will always be a str !!
input_variable = input("Enter a number: ")

type(input_variable)  # returns   str (String)

#   Change the input type by casting:
input_variable = int(input("Enter a number: "))

type(input_variable)  # returns   int (interger)
