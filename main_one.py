# Activities & Practices

# 01 "Large Power"
# For the first code challenge, we are going to create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return [True] if the result is greater than 5000 or return [False] if it is not. In order to accomplish this, we will need the following steps:

# 1. Define the function to accept two input parameters called [base] and [exponent]
# 2. Calculate the result of base to the power of [exponent]
# 3. Use an [if] statement to test if the result is greater than 5000. If it is then return [True]. Otherwise, return [False]

# Create a function named [large_power()] that takes two parameters named [base] and [exponent].
# If [base] raised to the [exponent] is greater than [5000], return [True], otherwise return [False]

# Hint: Make sure you use [if] and [else] statements to [return True] or [return False]. 
# Also, to take the power of one number to another number you can use the [**] operator.
print("Large Power challenge")
def large_power(base, exponent):
  result = base ** exponent
  if result > 5000:
    return True
  return False

# or you can do this:
# if base ** exponent > 5000: return True .. etc.  

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# # should print True
print(large_power(2, 12))
# should print False
print("----------------------------")

# 02 "Over Budget"
# Let’s say we are trying to save some money and we are watching our budget. We need to make sure that the result of our spending is less than the total amount we have allocated for each of the categories. Our function will accept a parameter called [budget] which describes our spending limit. The next four parameters describe what we are spending our money on. We need to sum all of our spendings and compare it to the budget. If we have gone over budget, we will return [True]. Otherwise we return [False]. Here are the steps we need:

# 1. Define the function to accept five parameters starting with [budget] then [food_bill], [electricity_bill], [internet_bill], and [rent]
# 2. Calculate the sum of the last four parameters
# 3. Use [if] and [else] statements to test if the budget is less than the sum of the calculated sum from the previous step.
# 4. If the condition is true, return [True] otherwise return [False]

# Create a function called [over_budget] that has five parameters named [budget], [food_bill], [electricity_bill], [internet_bill], and [rent].
# The function should return [True] if [budget] is less than the sum of the other four parameters — you’ve gone over budget! Return [False] otherwise.
print("Over Budget")
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  sum = food_bill + electricity_bill + internet_bill + rent
  if budget < sum:
  # or | if budget < (food_bill + electricity_bill + internet_bill + rent):  
    return True
  else:
    return False 

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# # should print False
print(over_budget(80, 20, 30, 10, 30))
# # should print True      
print("----------------------------")

# 03 "Twice As Large"
# In this challenge, we will determine if one number is twice as large as another number. To do this, we will compare the first number with two times the second number. Here are the steps:

# 1. Define our function with two inputs [num1] and [num2]
# 2. Multiply the second input by 2
# 3. Use an [if] statement to compare the result of the last calculation with the first input
# 4. If num1 is greater then return [True] otherwise return [False]

# Create a function named [twice_as_large()] that has two parameters named [num1] and [num2].
# Return [True] if [num1] is more than double [num2]. Return [False] otherwise.
print("Twice As Large")
def twice_as_large(num1, num2):
  num2 = num2 * 2
  if num1 > num2:
    return True 
  return False 

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True   
print("----------------------------")

# 04 "Divisible By Ten"
# To make things a bit more challenging, we are going to create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

# 1. Define the function header to accept one input [num]
# 2. Calculate the remainder of the input divided by 10 (use modulus)
# 3. Use an [if] statement to check if the remainder was 0. If the remainder was 0, return [True], otherwise, return [False]

#Create a function called [divisible_by_ten()] that has one parameter name [num]
# The function should return [True] if [num] is divisible by [10], and [False] otherwise. Consider using modulo operator [%] to check for divisibility.
print("Divisible By Ten")
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  return False 

# Uncomment these print() function calls to test your divisible_by_ten() function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False   
print("----------------------------")

# 05 "Not Sum To Ten"
# Finally, we are going to check if the summation of two inputs does not equal ten. Our function will accept two inputs and add them together. If the two numbers added together are not equal to ten, then we will return [True], otherwise, we will return [False]. Here is what we need to do:

# 1. Define the function to accept two parameters, [num1] and [num2]
# 2. Add the two parameters together
# 3. Test if the result is not equal to 10
# 4. If the sum is not equal, return [True], otherwise, return [False]

# Create a function named [not_sum_to_ten()] that has two parameters named [num1] and [num2].
# Return [True] if [num1] and [num2] do not sum to 10. Return [False] otherwise.
print("Not Sum To Ten")
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True 
  return False  

# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False  