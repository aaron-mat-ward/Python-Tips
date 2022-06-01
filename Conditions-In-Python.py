# -----------------------------------------------------------------------------
#                               CONDITIONS:
# -----------------------------------------------------------------------------
#   PURPOSE :   Compares the value of two things against one another.
#               Python uses boolean logic to evaluate conditions.
# 
#   LOGICAL CONDITIONS: Python supports the usual conditions from mathematics:
#  
#               Equals: ==
#               Not Equals: !=
#               Less than: <
#               Less than or equal to: <=
#               Greater than: >
#               Greater than or equal to: >=
#   
#   CHAINING CONDITIONS: You can chain one or more expressions together 
#                         with operators:
#                           
#               Operators:
#                   and     Requires both conditions to be True
#                   or      Requires either condition to be True
#                   not     Reverses the condition.
# -----------------------------------------------------------------------------

# Conditional Expressions used on numbers (Integers or Floats):
1 > 2                       # returns False
1 == 1                      # returns True
1 != 3                      # returns True

# Conditional Expressions used on variables:
variable_a = 1
variable_b = 2

variable_a > variable_b     # returns False
variable_a != variable_b    # returns True


# Conditional Expressions used on characters:
#   This works by comparing the characters ASCII values.
#       The ord() function returns ASCII value.
'a' == 'A'                  # returns False
'a' > 'A'                   # returns True

ord('a')                    # returns int(97)
ord('A')                    # returns int(65)


# Chaining conditions with boolean operators:
true_condition = True
false_condition = False

true_condition and false_condition    # returns False
true_condition and false_condition    # returns True

true_condition or false_condition     # returns True
false_condition or false_condition    # returns False

not true_condition                    # returns False
not false_condition                   # returns True
