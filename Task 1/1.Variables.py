# 1. Variables 

# -------------------------------------------------------------------------------------------------------------------------------- #

'''1. Create a variable named pi and store the value 22/7 in it. 
 Now check the data type of this variable. '''

pi = 22/7
print(type(pi))

# It's returninng float as the datatype 

# -------------------------------------------------------------------------------------------------------------------------------- #

'''2. Create a variable called for and assign it a value 4. See what
 happens and find out the reason behind the behavior that you
 see. '''

#for = 4  # Kindly Comment out this line for executing rest of the code !

# It will throw an error as the "for" is a reserved keyword having special meaning. So, it cannot be used as a variable name.

# -------------------------------------------------------------------------------------------------------------------------------- #

'''3. Store the principal amount, rate of interest, and time in
 different variables and then calculate the Simple Interest for 3
 years. Formula: Simple Interest = P x R x T / 100 '''

p = 2510     # Principal Amount 
r = 5        # Rate Of Intrest
time = 3     # Time 

si = ((p * r * time) / 100)  # Simple Intrest ((P x R x T) / 100)
print (si)

# The Output is 376.5 

# -------------------------------------------------------------------------------------------------------------------------------- #