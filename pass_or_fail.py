# pass or fail calculator
# get the test score
score = int(input('Enter your test score: '))

# Did user pass?
if score > 59:
    print(f'Congrats \nYou passed the exam!')
else:
    print(f'Sorry you did not pass. \nStudy, and try again...')
