# 2. Numbers 

# ------------------------------------------------------------------------------------------------------ #

'''1. Write a function that takes two arguments, 145 and 'o', and
 uses the `format` function to return a formatted string. Print the
 result. Try to identify the representation used. '''

def function(a,b) :        
    return format(a,b)           # Returns formatted value

print(function(145,'o'))         # The 'o' format specifier stands for octal representation (base 8)

# It is returning 221 as the formatted result 

# ------------------------------------------------------------------------------------------------------ #

'''2. In a village, there is a circular pond with a radius of 84 meters.
 Calculate the area of the pond using the formula: Circle Area = π
 r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
 1.4 liters of water in a square meter, what is the total amount of
 water in the pond? Print the answer without any decimal point in
 it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
 Water per Square Meter '''

radius = 84       
pi = 3.14            
area = int(pi * radius ** 2)     
water = int(area * 1.4)             

print(f"The total area of pond is {area} and the total amount of water in the pond is {water} liters")

# Output is "The total area of pond is 22155 and the total amount of water in the pond is 31016 liters"

# ------------------------------------------------------------------------------------------------------ #

'''3. If you cross a 490 meter long street in 7 minutes, calculate your
 speed in meters per second. Print the answer without any decimal
 point in it. Hint: Speed = Distance / Time '''
    
distance = 490
time_in_minutes = 7
time_in_seconds = time_in_minutes * 60
speed = int(distance / time_in_seconds)

print(f"Your speed is {speed} meters per second")

# The calculated speed is 1

# ------------------------------------------------------------------------------------------------------ #