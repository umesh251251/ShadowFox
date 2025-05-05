# 5. For Loop

#-------------------------------------------------------------------------------------------------------------------#

'''1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
 times). 
Count and print the following statistics: 
How many times you rolled a 6 
How many times you rolled a 1 
How many times you rolled two 6s in a row'''

import random
r = []
two_6_in_a_row = 0

for i in range(20):
    roll = random.randint(1, 6)
    r.append(roll)

    if i > 0 and roll == 6 and r[i - 1] == 6:
        two_6_in_a_row += 1

count_6 = r.count(6)
count_1 = r.count(1)

print("All rolls:", r)
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s were rolled in a row: {two_6_in_a_row}")

#-------------------------------------------------------------------------------------------------------------------#

'''2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks. 
Write a program that: 
Asks you to perform 10 jumping jacks at a time. 
After each set, it asks, "Are you tired?" 
If you reply "yes" or "y," it should ask if you want to skip the remaining sets. 
If you reply "yes" or "y," it should break and print, "You completed a total of jumping jacks." 
For example, if you did only 30 jumping jacks and answered "yes," the program
 will break and print, "You completed a total of 30 jumping jacks." 
If you reply "no" or "n," it should continue and display how many jumping jacks
 are remaining. After that, ask you again, "Are you tired?" 
For example, if you answered "no," it should display that 70 jumping jacks are
 remaining and ask you again, "Are you tired?" 
If you reply "no" or "n," it should continue and display how many jumping jacks
 are remaining. After that, ask you again, "Are you tired?" 
For example, if you answered "no," it should display that 70 jumping jacks are
 remaining and ask you again, "Are you tired?" 
If you complete all 100 jumping jacks, it should print, "Congratulations! You
 completed the workout," and stop the program
'''

total = 100
set_size = 10
done = 0

while done < total:
    done += set_size
    
    if done >= total:
        print("Congratulations! You completed the workout.")
        break

    remaining = total - done
    tired = input(f"You've done {done} jumping jacks. Are you tired? (yes/y or no/n): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
    else:
        print(f"{remaining} jumping jacks remaining.\n")

#-------------------------------------------------------------------------------------------------------------------#