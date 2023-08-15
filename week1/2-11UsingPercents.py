#Variables
male = 0
female = 0
total = 0
percentMale = 0.0
percentFemale = 0.0

#Get num of male
male = int(input('Enter the number of male students: '))

# Get num female
female = int(input('Enter the number of female students: '))

# Calculate total
total = male + female

# Calc percent
percentMale = (male / total) * 100
percentFemale = (female /total) * 100

# Print percent male/female
print('Male:', format(percentMale, '.2f'), '%')
print('Female:', format(percentFemale, '.2f'), '%')
