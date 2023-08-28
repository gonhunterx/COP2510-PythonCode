# Get three test scores.
test1 = int(input('Enter first test score: '))
test2 = int(input('Enter second test score: '))
test3 = int(input('Enter third test score: '))

# Calculate the average.
avg = (test1 + test2 + test3) / 3

# Is this a high average?
if avg > 90:
    print("You're awesome!")

#Display average
print('Your average is', avg)
