# python_exercises_review.py - this was my attempt at cleaning up my code to look like: https://github.com/jf-2020/day4/blob/master/python_review_exercises.py but
# this took too long and I gave up.  All exercises function correctly though. 
#
# ip - 4/18


#######################
### Day of the Week ###
#######################

## This uses lists, which we weren't supposed to use yet ##
'''
day = int(input('Day (0-6)? '))

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print(days[day])
'''
## This uses lists, which we weren't supposed to use yet ##



def day_of_week():
    '''
    param type  -> None
    return type -> String
    '''

    day = int(input("Day (0-6)? "))

    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"
    else:
        return "Please enter numbers (0-6)"

print(day_of_week())

'''
def main_0():
    # main function for Day of the Week problem

    ret_val = day_of_the_week()
    print(ret_val)
'''

# Work or Sleep In?

## This uses lists, which we weren't supposed to use yet ##
'''
day = int(input('Day (0-6)? '))

days = ['Sleep in','Go to work', 'Go to work', 'Go to work', 'Go to work', 'Go to work' ,'Sleep in']

print(days[day])
'''
## This uses lists, which we weren't supposed to use yet ##


'''
day = int(input('Day (0-6)? '))

if day == 0 or day == 6:
    print('Sleep in')
elif day < 6 and day > 0:
    print('Go to work')
'''

# Celsius to Fahrenheit
'''
celcius = int(input('Temperature in C? '))

farenheit = (celcius * 1.8) + 32
print(str(farenheit) + "F")

'''

# Tip Calculator
'''
bill = float(input('Total bill amount? '))
service_input = str(input('Level of service? '))

if service_input == 'good':
    tip_amount = .2 * bill
    total_bill = bill + tip_amount
    print('Tip amount: %.2f' % (tip_amount))
    print('Total amount: %.2f' % (total_bill) )
elif service_input == 'fair':
    tip_amount = .15 * bill
    total_bill = bill + tip_amount
    print('Tip amount: %.2f' % (tip_amount))
    print('Total amount: %.2f' % (total_bill) )
elif service_input == 'bad':
    tip_amount = .1 * bill
    total_bill = bill + tip_amount
    print('Tip amount: %.2f' % (tip_amount))
    print('Total amount: %.2f' % (total_bill) )
else:
    print('Please enter \'good\', \'fair\', or \'bad\'')

'''

# Tip Calculator 2

'''
bill = float(input('Total bill amount? '))
service_input = str(input('Level of service? '))
split_input = float(input('Split how many ways? '))

def output():
    print('Tip amount: %.2f' % (tip_amount))
    print('Total amount: %.2f' % (total_bill))
    print('Amount per person: %.2f' % (split))


if service_input == 'good':
    tip_amount = .2 * bill
    total_bill = bill + tip_amount
    split = total_bill / split_input
    output()

elif service_input == 'fair':
    tip_amount = .15 * bill
    total_bill = bill + tip_amount
    split = total_bill / split_input
    output()

elif service_input == 'bad':
    tip_amount = .1 * bill
    total_bill = bill + tip_amount
    split = total_bill / split_input
    output()
else:
    print('Please enter \'good\', \'fair\', or \'bad\'')

'''