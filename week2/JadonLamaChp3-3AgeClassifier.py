# Age Classifier
# Ask user to enter a persons age
age = float(input('Please enter a person\'s age: '))

# Check to see whether the person is an infant, a child, a teenager, or an adult
if(age < 1):
    print('They are an infant')
elif(age < 13):
    print('They are a child')
elif(age < 20):
    print('They are a teenager')
else:
    print('They are an adult')
