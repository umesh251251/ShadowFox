# 4. If Condition 

#-------------------------------------------------------------------------------------------------------------------#

'''
1. Write a program to determine the BMI Category based on user input. Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

def BMI():                                                           
    h = float(input("Enter Your Height in metres : "))           
    w = float(input("Enter Your Weight in kilograms : "))       
    bmi = (w/(h*2))                

    if bmi >= 30 :                              
        print("Obesity")
    elif bmi > 25 and bmi <= 29 :       
        print("Overweight")
    elif bmi > 18.5 and bmi <= 25 :     
        print("Normal")
    elif bmi < 18.5 :                  
        print("Underweight")
    else :
        print ("Wrong Input")           

BMI()                  

#-----------------------------------------------------------------------------------------------------------------------#   

'''
2. Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi" 
Output: "Abu Dhabi is in UAE"
'''

Australia = ["sydney", "melbourne", "brisbane", "perth"]   
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]           
India = ["mumbai", "bangalore", "chennai", "delhi"]        
city = input("Enter a City Name : ").lower()                                

if city in Australia :                    
    print(f"{city} is in Australia")
elif city in UAE :                         
    print(f"{city} is in UAE")
elif city in India :                     
    print (f"{city} is in India")
else :
        print ("Wrong Input")        

#-------------------------------------------------------------------------------------------------------------------------#

'''
3. Write a program to check if two cities belong to the same country. 
Ask the user to enter two cities and print whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''

city1 = input("Enter the first City: ").lower()             
city2 = input("Enter the second City: ").lower()                               

if city1 in Australia and city2 in Australia :               
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE :                         
    print("Both cities are in UAE")
elif city1 in India and city2 in India :                  
    print ("Both cities are in India")
else :
    print ("They don't belong to the same country")         

#-----------------------------------------------------------------------------------------------------------------------------------------#